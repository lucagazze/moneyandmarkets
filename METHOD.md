# Finance Study Lab — método de trabajo

Portado de Physics Study Lab el 2026-10-08, a pedido de Bruno. Cada regla está
acá porque **romperla ya costó trabajo real**, y el costo está anotado. Una
norma sin su motivo se olvida en tres semanas.

---

## 1. Los libros se escriben como fuente, nunca como imágenes

**La regla.** El contenido vive en archivos de texto. El PDF se *compila* desde
ahí. Ninguna página se genera como imagen plana.

**Lo que costó no hacerlo.** The Final Book of Physics eran 127 PNG sin fuente.
No se podía buscar una palabra, no se podía arreglar una errata sin regenerar la
página entera, y nadie podía auditar el contenido porque no había contenido que
leer: había píxeles. Reconstruirlo fue un trabajo completo, y la auditoría que
recién entonces se pudo correr encontró **18 errores de física y 6 imprecisiones**
que llevaban meses impresos.

En finanzas el riesgo es peor que en física. Un umbral mal escrito —EPS ≥25%
tipeado como ≥2.5%— es indetectable en una imagen y enseña a la gente a operar
con una regla falsa.

**Cómo se hace.** HTML → Chrome headless → PDF. Da texto real seleccionable,
A4 exacto, fuentes incrustadas y recuento de páginas verificable.

    content/   el texto y la estructura, en claro
    build/     el renderizador, el verificador y la auditoría
    out/       el PDF compilado (nunca al repo)

## 2. Nada se afirma sin medirlo

**La regla.** Recuento de páginas, márgenes de audio, caracteres de un anuncio,
área bajo una curva: se miden con un script y se reporta el número.

**Lo que costó no hacerlo.** El ajuste de figuras del libro de física se
calculaba en cada compilación y **nunca se le pasaba al compilador** — tres
minutos de medición tirados y ocho páginas partidas en dos. El error sobrevivió
semanas porque el valor por defecto del CSS lo tapaba. También: una curva de
efecto túnel "típica" dejaba pasar 4 píxeles y el dibujo mostraba lo contrario
de lo que narraba la voz.

**Cómo se hace.** Un `check.py` que sale con código distinto de cero si algo
falla. Si el verificador no puede fallar, no es un verificador.

## 3. Las correcciones se registran, no se editan encima

**La regla.** Todo cambio al texto va a `corrections.py` como una tupla
`(página, texto viejo exacto, texto nuevo, motivo)`. El original queda intacto.

**Por qué.** Permite comparar ediciones, deshacer una sola corrección, y
—sobre todo— que exista una lista de qué se cambió y por qué. En física son 27
entradas y cada una tiene su razón escrita.

**Detalle que importa:** si una corrección no encuentra su texto, el script
**revienta**. Una corrección que falla en silencio es peor que ninguna.

## 4. Todo umbral es una regla explícita, con su fuente

**La regla.** Ningún número se enseña como intuición. EPS ≥25%, ROE ≥17%, el
volumen contra su media: cada uno aparece como regla, con de dónde sale.

**Por qué acá y no en física.** En física un error es un error. Acá alguien
puede poner plata sobre un umbral mal copiado. Y además el brief lo exige:
*"todo umbral se enseña como regla explícita, no como vibe"*.

**Y nunca un ticker vigente como recomendación.** Solo ejemplos históricos ya
cerrados. Está en el brief y no se negocia.

## 5. Cero párrafos copiados de O'Neil / IBD

Está en el brief. El libro explica un método público con palabras propias,
ejemplos propios y gráficos propios. Las fuentes van en el apéndice B.

## 6. Lo pago nunca entra al repo

**La regla.** `.gitignore` bloquea `img/book/`, `img/book-b-leader-screen/` y
`*.pdf`. Las muestras del landing viven sueltas en `img/` y están permitidas.

**Lo que casi costó.** En física, 169 MB de PDFs pagos a un `git add .` de
quedar publicados gratis en un repo público que despliega el sitio. Acá eran 18
MB de páginas sin seguimiento, tapado el 2026-10-08.

## 7. Lo que se afirma en la venta tiene que existir en el producto

**La regla.** Antes de escribir copy, se verifica contra el archivo que se
entrega. Números de página, cantidad de capítulos, qué incluye.

**Lo que costó no hacerlo.** Una auditoría de la landing de física encontró
**cuatro afirmaciones falsas**. Y acá, hoy, el landing dice *"3,200+ students"*
cuatro veces y tiene 50 bloques de testimonio para un producto que todavía no se
puede comprar — los seis botones apuntan a `#offerta`, un ancla interna heredada
del template italiano.

**Decisión pendiente de Bruno.** Está marcado, no corregido.

---

## 7b. Una sola línea editorial, del más básico al pro

Bruno, 2026-10-08: *"quiero que sea todo a nivel profesional, que se explique
para todo público, apto e intuitivo, con buenas ilustraciones, como THE FINAL
BOOK, pero con textos a nivel profesional y entendible para cualquiera. Todo
bajo la misma línea desde el primer producto, más básico, hasta el pro."*

