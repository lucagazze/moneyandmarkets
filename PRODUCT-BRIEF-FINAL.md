# Money and Markets — Brief definitivo (locked)

Este documento reemplaza y resuelve las notas abiertas de `CURRICULUM-NOTES.md`.
Es la referencia única para contenido, copy, diseño y producto. Si algo de aquí
contradice al HTML actual, este documento gana — el HTML actual (copy, personas,
testimonios, sample pages, precios) es del currículum viejo (finanzas personales
para principiantes) y queda completamente reemplazado.

Fecha de cierre: 2026-09-19.

---

## 0. Qué cambia respecto al landing actual (para que quede escrito una vez)

El landing existente (`index.html`) fue construido para un público y un currículum
que ya no es el producto. Nada de su copy, personas, testimonios, páginas de
muestra o precios se conserva. Lo único que se reutiliza es el esqueleto técnico
(acordeón, carrusel de muestras, wiring de checkout, sistema de CSS).

| | Landing actual (obsoleto) | Producto final (este doc) |
|---|---|---|
| Avatar | Principiante total en finanzas personales (New Earner / Late Starter / Self-Taught) | Estudiante de finanzas/negocios o analista junior |
| Currículum | Interés compuesto, index funds, 401k/IRA | CAN SLIM + Wyckoff + Darvas + Weinstein + Minervini |
| Tono | "Sin la jerga de Wall Street", beginner-friendly | Desk, preciso, con umbrales — no guru |
| Precio | $13–65 sueltos, sin stack claro | $97 core + 4×$27 → $67 bundle |
| Diseño | Heredado de Physics Study Lab (páginas ilustradas, personajes) | Estética propia: mesa de trading, diagramas, sin personajes |

---

## 1. Marca y posicionamiento (cerrado)

- **Marca / sitio:** Money and Markets
- **Producto flagship (nombre del ebook):** *The Leader Screen* — a field manual
  for spotting growth leaders before the crowd explains them
