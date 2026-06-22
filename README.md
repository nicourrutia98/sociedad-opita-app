# Sociedad Opita — Bundle del monumento digital vivo

> El primer monumento digital vivo de una comunidad colombiana.
> Tello, Huila, Colombia.

---

## ¿Qué es este repo?

Este repo contiene **el bundle compilado** del monumento digital vivo que vive en
[`sociedad.opitacode.com`](https://sociedad.opitacode.com). Es el resultado del
proceso de build de Astro 5 + React 19 + Tailwind 3.4 + Pixi.js 8.6 + D3 7.9.

**Este repo NO contiene el código fuente Astro**. El código fuente se construye
externamente y se compila a este bundle. Versionamos el bundle aquí para tener
un historial completo de cada deploy, poder hacer rollback a cualquier versión
anterior, y servir de auditoría pública del estado real del sitio.

> "Hecho por un nativo huilense, en el Huila, con IA,
> para que Tello no se muera cuando los pelaos se vayan pa' Bogotá."
> — Juan Nicolás Urrutia Salcedo, operador del proyecto

---

## Estado actual

| Sección | Ruta | Concepto | Estado |
|---|---|---|---|
| Landing principal | `/` | El monumento y sus 4 dimensiones | ✅ |
| **La Ventana** | `/ventana` | Mira el pueblo correr (reloj virtual) | ✅ |
| **El Puente** | `/puente` | Háblale a sus personajes (chat LLM) | ✅ |
| **La Réplica** | `/replica` | Extiende el monumento a tu municipio | ✅ |
| **El Taller** | `/taller` | El detrás de escena académico | ✅ |
| **Pronto** | `/pronto` | Placeholder (próxima dimensión) | ⚠️ |

Consulta [`VISUAL-HONESTY.md`](VISUAL-HONESTY.md) para entender qué imágenes
muestra el bundle, de dónde vienen, y qué no son.

---

## Estructura

```
sociedad-opita-app/
├── index.html                       # Landing principal
├── ventana/                         # Sección "La Ventana"
├── puente/                          # Sección "El Puente"
├── replica/                         # Sección "La Réplica"
├── taller/                          # Sección "El Taller"
├── pronto/                          # Placeholder de próxima dimensión
├── _astro/                          # JS + CSS bundleado por Astro
├── persona-*.{svg,jpg}              # Retratos de las 10 personas validadas
├── tile-*.jpg                       # Imágenes Wikimedia para las 4 secciones
├── hero-tello-landscape.jpg         # Hero panorámica (Wikimedia, Gigante)
├── plaza-similar-tello.jpg          # Foto plaza (Wikimedia, Huila)
├── favicon.svg, robots.txt,
│   sitemap.xml, og-image.jpg        # SEO + social
├── VISUAL-HONESTY.md                # Declaración visual honesta (LEER)
├── LICENSE                          # CC-BY-4.0
└── downloads/                       # Corpus descargable (papers, artesanías)
    ├── papers-tello.bib             # 204 papers académicos
    ├── papers-tello-priority.bib    # Subset con URL verificada
    ├── papers-tello-summary.md      # Resumen metodológico
    └── artesanias/                  # 8 reportes de Artesanías de Colombia
```

---

## Deploy

Este bundle se despliega en `sociedad.opitaode.com` vía:

1. **AWS S3** (`s3://sociedad-opita-app-prod/`) — origen
2. **CloudFront** (`E9NPTPSJGKRMQ`) — CDN edge, redirect-to-https, TTL 300s
3. **Route 53** (`opitacode.com` hosted zone) — DNS autoritativo
4. **ACM** (`d618be91-...`) — TLS cert en us-east-1
5. **Cloudflare** — capa CDN/proxy opcional

### Deploy manual (3 pasos)

```bash
# 1. Sync bundle a S3
aws s3 sync . s3://sociedad-opita-app-prod/ --delete --cache-control "max-age=300"

# 2. Invalidar cache de CloudFront
aws cloudfront create-invalidation --distribution-id E9NPTPSJGKRMQ --paths "/*"

# 3. Verificar
curl -I https://sociedad.opitacode.com
```

### Rollback (con S3 versioning habilitado)

```bash
# Listar versiones
aws s3api list-object-versions --bucket sociedad-opita-app-prod

# Restaurar versión anterior
aws s3api restore-object --bucket sociedad-opita-app-prod --key index.html --version-id <ID>
```

---

## Las 4 dimensiones del monumento

El bundle NO es un SaaS, NO es un juego, NO es una red social. Es un **monumento**
diseñado para 3 audiencias que convergen en la landing y divergen según su intención:

| Audiencia | Sección primaria | Qué busca |
|---|---|---|
| 🏘️ **Pueblo** (curioso, nativo, familia) | `/ventana`, `/puente` | Reconocerse, conversar, recordar |
| 🔬 **Académico / Científico** | `/taller` | Paper, BibTeX, ground-truth, replicar |
| 🤝 **Aliado institucional** (alcaldía, universidad, embajada) | `/replica` | Llevar el monumento a su municipio |

**Regla dura** (inalterable): El producto NO se adapta a la monetización. La
monetización emerge del uso real. Ver
[`REPLANTEAMIENTO-COMERCIAL.md`](https://github.com/nicourrutia98/sociedad-opita/blob/main/docs/deployment/REPLANTEAMIENTO-COMERCIAL.md)
en el repo académico.

---

## Honestidad visual

Las imágenes de este bundle son de **tres tipos, declarados honestamente**:

1. **62 fotografías reales de Wikimedia Commons** (CC-BY-SA-4.0) de municipios del
   mismo terreno andino-Magdalena que Tello (Neiva, Gigante, San Agustín, etc.).
   Son la familia visual de Tello, NO son Tello.
2. **2 retratos AI-generated** (Doña Prudencia, Don Eliécer) declarados como
   "Retrato AI — no fotográfico documental".
3. **7 marcadores tipográficos SVG** (iniciales serif sobre fondo arena) como
   placeholder honesto hasta que llegue fotografía real con consentimiento.

15 imágenes AI marcadas como AI_SLOP **NO se usan** (anatomía incorrecta, ojos
muertos, fondo derretido). Preferimos marcadores honestos a AI slop.

Ver [`VISUAL-HONESTY.md`](VISUAL-HONESTY.md) para los detalles completos.

---

## Memoria histórica — La Masacre del Puente de los Decapitados (1950)

Esta sección existe porque un monumento cultural que ignora 1950 no es un
monumento — es propaganda. Pero el tono es deliberado: **dignidad, no morbo**.
Honramos a los muertos sin reducir la memoria a trauma.

> "El monumento a Tello no es solo el que sobrevive — es también el que recuerda."

La masacre NO se replica como contenido interactivo, NO se usa como mecánica
emocional, NO se cuantifica. Es contexto fundacional: explica por qué un pueblo
de 12.908 habitantes decide hoy preservar su voz antes de que se apague.

Ver `/taller` para los detalles.

---

## Bitácora del proyecto

Este repo sigue un sistema anti-deuda-técnica de **3 piezas por deploy**:

1. **Tag semver** (ej. `v0.1.0`)
2. **Entrada en bitácora** del proyecto
3. **Post-mortem en skill** (documenta qué funcionó y qué falló)

Si no puedo hacer las 3, no deployo. Ver
[`DEPLOY-PROCESS.md`](https://github.com/nicourrutia98/sociedad-opita/blob/main/docs/deployment/DEPLOY-PROCESS.md)
en el repo académico.

---

## Versión actual

**v0.1.0** — Bundle inicial descargado de S3 `sociedad-opita-app-prod` el
2026-06-22, marcando el inicio del versionado público del bundle.

Próximas versiones:
- **v0.2.0** — 5ª Dimensión "La Memoria Viva" (cuando se implemente)
- **v0.3.0** — In-app feedback collection system (cuando se implemente)
- **v1.0.0** — Cuando el monumento esté maduro sin breaking changes esperados

---

## Licencia

**CC-BY-4.0** (Creative Commons Atribución 4.0 Internacional) para todo el
contenido del bundle (HTML, CSS, JS, imágenes, textos). Ver [`LICENSE`](LICENSE).

Las fotos individuales de Wikimedia Commons mantienen su licencia original
(CC-BY-SA-4.0 en su mayoría). Atribución completa en cada `<figcaption>` del sitio.

---

## Contacto

- **Operador**: Juan Nicolás Urrutia Salcedo
- **GitHub**: [@nicourrutia98](https://github.com/nicourrutia98)
- **Instagram**: [@nico98urrutia](https://instagram.com/nico98urrutia)
- **WhatsApp**: [+57 312 612 6085](https://wa.me/573126126085)
- **Sitio**: [sociedad.opitacode.com](https://sociedad.opitacode.com)

---

## Repos relacionados

- [`nicourrutia98/sociedad-opita`](https://github.com/nicourrutia98/sociedad-opita) —
  Repo académico: simulación Python + biografías forenses + paper + docs estratégicos
- `anomalyco/sociedad-opita-app-v2` — Repo del código fuente Astro (privado, no público)

---

> "Sociedad Opita es un proyecto personal de Juan Nicolás Urrutia Salcedo.
> Código abierto. Datos abiertos. Idioma preservado."