**Esto resuelve una tensión que estaba mal planteada.** "Ilustrado" son dos
cosas distintas y yo las había tratado como una:

- **Ilustración de personajes** — escenas a color, estilo guía para
  adolescentes. Es lo que la sección 5 del brief descarta, y con razón: le
  quita credibilidad a un libro que lee un futuro analista.
- **Diagrama técnico** — la anatomía de The Final Book. Eso **sí** es
  profesional, y es exactamente lo que este libro necesita.

**La anatomía de página, que se respeta en los tres niveles:**

    banda superior navy
    encabezado:  PARTE — NOMBRE                        nº de página
    ────────────────────────────────────────────────────────────────
    título serif numerado   (3.2  Return on equity)
    cuerpo justificado, serif, texto corrido

           [ diagrama de línea, centrado, tinta sobre crema ]

    Figura 3.2: pie de figura en cuerpo menor
    ────────────────────────────────────────────────────────────────
    KEY IDEA
    una frase. la que te llevás si no leés nada más.
    ────────────────────────────────────────────────────────────────
                            nº de página

Papel crema, tinta navy, un acento. Serif en títulos y cuerpo, sans para
etiquetas de figura. Gráficos en blanco y negro con un color de acento.

**El escalón entre productos es de PROFUNDIDAD, no de seriedad.** El de entrada
no es "la versión con dibujitos": es el mismo libro con menos alcance. Alguien
que compra el de $19 y después el de $67 tiene que sentir que son del mismo
autor y de la misma editorial.

**Y "entendible para cualquiera" no significa simplificar la física del
negocio.** Significa: una idea por párrafo, el término técnico definido la
primera vez que aparece, un ejemplo numérico cada vez que hay una fórmula, y
cero jerga usada para sonar inteligente. El capítulo 3 abre explicando por qué
la comparación es interanual y no contra el trimestre anterior — eso es
accesible y profesional a la vez, que es lo que se pide.

---

## 8. Reels — el formato queda fijo

Bruno lo confirmó el 2026-10-08: le gustan los últimos y ese es el estándar
hacia adelante, también para finanzas.

**La división del trabajo, que es lo que hace que funcione:**

> **El dibujo lleva la física (o la matemática). El muñeco lleva la emoción.**

El diagrama va en vector, porque en estos reels **el movimiento es el contenido**
y tiene que ser exacto. Los personajes 3D brillantes le ponen cara, humor y
escala humana, y van **chicos, encima del diagrama** — un actor sobre un gráfico,
no un reemplazo del gráfico.

**Lo que no se hace:** meter dos respuestas a la misma pregunta en el mismo
cuadro. Un puente de juguete *y* un puente dibujado era eso; parar al muñeco
encima del dibujo los volvió una sola imagen.

**Reglas heredadas, todas con su cicatriz:**

- **Nada de Veo cuando el movimiento es la lección.** Rompió la física en 3 de 3
  intentos: prendió una lámpara que debía apagarse, levantó un pistón atornillado.
- **Los assets generados no llevan texto.** Los modelos escriben mal, y un rótulo
  es lo único que el espectador lee de cerca. Van dibujados en código.
- **Todo personaje, saturado.** Un personaje pálido sobre ciclorama claro no se
  lee en un teléfono y es imposible de recortar.
- **El encuadre, abajo y grande.** Se cayó en el mismo error cuatro veces: todo
  arriba y el tercio inferior muerto. En un teléfono se lee como un recorte fallado.
- **El nivel de música se mide por reel.** Cada pista de Lyria vuelve distinta.
  El estándar aprobado es el **margen** —voz 12 a 20 dB sobre la cama—, no el
  número de volumen. En cuatro reels salió 0.12, 0.15, 0.15 y 0.22.
- **El cierre se agacha bajo la voz**, con profundidad por reel, porque las camas
  crecen al final y pisan el llamado a la acción.

**Material compartido** (en `physicstudylab-videos/`, reutilizable acá):
`public/cast/` con su README de estilo, `src/SeriesKit.tsx`, `src/PslOutro.tsx`.
Finanzas necesitará su propio cierre y probablemente su propio reparto —el
avatar es un futuro analista, no un adolescente— pero el método es el mismo.

---

## 9. El orden de trabajo, según el propio brief

1. Capítulos **03–09 y 12** — el núcleo CAN SLIM y el workflow. Máxima prioridad.
2. Bonos 1 y 2 (Scorecard + Morning Brief) — de ahí sale el lead magnet.
3. Pipeline de diseño: diagramas y gráficos limpios, no ilustración de personajes.
4. Reescritura completa del landing.
5. Checkout + pixel propio.
6. Revisión legal del disclaimer antes de cualquier ad pago.
7. Soft launch a ~20 personas del avatar antes de escalar tráfico.

**Estado al 2026-10-08:** el landing está terminado y el contenido al 20%.
Libro A tiene 11 páginas (todas Livermore); libro B tiene 15 (capítulos 2-6).
Los capítulos 3-9 no están empezados. Y los dos libros están en formatos
distintos, **ninguno A4**: 1.792 (que es 9:16, el formato prohibido para libros)
y 1.281.
