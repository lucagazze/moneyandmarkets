#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rehace img/pages-collage.webp: el abanico de paginas con la tapa al frente.

POR QUE SE REHIZO
  El archivo anterior (1500x1920) cortaba por el borde del lienzo las paginas
  de los costados y las de abajo. No era un problema de CSS: los pixeles no
  estaban en la imagen. Agregar margen no lo arregla, hay que recomponer.

COMO EVITA QUE SE VUELVA A CORTAR
  No se acomoda a ojo. Cada pagina se rota primero, se mide su caja real ya
  rotada, y recien ahi se decide el lienzo: se toma la union de todas las
  cajas y se agrega MARGEN. Si una pagina se mueve o se rota distinto, el
  lienzo se agranda solo. Al final verifica y falla si algo quedo a menos de
  MARGEN del borde.

  python3 armar-collage.py
"""
import math, pathlib, sys
from PIL import Image, ImageFilter

RAIZ = pathlib.Path(__file__).parent / "img"
SALIDA = RAIZ / "pages-collage.webp"
MARGEN = 48          # px de aire garantizado entre lo dibujado y el borde
ESCALA_HOJA = 0.60   # tamano de las paginas de atras, sobre el original
ESCALA_TAPA = 0.78   # la tapa, mas grande: es la que manda

# Las ocho paginas alrededor de la tapa: (archivo, angulo, dx, dy) en px sobre
# el centro. Angulo en grados, positivo = antihorario.
HOJAS = [
    ("page-1.jpg", 10, -430, -330),
    ("page-2.jpg", 3, -140, -430),
    ("page-3.jpg", -7, 300, -360),
    ("page-4.jpg", 12, -470, 190),
    ("page-5.jpg", -10, 420, 150),
    ("page-6.jpg", 7, -330, 450),
    ("page-7.jpg", -4, 40, 500),
    ("page-8.jpg", -12, 360, 470),
]


def cargar(nombre, escala):
    im = Image.open(RAIZ / nombre).convert("RGBA")
    return im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)


def con_sombra(im, radio=18, desvio=(0, 10), opacidad=70):
    """Sombra suave: sin esto las paginas se ven pegadas, no apiladas."""
    sombra = Image.new("RGBA", (im.width + radio * 4, im.height + radio * 4), (0, 0, 0, 0))
    silueta = Image.new("RGBA", im.size, (14, 23, 48, opacidad))
    silueta.putalpha(im.getchannel("A").point(lambda a: min(a, opacidad)))
    sombra.paste(silueta, (radio * 2 + desvio[0], radio * 2 + desvio[1]), silueta)
    sombra = sombra.filter(ImageFilter.GaussianBlur(radio))
    sombra.paste(im, (radio * 2, radio * 2), im)
    return sombra


def main():
    faltan = [n for n, *_ in HOJAS if not (RAIZ / n).exists()]
    if not (RAIZ / "cover.jpg").exists():
        faltan.append("cover.jpg")
    if faltan:
        sys.exit(f"\n  Faltan imagenes en img/: {', '.join(faltan)}\n")

    # 1. Rotar todo primero, para conocer el tamano REAL de cada pieza.
    piezas = []  # (imagen ya rotada y con sombra, centro x, centro y)
    for nombre, angulo, dx, dy in HOJAS:
        im = con_sombra(cargar(nombre, ESCALA_HOJA))
        im = im.rotate(angulo, resample=Image.BICUBIC, expand=True)
        piezas.append((im, dx, dy))
    tapa = con_sombra(cargar("cover.jpg", ESCALA_TAPA), radio=26, desvio=(0, 16), opacidad=95)
    piezas.append((tapa, 0, 0))

    # 2. El lienzo sale de la union de las cajas, no de un numero inventado.
    izq = min(dx - im.width / 2 for im, dx, dy in piezas)
    der = max(dx + im.width / 2 for im, dx, dy in piezas)
    arr = min(dy - im.height / 2 for im, dx, dy in piezas)
    aba = max(dy + im.height / 2 for im, dx, dy in piezas)
    W = round(der - izq) + MARGEN * 2
    H = round(aba - arr) + MARGEN * 2
    cx, cy = -izq + MARGEN, -arr + MARGEN

    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for im, dx, dy in piezas:
        lienzo.alpha_composite(im, (round(cx + dx - im.width / 2), round(cy + dy - im.height / 2)))

    # 3. Verificar: ninguna tinta a menos de MARGEN del borde.
    caja = lienzo.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    aire = (caja[0], caja[1], W - caja[2], H - caja[3])
    print(f"  lienzo {W}x{H}   aire izq/arr/der/ab: {aire}")
    if min(aire) < MARGEN - 2:
        sys.exit(f"\n  Algo quedo pegado al borde (aire minimo {min(aire)}px, pedido {MARGEN}px).\n")

    # Fondo del sitio, para que no se vea un rectangulo transparente.
    fondo = Image.new("RGB", (W, H), (255, 255, 255))
    fondo.paste(lienzo, (0, 0), lienzo)
    fondo.save(SALIDA, "WEBP", quality=88, method=6)
    kb = SALIDA.stat().st_size / 1024
    print(f"  escrito {SALIDA.name}: {W}x{H}  {kb:.0f} KB  (nada tocando el borde)")


if __name__ == "__main__":
    main()
