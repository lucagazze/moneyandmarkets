#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cablea los 7 botones de la landing al checkout real.

Hoy todos apuntan a `#offerta`, un ancla interna: el visitante hace clic, la
pagina salta a la caja de oferta y no pasa nada mas. Este script los reemplaza
por la URL de Impultienda de una sola pasada, para que no quede ninguno sin
cambiar -- que es exactamente como se pierde una venta sin enterarse.

Uso:
    python3 connect-checkout.py https://checkout.financestudylab.com/checkout/xxxx
    python3 connect-checkout.py --revert     # vuelve a #offerta
"""
import pathlib, re, shutil, sys

HTML = pathlib.Path(__file__).parent / "index.html"
BAK = pathlib.Path(__file__).parent / ".index-before-checkout.html"


def wire(url):
    s = HTML.read_text()
    n = s.count('href="#offerta"')
    if not n:
        print("  no hay botones apuntando a #offerta -- ¿ya estaban cableados?")
        return 1
    shutil.copy(HTML, BAK)
    s = s.replace('href="#offerta"', f'href="{url}"')
    # los enlaces externos se abren en la misma pestaña a proposito: mandar el
    # checkout a otra pestaña pierde al comprador que cierra la que tenia
    HTML.write_text(s)
    print(f"  {n} botones -> {url}")
    print(f"  copia de seguridad en {BAK.name}")
    return 0


def revert():
    if not BAK.exists():
        print("  no hay copia de seguridad"); return 1
    shutil.copy(BAK, HTML); print("  landing restaurada a #offerta"); return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--revert":
        sys.exit(revert())
    u = sys.argv[1]
    if not re.match(r"^https://", u):
        sys.exit("  la URL tiene que empezar por https://")
    sys.exit(wire(u))
