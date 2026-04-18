# Maths — Complex numbers (HTML)

This folder contains a **single static web page**, `index.html`, that explains **complex numbers** in plain language: the imaginary unit **i**, the Argand plane, modulus **r** and argument **θ**, addition and multiplication, **Euler’s formula**, why complex numbers matter in science and engineering, and a short historical note.

The page is presented as a **Hal AI by CJF** branded educational note with interactive canvas diagrams and the standard header logo used across the Maths collection.

## What the page covers

- **What a complex number is** — **z = a + bi** as coordinates **(a,b)** in the plane; **|z|** as distance from the origin (hypotenuse), and why **i** ties geometry to multiplication
- **What i is** — **i² = −1** and extending the number system
- **Polar form** — **r = |z|** (same quantity: hypotenuse / radius, **√(a²+b²)**), argument **θ**, and the right-triangle link to **a**, **b**
- **Addition** — componentwise sum and the parallelogram rule
- **Multiplication** — algebraic rule; polar view (moduli multiply, arguments add) and rotation–scaling; Euler’s rule linked to the same angle-addition picture
- **Euler’s formula** — **e^(iθ) = cos θ + i sin θ** and **z = r e^(iθ)**; link to the companion page on **e**
- **Why they matter** — quantum mechanics, electrical phasors, Fourier analysis, dynamics, fundamental theorem of algebra
- **History** — Cardano, Bombelli, Argand/Wessel, Gauss, Hamilton (brief)

## Interactive features

- **Argand diagram** — drag the point or use sliders; shows **r**, **θ**, and the real/imaginary legs
- **Addition diagram** — two numbers and their sum with adjustable components (same geometry as **vector addition**; see the linked **[Vectors in the plane](../Vectors/index.html)** guide)
- **Multiplication diagram** — polar-style controls with **θ₁**, **θ₂**, **θ₁+θ₂** arcs from the axis; a softer arc for **arg(z₂)** and a brighter dashed **+θ₂** arc between the **z₁** and **z₁z₂** rays; sliders for **z₁** and **z₂** use **green** and **violet** accents to match the diagram
- **Reset** — each diagram section has a **Reset** button that restores that section’s default slider values (see below)
- **Snap → π/2 grid** (multiplication only) — snaps **θ₁** or **θ₂** to the nearest of **0**, **±π/2**, **±π** on the slider scale (nearest principal axis in this range)

## Default slider positions

- **Polar form** (**a**, **b** on −3…3): **2.1** for both (~85% of the span) — strong default in the first quadrant.
- **Addition** (rectangular components on −2.5…2.5): **z₁** = **1 + 0.6i**, **z₂** = **−0.4 + 1.1i** (original illustrative defaults for the parallelogram).
- **Multiplication** (angle inner scale −314…314, moduli 0.2…2): **θ₁** and **θ₂** at **220** and **214** (i.e. **2.20** and **2.14** rad when scaled); **|z₁|** and **|z₂|** at **1.73** (~85% of the modulus span). **Reset** restores these values.

**Angle sliders:** the stored value is an integer; **radians = slider value × 0.01** (hundredths of a radian).

## How to view

Open `index.html` in any modern web browser, or publish the folder on **GitHub Pages** and open the site URL.

**iPhone / iPad:** In Safari, tap **Share → Add to Home Screen**. The file `apple-touch-icon.png` is included as a **180 × 180** home-screen icon; the mobile web app title is set to **Complex numbers**.

**Note:** The page loads **KaTeX** from a CDN for typeset mathematics. Use an internet connection for first load, or host KaTeX locally if you need fully offline use.

## Assets in this folder

| File | Purpose |
|------|---------|
| `index.html` | Main educational page about complex numbers |
| `README.md` | Project summary and usage notes |
| `header-logo.svg` | Official Hal AI by CJF header logo used on the page |
| `favicon.svg` | Browser tab icon (shared style with other Maths pages) |
| `apple-touch-icon.png` | **180 × 180** PNG for iPhone / iPad **Add to Home Screen** |
| `build_apple_icon.py` | Generates `apple-touch-icon.png` (requires [Pillow](https://pypi.org/project/Pillow/)) |

## Notes

- The entry file **must** be named **`index.html`** with a **lowercase** `i`. On case-sensitive web servers (typical for **GitHub Pages** and many Linux hosts), `Index.html` is a different path and may not be used as the folder’s default document.
- No build step is required to use the page.
- The page is client-side HTML, CSS, canvas, JavaScript, and optional CDN KaTeX.
- Range controls use a visible **focus** style (keyboard / screen-reader friendly).
- The content is intended as a clear visual introduction rather than a full formal course.

---

*Educational summary only — intended as an accessible introduction to complex numbers and their geometric meaning.*
