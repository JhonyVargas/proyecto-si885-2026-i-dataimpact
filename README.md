# Dashboard de empleabilidad — Egresados de Ingeniería de Sistemas, UPT

Solución de Inteligencia de Negocios para el seguimiento de la empleabilidad de
los egresados de la Escuela Profesional de Ingeniería de Sistemas de la
Universidad Privada de Tacna, promociones **2017–2024**.

Curso: **SI885 — Inteligencia de Negocios** (2026-I)

[![CI](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/actions/workflows/ci.yml/badge.svg)](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/actions/workflows/ci.yml)
![Curso](https://img.shields.io/badge/Curso-SI885_Inteligencia_de_Negocios-8B1E3F?style=flat)
![Promociones](https://img.shields.io/badge/Promociones-2017--2024-4C566A?style=flat)
![Egresados](https://img.shields.io/badge/Egresados-139-4C566A?style=flat)
![Cobertura](https://img.shields.io/badge/Cobertura_de_informaci%C3%B3n-25.2_%25-D08770?style=flat)

### Stack tecnológico

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-1.4-FFF000?style=flat&logo=duckdb&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-modelo_estrella-00758F?style=flat&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-tablero-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-tema_claro/oscuro-1572B6?style=flat&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-sin_dependencias-F7DF1E?style=flat&logo=javascript&logoColor=black)
![pytest](https://img.shields.io/badge/pytest-19_pruebas-0A9EDC?style=flat&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?style=flat&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-control_de_versiones-F05032?style=flat&logo=git&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-docs-000000?style=flat&logo=markdown&logoColor=white)
![Mermaid](https://img.shields.io/badge/Mermaid-diagramas-FF3670?style=flat&logo=mermaid&logoColor=white)

### Integrantes

| Integrante | Código |
|---|---|
| Pacompía Ortiz, Abel Fernando | 2023076797 |
| Cruz Mamani, Victor Williams | 2022073903 |
| Vargas Luque, Jhony | 2022075754 |

Docente: **Mag. Patrick José Cuadros Quiroga**

---

## Qué mide y qué no

Este es el punto metodológico central del proyecto, y conviene leerlo antes que
cualquier cifra.

El universo son **139 egresados únicos**. De ellos, **35 tienen empleo
verificable en fuentes públicas** (perfiles de LinkedIn). La nómina de graduados
proviene de la página web oficial de la UPT. Eso da una **cobertura de información del
25.2 %**.

> **La cobertura no es la tasa de empleabilidad.** Los 104 egresados restantes
> no son desempleados: son casos sin información. La empleabilidad real no es
> estimable a partir de fuentes públicas, y el tablero no la reporta.

Tratar la cobertura como empleabilidad invalidaría el estudio completo. Por eso
el indicador se nombra explícitamente y la advertencia viaja en el propio
tablero, no solo en el informe.

Como contrapartida, la cobertura es un indicador útil por sí mismo: mide qué tan
bien la Escuela conoce a sus egresados. Un 75 % de invisibilidad es un hallazgo
accionable para el proceso de seguimiento y para la acreditación.

---

## Arranque rápido

```bash
pip install -r requirements.txt
make pipeline          # reconstruye todo, de punta a punta
```

Abrir `dashboard/index.html` en cualquier navegador. No requiere servidor.

Sin `make` (Windows):

```powershell
$env:PYTHONPATH="src"; python -m empleabilidad.pipeline
```

---

## Arquitectura

```
data/raw/           nómina nominal          ← NO versionada (datos personales)
    │
    ├─ ingest.py    contrato + seudonimización
    ▼
data/seed/          semilla seudonimizada   ← versionable
    │
    ├─ modelo.py    modelo estrella (DuckDB)
    ▼
data/marts/         data mart dimensional
    │
    ├─ kpis.py      indicadores + supresión
    ▼
dashboard/          tablero estático, sin dependencias
```

### Decisiones

| Decisión | Motivo |
|---|---|
| **DuckDB**, no PostgreSQL | 139 filas y cargas semestrales. Un motor cliente-servidor aporta complejidad operativa sin beneficio. El almacén es un archivo: se versiona, se copia, sobrevive al egreso del equipo. |
| **Tablero estático** | Sin build, sin servidor, sin licencias. Publicable en GitHub Pages o en cualquier hosting estático, sin costo ni mantenimiento. |
| **Datos embebidos** en el HTML | Funciona desde `file://`, en Pages y en cualquier hosting estático. |
| **Clasificación curada** | Con 35 registros, una tabla explícita y auditable es preferible a una heurística. Cada decisión es revisable en un diff. |

Ver `docs/adr/` para el registro completo.

### Modelo dimensional

Grano de la tabla de hechos: **una observación de la situación laboral de un
egresado, en una fecha, proveniente de una fuente determinada.**

Modelar la fuente es deliberado: un perfil verificado directamente y una entrada
de directorio no son evidencia del mismo peso, y el tablero debe poder
distinguirlas.

```
fact_observacion_laboral
  ├─ tiene_evidencia_empleo   0/1
  ├─ es_afin                  0/1/NULL   ← tri-estado, ver abajo
  ├─ meses_insercion          NULL       ← requiere encuesta
  └─ FK → dim_egresado, dim_empleador, dim_area, dim_fuente, dim_tiempo
```

---

## Tres decisiones que sostienen la honestidad del análisis

**1. La afinidad formativa es tri-estado.** Cuando la fuente declara empresa
pero no cargo, no se puede saber si la persona trabaja en un área afín. Ese caso
se registra como `NULL` (desconocido), nunca como `0`. Forzarlo a falso
subestimaría la afinidad; forzarlo a verdadero la inflaría. El indicador se
reporta sobre su denominador real: los casos con cargo identificable.

**2. Un titular de LinkedIn no es evidencia de empleo.** Entradas como
"Bachiller en Ingeniería de Sistemas" o "Egresado UPT" describen la formación,
no un puesto. Contarlas como empleo es lo que eleva artificialmente la cifra.
Hay un test que protege esta distinción.

**3. Celdas pequeñas.** Los cortes por sector y área con menos de 5 casos se
marcan como suprimidos, y el tablero advierte que los cruces de filtros con
pocos casos deben leerse con cautela. Con cohortes de ~20 personas, combinar
año, sector y ubicación puede aislar a un individuo: agregar no es anonimizar.

> **Pendiente.** El tablero todavía embebe los registros individuales
> seudonimizados y no oculta los cortes pequeños. Ver la sección de riesgos del
> FD04.

---

## Privacidad

La nómina contiene nombres reales de 141 personas. El repositorio es público.

- `data/raw/` está en `.gitignore` **desde el primer commit**.
- La única etapa que ve nombres es la ingesta; a partir de ahí todo opera sobre
  identificadores seudónimos.
- La seudonimización usa **SHA-256 con sal**. La sal vive en `.env`, fuera del
  repositorio. Sin sal, el hash se rompe por fuerza bruta contra el universo
  conocido de egresados.
- El seudónimo es **determinista**: la misma persona produce el mismo
  identificador entre oleadas de encuesta, lo que permite seguir trayectorias
  sin re-identificar.

Marco: Ley N.° 29733, Ley de Protección de Datos Personales.

---

## Estado de los indicadores

| Indicador | Estado | Fuente |
|---|---|---|
| Cobertura de información | ✅ | Nómina oficial + LinkedIn |
| Egresados por promoción | ✅ | Nómina oficial |
| Sector del empleador | ✅ | Clasificación curada |
| Área de desempeño | ✅ | Solo casos con cargo declarado |
| Concentración de empleadores | ✅ | Clasificación curada |
| **Tiempo de inserción laboral** | ❌ | **Requiere encuesta** |
| Tasa de empleabilidad real | ❌ | **Requiere encuesta** |

Los dos últimos no son limitaciones de la implementación: las fuentes públicas
no exponen fecha de inicio laboral ni permiten distinguir desempleo de ausencia
de información. El modelo ya reserva las columnas para no rehacerse después.

---

## Comandos

```bash
make pipeline     # ingesta → modelo → KPIs → tablero
make test         # suite de tests
make limpiar      # borra artefactos generados
```

---

## Estructura

```
data/raw/        nómina nominal (no versionada)
data/seed/       semilla seudonimizada
data/marts/      almacén DuckDB (generado)
src/empleabilidad/
  clasificacion.py   reglas curadas de empleador, cargo, sector y área
  ingest.py          contrato de datos y seudonimización
  modelo.py          construcción del modelo estrella
  kpis.py            indicadores y supresión
  tablero.py         render del HTML
sql/             modelo dimensional
tests/           suite de tests
docs/adr/        registro de decisiones de arquitectura
dashboard/       tablero publicable
```

---

## Documentación del proyecto

Los informes formales están en la rama [`Documentos`](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/tree/Documentos):

| Documento | Versión |
|---|---|
| [FD01 – Informe de Factibilidad](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/blob/Documentos/FD01-Informe-Factibilidad.md) | 1.1 |
| [FD02 – Documento de Visión](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/blob/Documentos/FD02-Informe-Vision.md) | 1.1 |
| [FD03 – Especificación de Requerimientos](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/blob/Documentos/FD03-Informe-Especificacion-Requerimientos.md) | 1.0 |
| [FD04 – Arquitectura de Software](https://github.com/UPT-FAING-EPIS/proyecto-si885-2026-i-dataimpact/blob/Documentos/FD04-Informe-Arquitectura-Software.md) | 1.0 |