- **Es:** sistema educativo de selección y timing de acciones de crecimiento,
  basado en CAN SLIM (O'Neil), conectado con Minervini (entrada), Darvas (cajas)
  y Weinstein (régimen de mercado)
- **No es:** curso de day trading, señales diarias, "hazte rico", resumen de
  *How to Make Money in Stocks*
- **Promesa permitida:** "Vas a saber qué mirar, en qué orden, y cuándo no operar."
- **Promesa prohibida:** cualquier % de retorno, "método de O'Neil garantizado",
  "CAN SLIM" como elemento de título/hero/marca.

### Avatar — dos capas, no una

- **Avatar de mensaje / hook (niching del copy):** estudiante de finanzas junior
  en Texas y Florida, 19–26 años. Sirve para afilar el mensaje y como primera
  cuña de ads (campus, CPMs bajos, sensación de relevancia local).
- **Avatar de compra / targeting real (no confundir con el de arriba):** cualquier
  estudiante de negocios/economía/finanzas o analista junior en EE.UU. que quiere
  pasar de teoría de clase a criterio de mesa. TX/FL es el ángulo de entrada, no
  el límite del producto.

---

## 2. Riesgos marcados (no ignorar)

1. **IP/marca de "CAN SLIM".** Es marca registrada de O'Neil/IBD. Se enseña el
   concepto con palabras propias + umbrales citados + ejemplos históricos
   públicos. "CAN SLIM" NUNCA en título del ebook, hero del landing, o creativos
   de ads — solo como mención técnica en el cuerpo del copy, con el disclaimer
   de no afiliación al lado.
2. **Regulatorio (FTC/SEC).** Contenido financiero recibe más escrutinio que un
   study guide. Ningún hook de la sección 6 va a ads pagados sin pasar filtro
   legal primero. Revisión legal real antes de tráfico pago — no "que alguien lo
   lea por arriba".
3. **Alcance vs. ejecución.** 14 capítulos + 4 bonos ya es mucho para un v1. El
   roadmap de secuelas (S1–S5) es backlog, no compromiso — se prioriza después
   del lanzamiento según qué bono genera más consultas/replies.
4. **Dirección visual no heredada.** Ver sección 5 — decisión explícita de NO
   usar el pipeline de páginas ilustradas de Physics Study Lab.

---

## 3. Arquitectura comercial (cerrado)

```
LEAD MAGNET (gratis): The 15-Minute Market Brief (recorte del Bono 2)
  → EBOOK PRINCIPAL: The Leader Screen ($97 valor core)
      + 4 BONOS ($27 c/u, $108 valor)
      = $205 valor tachado → $67 bundle de lanzamiento
         → BACKLOG (no v1): secuelas S1–S5, ver sección 8
```

| Ítem | Qué es | Rol |
|---|---|---|
| Core | Ebook *The Leader Screen* (90–120 pp) | Producto |
| Bono 1 | One-page CAN SLIM scorecard | Usabilidad |
| Bono 2 | 15-minute morning brief | Hábito |
| Bono 3 | Interview talk-track (8 respuestas) | Gancho de carrera |
| Bono 4 | Watchlist starter + reglas de NO-trade | Reduce pérdidas / retención |

---

## 4. Estructura del ebook (cerrado, con una modificación)

Se conserva la estructura de 14 capítulos del brief original, con un cambio:

> **El capítulo 13 ("The Texas–Florida lens") pasa de capítulo core a apéndice
> opcional.** Es el contenido más angosto geográficamente y el que menos le
> sirve a un lector fuera de esos dos estados. Como apéndice sigue funcionando
> como diferenciador de nicho para ads locales, sin diluir el cuerpo principal
> del libro para el resto de los compradores.

00. How to use this book
01. The student gap
02. What a leader looks like (without romance)
03. C — Current quarterly earnings
04. A — Annual earnings + quality
05. N — New
06. S — Supply and demand
07. L — Leader or laggard
08. I — Institutional sponsorship
09. M — Market direction (capítulo ancla)
10. Bases and entries (puente hacia S1, no agotar el tema acá)
11. Position sizing and exits
12. The Sunday night workflow
13. What this system is bad at
14. *(antes 14, ahora cierre)* — mismo contenido, renumerado tras mover TX/FL

**Apéndices:**
- A — Glosario
- B — Fuentes y lecturas
- C — Plantilla de scorecard (versión reducida)
- **D — The Texas–Florida lens** (movido desde capítulo core)

Reglas de contenido (sin cambios respecto al brief original):
- Ejemplos históricos ya cerrados, nunca tickers vigentes como recomendación.
- Todo umbral (EPS ≥25%, ROE ≥17%, etc.) se enseña como regla explícita, no
  como "vibe".
- Cero párrafos copiados de O'Neil/IBD.

---

## 5. Diseño — dirección propia, no heredada (cerrado)

Decisión explícita: **no se reutiliza el pipeline de páginas ilustradas de
Physics Study Lab** (personajes, escenas a color estilo GCSE). El avatar de
este producto (estudiante de finanzas que quiere verse serio, futuro analista)
no responde bien a una estética de guía ilustrada para adolescentes — juega en
contra de la credibilidad que el producto necesita transmitir.

**Dirección visual:** mesa de trading / manual de campo.
- Tipografía: serif para títulos, sans para cuerpo.
- Paleta: tinta, papel, un acento verde "tape" o ámbar "alert". Cero excesos
  visuales tipo "Lambo".
- Cada letra CAN SLIM = spread de 2 páginas con el umbral en una caja.
- Gráficos simples, blanco/negro + un color de acento.
- Checklists imprimibles al cierre de C, A, L, M.
- "Field notes" laterales con errores comunes de estudiante.

Esto implica un pipeline de generación de imágenes nuevo (diagramas/gráficos
limpios, no ilustración de personajes) — a definir cuando se pase a producción
de assets.

---

## 6. Landing page (cerrado en estructura, todo el contenido se reescribe)

Estructura de secciones sin cambios respecto al brief (hero → problem →
transformation → what you get → inside the system → who it's for/not for →
14-day usage → author → bonuses → price stack → FAQ → final CTA), en inglés.

**Todo el contenido actual del HTML (personas, testimonios, sample pages,
precios) se descarta y se reescribe desde cero** contra este brief — no hay
copy reciclable del currículum de finanzas personales.

10 hooks para contenido/ads — recordatorio: **pasan filtro legal antes de
usarse en ads pagados**, el landing es más permisivo que la revisión de
Meta/Google para productos financieros.

---

## 7. Legal (no negociable)

Disclaimer base (revisión legal real pendiente, esto es el piso):

> Educational material only. Not investment advice, not a solicitation to buy
> or sell any security. Past characteristics of winning stocks do not predict
> future results. You can lose money. The CAN SLIM framework was developed by
> William J. O'Neil; this work is an independent educational interpretation and
> is not affiliated with, endorsed by, or sponsored by William O'Neil + Co.,
> IBD, or MarketSurge.

Gate de lanzamiento: **no se corre tráfico pago hasta que un abogado revise
disclaimer + hooks de ads**, no solo una lectura interna.

---

## 8. Backlog (no comprometido para v1)

| # | Título interno | Tema |
|---|---|---|
| S1 | *The Pivot* | Cup-handle, VCP, Darvas box, stops 3–8% |
| S2 | *The M Manual* | Fed, curva, liquidez, dollar, risk-on/off |
| S3 | *The Lineage* | Livermore, Darvas, Weinstein, Minervini, Lynch |
| S4 | *Energy & Rate Tape* | Texas lens ampliado |
| S5 | *Monetary Field Notes* | Historia monetaria en lenguaje de trader |

Se prioriza después del lanzamiento de v1, según señal real (qué bono/capítulo
genera más consultas o replies en la secuencia post-compra).

---

## 9. Definición de "listo" para publicar (sin cambios respecto al brief)

- Umbrales de C/A/L/M escritos como reglas, no como vibes.
- Capítulo "cuándo no sirve" presente.
- Disclaimer en portadilla, revisado por legal.
- Cero recomendaciones de tickers vigentes.
- Scorecard usable en 3 minutos.
- Landing dice explícitamente para quién NO es.
- "CAN SLIM" ausente de título, hero y creativos de ads.

---

## 10. Próximos pasos sugeridos (orden de ejecución)

1. Draft de capítulos 03–09 + 12 (el núcleo CAN SLIM + workflow) — máxima prioridad de contenido.
2. Bonos 1 y 2 (Scorecard + Morning Brief) — el lead magnet sale de acá.
3. Definir el pipeline de diseño nuevo (diagramas/gráficos, no ilustración de personajes).
4. Reescritura completa del landing (copy, personas, sample pages, precios).
5. Checkout + pixel propio (nunca reusar el de Physics Study Lab).
6. Revisión legal de disclaimer + hooks antes de cualquier ad pago.
7. Soft launch a ~20 personas del avatar antes de escalar tráfico.
