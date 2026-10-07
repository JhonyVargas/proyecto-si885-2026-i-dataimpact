<center>

![Logo de la Universidad Privada de Tacna](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto *Dashboard de empleabilidad de los egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna***

Curso: *Inteligencia de Negocios*

Docente: *CUADROS QUIROGA, PATRICK JOSE*

Integrantes:

***Pacompía Ortiz Abel Fernando (2023076797)***

***Cruz Mamani Victor Williams (2022073903)***

***Vargas Luque Jhony (2022075754)***

**Tacna – Perú**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

| CONTROL DE VERSIONES | | | | | |
| :-: | :- | :- | :- | :- | :- |
| **Versión** | **Hecha por** | **Revisada por** | **Aprobada por** | **Fecha** | **Motivo** |
| 1.0 | AJV | P. Cuadros Q. | P. Cuadros Q. | 22/08/2026 | Versión inicial |
| 1.1 | Equipo del proyecto | | | 06/10/2026 | Alineación con la solución implementada: DuckDB y tablero web estático; indicador de cobertura de información; capacidades actuales y futuras |

<br>

**Sistema *Dashboard de Empleabilidad de Egresados EPIS-UPT***

**Documento de Visión**

**Versión *1.1***

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# ÍNDICE GENERAL

1. [Introducción](#_Toc1)
   - 1.1 [Propósito](#_Toc11)
   - 1.2 [Alcance](#_Toc12)
   - 1.3 [Definiciones, Siglas y Abreviaturas](#_Toc13)
   - 1.4 [Referencias](#_Toc14)
   - 1.5 [Visión General](#_Toc15)
2. [Posicionamiento](#_Toc2)
   - 2.1 [Oportunidad de negocio](#_Toc21)
   - 2.2 [Definición del problema](#_Toc22)
3. [Descripción de los interesados y usuarios](#_Toc3)
   - 3.1 [Resumen de los interesados](#_Toc31)
   - 3.2 [Resumen de los usuarios](#_Toc32)
   - 3.3 [Entorno de usuario](#_Toc33)
   - 3.4 [Perfiles de los interesados](#_Toc34)
   - 3.5 [Perfiles de los usuarios](#_Toc35)
   - 3.6 [Necesidades de los interesados y usuarios](#_Toc36)
4. [Vista General del Producto](#_Toc4)
   - 4.1 [Perspectiva del producto](#_Toc41)
   - 4.2 [Resumen de capacidades](#_Toc42)
   - 4.3 [Suposiciones y dependencias](#_Toc43)
   - 4.4 [Costos y precios](#_Toc44)
   - 4.5 [Licenciamiento e instalación](#_Toc45)
5. [Características del producto](#_Toc5)
6. [Restricciones](#_Toc6)
7. [Rangos de calidad](#_Toc7)
8. [Precedencia y Prioridad](#_Toc8)
9. [Otros requerimientos del producto](#_Toc9)

[CONCLUSIONES](#_TocConclusiones)

[RECOMENDACIONES](#_TocRecomendaciones)

[BIBLIOGRAFÍA](#_TocBibliografia)

[WEBGRAFÍA](#_TocWebgrafia)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Informe de Visión

<a id="_Toc1"></a>

## 1. Introducción

<a id="_Toc11"></a>

### 1.1 Propósito

El propósito del presente Documento de Visión es definir el alcance, los objetivos, los interesados, las necesidades, las características principales y las restricciones del sistema denominado *Dashboard de empleabilidad de egresados EPIS-UPT*.

Este documento proporciona una visión general de la solución y sirve como referencia para que el equipo del proyecto, la Dirección de la Escuela Profesional de Ingeniería de Sistemas, el Comité de Acreditación y los responsables de GPS Alumni comprendan la finalidad, las capacidades actuales y las limitaciones del sistema.

<a id="_Toc12"></a>

### 1.2 Alcance

El proyecto comprende el desarrollo de un dashboard de Inteligencia de Negocios para el seguimiento de la empleabilidad de los egresados de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna, promociones **2017 a 2024** (139 egresados únicos).

El alcance de la versión actual incluye:

- Construir el marco censal de egresados a partir de la nómina de graduados publicada en la página web oficial de la UPT.
- Validar los datos de entrada mediante un contrato de datos y seudonimizar la identidad de los egresados.
- Integrar y clasificar la evidencia laboral disponible en los perfiles públicos de LinkedIn: empleador, cargo, sector, área de desempeño, ubicación y nivel de confiabilidad.
- Almacenar la información en un data mart dimensional (modelo estrella) sobre DuckDB.
- Calcular indicadores con denominadores explícitos: cobertura de información, cobertura por promoción, estado de la evidencia, distribución por sector, área y ubicación, afinidad formativa y concentración de empleadores.
- Publicar un dashboard web estático e interactivo con filtros por promoción y sector.
- Automatizar las pruebas y la reconstrucción del tablero mediante integración continua.

#### Fuera del alcance de la versión actual (requiere encuesta directa)

Las fuentes públicas no permiten distinguir a un egresado desempleado de uno que no publica su situación laboral, ni exponen fechas de contratación o salarios. Por ello, los siguientes indicadores quedan condicionados a la aplicación de una encuesta a los egresados:

- Tasa de empleabilidad real.
- Tiempo de inserción laboral (el modelo ya reserva las columnas correspondientes).
- Rango salarial.
- Modalidad de trabajo (presencial, remoto o híbrido).
- Competencias tecnológicas, certificaciones y posgrados.

#### Exclusiones del alcance

El sistema no incluirá:

- La gestión de trámites de egreso, grados académicos o titulación.
- La administración de ofertas laborales o procesos de contratación.
- El funcionamiento como bolsa de trabajo.
- La modificación directa de la información del sistema académico institucional.
- El análisis predictivo de tendencias laborales.
- La publicación de datos personales identificables de los egresados.

<a id="_Toc13"></a>

### 1.3 Definiciones, Siglas y Abreviaturas

- **UPT**: Universidad Privada de Tacna.
- **EPIS**: Escuela Profesional de Ingeniería de Sistemas.
- **BI (Business Intelligence)**: Inteligencia de Negocios; conjunto de estrategias, aplicaciones y tecnologías enfocadas en crear conocimiento a través del análisis de datos.
- **ETL (Extract, Transform, Load)**: proceso de extracción, transformación y carga de datos desde fuentes origen hacia una base de datos analítica.
- **KPI (Key Performance Indicator)**: indicador clave de desempeño cuantificable.
- **Data mart**: almacén de datos orientado a un tema específico, organizado para el análisis.
- **Modelo estrella**: modelo dimensional compuesto por una tabla de hechos y tablas de dimensiones.
- **DuckDB**: motor de base de datos analítica, columnar y embebido en un único archivo.
- **Marco censal**: lista completa de los egresados que conforman el universo de estudio.
- **Cobertura de información**: porcentaje de egresados del marco censal cuya situación laboral es verificable en alguna fuente. **No equivale a la tasa de empleabilidad.**
- **Afinidad formativa**: correspondencia entre el cargo desempeñado y la formación en Ingeniería de Sistemas. Se registra como afín, no afín o desconocida.
- **Seudonimización**: reemplazo de la identidad de una persona por un identificador que no permite reconocerla sin información adicional (en este proyecto, una sal secreta).
- **Supresión de celdas pequeñas**: práctica de control de divulgación estadística que consiste en no publicar o marcar con advertencia el detalle de los grupos con menos de 5 casos.
- **GPS Alumni**: programa institucional de seguimiento a egresados de la Universidad Privada de Tacna.
- **ICACIT**: Instituto de Calidad y Acreditación de Carreras de Ingeniería y Tecnología.
- **Ley N.º 29733**: Ley de Protección de Datos Personales en el Perú.

<a id="_Toc14"></a>

### 1.4 Referencias

- FD01 – Informe de Factibilidad, versión 1.1.
- Registro de decisiones de arquitectura del proyecto (`docs/adr/`): ADR 001 (DuckDB en lugar de PostgreSQL), ADR 002 (cobertura de información en lugar de tasa de empleabilidad) y ADR 003 (afinidad formativa tri-estado).
- Estatuto Universitario y Reglamento de Seguimiento al Egresado de la Universidad Privada de Tacna.
- Estándares de Acreditación de Carreras Universitarias de Ingeniería de Sistemas (ICACIT / SINEACE).

<a id="_Toc15"></a>

### 1.5 Visión General

El presente Documento de Visión describe el propósito y alcance del sistema, el problema que se busca resolver, los interesados y usuarios involucrados, las necesidades identificadas y las principales características del producto.

Asimismo, presenta las capacidades del dashboard, las tecnologías empleadas, las restricciones del proyecto, los criterios de calidad, las prioridades de implementación y los requerimientos de seguridad y protección de datos. Debe utilizarse junto con el FD01 – Informe de Factibilidad.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc2"></a>

## 2. Posicionamiento

<a id="_Toc21"></a>

### 2.1 Oportunidad de negocio

La Escuela Profesional de Ingeniería de Sistemas requiere información integrada para conocer la situación laboral de sus egresados y evaluar la correspondencia entre la formación académica y las necesidades del mercado laboral.

El dashboard transforma la nómina de graduados de la página web de la UPT y la evidencia laboral de LinkedIn en indicadores consultables. Además de mostrar en qué sectores, áreas y ciudades trabajan los egresados con información disponible, mide por primera vez cuánto conoce la Escuela sobre sus egresados. Ese dato es accionable: permite focalizar el seguimiento en las promociones con menor información y justificar la aplicación de una encuesta directa.

Los resultados podrán apoyar la actualización del plan de estudios, el seguimiento de los egresados y la presentación de evidencias durante los procesos de acreditación.

<a id="_Toc22"></a>

### 2.2 Definición del problema

| Aspecto | Descripción |
| --- | --- |
| **Problema identificado** | La información sobre la situación laboral de los egresados está dispersa y es incompleta: solo el 25.2 % de los egresados de las promociones 2017 a 2024 tiene una situación laboral verificable. |
| **Personas y áreas afectadas** | La Dirección de la EPIS, el Comité de Acreditación, los responsables de GPS Alumni y, de manera indirecta, los estudiantes y egresados. |
| **Impacto del problema** | Dificultad para calcular indicadores de empleabilidad, riesgo de presentar cifras incorrectas (por ejemplo, confundir falta de información con desempleo) y demora en la elaboración de reportes para la acreditación. |
| **Causas principales** | Falta de una base de datos consolidada, ausencia de un proceso sistemático de encuesta a egresados y formatos de información no estandarizados. |
| **Solución propuesta** | Un dashboard de Inteligencia de Negocios que integra, clasifica y visualiza la información disponible con denominadores explícitos, y que hace visibles las brechas de información. |
| **Resultado esperado** | Información organizada y verificable sobre la situación laboral conocida de los egresados, y un diagnóstico cuantificado de lo que se desconoce. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc3"></a>

## 3. Descripción de los interesados y usuarios

<a id="_Toc31"></a>

### 3.1 Resumen de los interesados

| Nombre | Función / Rol | Representación |
| :--- | :--- | :--- |
| Director de la EPIS | Autoridad académica | Toma decisiones sobre actualización curricular y convenios institucionales. |
| Comité de Acreditación | Evaluadores de calidad | Requiere indicadores de seguimiento de egresados para los procesos de acreditación. |
| Coordinación GPS Alumni UPT | Responsable de egresados | Podría aplicar, en coordinación con la Escuela, la futura encuesta a egresados. |
| Egresados de la EPIS | Fuente de información | Su situación laboral se conoce a través de sus perfiles públicos de LinkedIn y, en el futuro, de encuestas. |

<a id="_Toc32"></a>

### 3.2 Resumen de los usuarios

| Usuario | Descripción | Rol en el sistema |
| :--- | :--- | :--- |
| **Administrador de datos** | Personal técnico o docente de la EPIS con acceso al repositorio. | Actualiza la nómina y la evidencia laboral, ejecuta el pipeline y publica el tablero. |
| **Analista académico / directivo** | Director de Escuela, miembros del Comité de Calidad. | Consulta el tablero y aplica filtros por promoción y sector. |
| **Docentes e investigadores** | Plana docente de la carrera. | Consulta de sectores y áreas de desempeño para investigación y cursos. |

<a id="_Toc33"></a>

### 3.3 Entorno de usuario

Los usuarios acceden al dashboard a través de cualquier navegador web moderno (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari), desde computadoras, tabletas o teléfonos. El tablero puede consultarse publicado en internet o abriendo directamente el archivo HTML, sin conexión a un servidor.

<a id="_Toc34"></a>

### 3.4 Perfiles de los interesados

**Perfil del Director de la EPIS**

- *Interés:* conocer dónde trabajan los egresados y si sus puestos son afines a la formación recibida.
- *Criterio de éxito:* indicadores claros, con la advertencia metodológica visible, que puedan presentarse sin riesgo de interpretación errónea.

**Perfil del Comité de Acreditación**

- *Interés:* obtener tablas cuantitativas por promoción.
- *Criterio de éxito:* exactitud de los datos, denominadores explícitos y capacidad de filtrar por años específicos.

<a id="_Toc35"></a>

### 3.5 Perfiles de los usuarios

**Perfil del analista / directivo (usuario final)**

- *Nivel técnico:* medio. Familiarizado con gráficos interactivos y filtros.
- *Frecuencia de uso:* mensual o trimestral (previo a sesiones de consejo de escuela y auditorías).
- *Comportamiento:* filtra por promoción y sector, y consulta las tablas de datos de cada gráfico.

<a id="_Toc36"></a>

### 3.6 Necesidades de los interesados y usuarios

| Necesidad | Inconveniente actual | Solución en el sistema |
| :--- | :--- | :--- |
| Conocer la situación laboral de los egresados. | Información dispersa e incompleta. | KPI de cobertura de información en la pantalla principal (25.2 %), acompañado de la advertencia de que no es tasa de empleo. La tasa real requiere encuesta. |
| Saber en qué promociones se conoce menos a los egresados. | No existe una medición de la información disponible. | Gráfico de cobertura de información por promoción. |
| Identificar sectores y áreas profesionales. | Desconocimiento del perfil desempeñado. | Gráficos de sector del empleador y área de desempeño, con advertencia de lectura para los grupos menores a 5 casos. |
| Conocer la afinidad entre formación y empleo. | No se distingue el cargo cuando la fuente solo declara la empresa. | Indicador de afinidad calculado solo sobre los casos con cargo identificable (11 de 12, 91.7 %). |
| Conocer la ubicación geográfica del empleo. | No se sabe si laboran en Tacna, Lima u otras ciudades. | Gráfico "¿Se quedan en Tacna?" con la distribución por ámbito. |
| Medir el tiempo transcurrido para conseguir empleo. | Las fuentes públicas no registran fechas de contratación. | No disponible en la versión actual: requiere encuesta. El modelo ya reserva el campo. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc4"></a>

## 4. Vista General del Producto

<a id="_Toc41"></a>

### 4.1 Perspectiva del producto

El *Dashboard de empleabilidad* es una solución analítica autónoma compuesta por un pipeline de datos y un tablero web estático:

```
Nómina de graduados de la web UPT + evidencia de LinkedIn (no versionada, datos personales)
   │  Ingesta: contrato de datos y seudonimización
   ▼
Semilla seudonimizada
   │  Modelo: esquema estrella en DuckDB
   ▼
Data mart dimensional
   │  Indicadores: cálculo y marcado de celdas pequeñas
   ▼
Dashboard HTML autocontenido
```

El pipeline completo se ejecuta con un solo comando. El tablero resultante no depende de servidores ni licencias y puede publicarse en GitHub Pages o en el portal institucional.

<a id="_Toc42"></a>

### 4.2 Resumen de capacidades

| Área funcional | Capacidad clave | Estado |
| :--- | :--- | :--- |
| **Cobertura del seguimiento** | Tarjetas con cobertura de información, número de egresados, egresados con evidencia laboral y porcentaje sin información. | Implementado |
| **Análisis por promoción** | Cobertura de información por año de egreso (2017 a 2024). | Implementado |
| **Estado de la evidencia** | Distribución entre empleo verificado, no confirmado, sin evidencia laboral y sin información. | Implementado |
| **Distribución geográfica** | Ámbito del empleo: Tacna, Lima y no determinado. | Implementado |
| **Perfil laboral** | Sector del empleador y área de desempeño. | Implementado |
| **Afinidad formativa** | Porcentaje de cargos afines sobre los casos con cargo identificable. | Implementado (nota metodológica) |
| **Concentración y calidad** | Empleadores con más de un egresado y confiabilidad de la evidencia (alta o media). | Implementado |
| **Empleabilidad real, tiempo de inserción y salario** | Indicadores basados en encuesta. | Futuro (requiere encuesta) |
| **Exportación de reportes** | Exportación a PDF o Excel. | Futuro |

<a id="_Toc43"></a>

### 4.3 Suposiciones y dependencias

- La nómina de graduados seguirá publicada en la página web oficial de la UPT, o la Escuela la proporcionará cada semestre.
- La evidencia laboral se obtiene de los perfiles públicos de LinkedIn, cuya disponibilidad depende de lo que publiquen los propios egresados.
- La medición de la empleabilidad real depende de la aplicación de una encuesta institucional.
- La publicación en internet depende de GitHub Pages o de un hosting estático institucional.

<a id="_Toc44"></a>

### 4.4 Costos y precios

El sistema es de uso institucional de la Universidad Privada de Tacna y no tendrá un precio de venta comercial.

De acuerdo con el FD01 – Informe de Factibilidad (versión 1.1), el costo total estimado del proyecto es de **S/13,030.00**, distribuido de la siguiente manera:

| Categoría de costo | Monto (S/) | Porcentaje |
| --- | ---: | ---: |
| Costos generales | 1,150.00 | 8.83 % |
| Costos operativos | 1,880.00 | 14.43 % |
| Costos del ambiente tecnológico | 0.00 | 0.00 % |
| Costos de personal | 10,000.00 | 76.75 % |
| **Costo total estimado del proyecto** | **13,030.00** | **100.00 %** |

*Nota: los porcentajes están redondeados a dos decimales, por lo que su suma puede diferir en 0.01 % del total.*

El costo del ambiente tecnológico es nulo porque todas las herramientas son de código abierto o gratuitas y el tablero no requiere licencias de visualización.

<a id="_Toc45"></a>

### 4.5 Licenciamiento e instalación

- **Licencias:** Python, DuckDB y pytest son de código abierto; GitHub, GitHub Actions y GitHub Pages son gratuitos para repositorios públicos.
- **Instalación para administradores:** instalar las dependencias (`pip install -r requirements.txt`) y ejecutar el pipeline (`make pipeline`).
- **Uso para consultores:** abrir `dashboard/index.html` en un navegador o acceder a la URL publicada. No requiere instalación.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc5"></a>

## 5. Características del producto

- **Filtros dinámicos:** segmentación por promoción (año de egreso) y por sector del empleador. Los filtros pueden activarse desde los botones o haciendo clic en las barras de los gráficos, y todos los indicadores se recalculan con la selección.
- **Tarjetas de KPIs:** cobertura de información, egresados en la selección, egresados con evidencia laboral y porcentaje sin información.
- **Gráficos de perfil laboral:** sector del empleador y área de desempeño (Desarrollo de Software, Infraestructura y Soporte, Datos / BI / IA, Docencia).
- **Distribución geográfica:** gráfico que muestra cuántos egresados con evidencia trabajan en Tacna, en Lima o en un lugar no determinado.
- **Calidad de la evidencia:** confiabilidad de cada fuente y empleadores con más de un egresado.
- **Tablas accesibles:** cada gráfico ofrece una vista de tabla con los datos exactos.
- **Nota metodológica integrada:** la advertencia de que la cobertura no es tasa de empleabilidad y la explicación de la afinidad viajan dentro del propio tablero.
- **Tema claro y oscuro**, diseño adaptable a teléfonos y navegación con teclado.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc6"></a>

## 6. Restricciones

- **Seguridad y privacidad:** el tablero no contiene nombres, DNI ni correos de los egresados. La nómina nominal no se versiona y los identificadores se seudonimizan con una sal secreta. Los cortes con menos de 5 casos se marcan y el tablero advierte que deben leerse con cautela.
- **Validez metodológica:** la cobertura de información no puede presentarse como tasa de empleabilidad. La afinidad se calcula solo sobre los casos con cargo identificable.
- **Fuentes de datos:** la versión actual se limita a la evidencia disponible en fuentes públicas, por lo que no incluye fechas de contratación, salarios ni modalidad de trabajo.
- **Frecuencia de actualización:** el data mart se actualiza de forma semestral o anual, ejecutando nuevamente el pipeline.
- **Compatibilidad:** el dashboard funciona en navegadores web estándar sin complementos, servidor ni conexión a internet.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc7"></a>

## 7. Rangos de calidad

- **Usabilidad:** cualquier indicador se obtiene con un máximo de 3 clics desde la pantalla principal.
- **Rendimiento:** el tablero es un único archivo de menos de 100 KB y recalcula los indicadores en el navegador; la interacción con los filtros debe responder en menos de **1 segundo**.
- **Disponibilidad:** al ser un sitio estático, la disponibilidad corresponde a la del servicio de hosting utilizado (GitHub Pages o el portal institucional). El archivo también puede consultarse sin conexión.
- **Confiabilidad:** el pipeline es reproducible: a partir de los mismos datos de entrada genera siempre los mismos indicadores. Las pruebas automatizadas validan el contrato de datos y las reglas de clasificación en cada cambio.
- **Trazabilidad:** cada decisión de clasificación de empleadores y cargos es revisable en el historial del repositorio.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc8"></a>

## 8. Precedencia y Prioridad

| Característica | Prioridad | Estado | Justificación |
| :--- | :--- | :--- | :--- |
| Ingesta, contrato de datos y seudonimización | **Alta** | Implementado | Fundamento indispensable y requisito legal. |
| Modelo dimensional y cálculo de KPIs | **Alta** | Implementado | Responde a la necesidad central del problema. |
| Tablero con cobertura, sector, área y afinidad | **Alta** | Implementado | Requerimiento clave para la toma de decisiones. |
| Distribución geográfica | **Media** | Implementado | Complementa el análisis con la dimensión regional. |
| Encuesta a egresados (empleabilidad real, tiempo de inserción, salario) | **Alta** | Pendiente | Único camino para medir la empleabilidad real. |
| Exportación de reportes en PDF/Excel | **Media** | Pendiente | Facilita la labor administrativa para auditorías ICACIT. |
| Análisis predictivo de tendencias | **Baja** | Fuera de alcance | Con 139 registros no hay volumen suficiente para modelos predictivos. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc9"></a>

## 9. Otros requerimientos del producto

**a) Estándares legales**

Cumplimiento de la Ley N.º 29733 (Ley de Protección de Datos Personales del Perú), de su reglamento (Decreto Supremo N.º 016-2024-JUS) y de las normativas sobre propiedad intelectual de la Universidad Privada de Tacna.

**b) Estándares de comunicación**

Publicación del tablero mediante HTTPS, provisto por GitHub Pages o por el hosting institucional.

**c) Estándares de cumplimiento de la plataforma**

Diseño adaptativo (responsive web design) que garantice una visualización adecuada desde pantallas de teléfono hasta monitores de escritorio.

**d) Estándares de calidad y seguridad**

- Pruebas automatizadas con pytest e integración continua con GitHub Actions.
- Verificación automática de que la nómina con datos personales no se suba al repositorio.
- El acceso de escritura a los datos y al tablero se controla mediante los permisos del repositorio en GitHub. El tablero publicado es de solo lectura y contiene únicamente información no identificable, por lo que no requiere autenticación de usuarios.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_TocConclusiones"></a>

## CONCLUSIONES

- El Documento de Visión establece el marco conceptual, el alcance y las especificaciones del *Dashboard de empleabilidad de los egresados de Ingeniería de Sistemas de la UPT*, alineados con la solución implementada.
- El principal hallazgo del sistema es que la Escuela conoce la situación laboral de solo el 25.2 % de sus egresados de las promociones 2017 a 2024. Este indicador de cobertura es en sí mismo accionable para el seguimiento y la acreditación.
- Entre los egresados con cargo identificable, el 91.7 % se desempeña en un área afín a la carrera, con predominio del sector de TI y consultoría y del área de Desarrollo de Software.
- La solución es sostenible: no requiere licencias, servidores ni mantenimiento de infraestructura, y su pipeline es reproducible y está documentado.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_TocRecomendaciones"></a>

## RECOMENDACIONES

- Diseñar y aplicar, en coordinación con GPS Alumni, una encuesta periódica a los egresados para medir la empleabilidad real, el tiempo de inserción laboral, el rango salarial y la modalidad de trabajo.
- Priorizar el seguimiento de las promociones con menor cobertura de información (2017 a 2019, con valores entre 15 % y 17 %).
- Designar un responsable de la actualización semestral de la nómina y de la evidencia laboral.
- Capacitar a las autoridades de la EPIS en la interpretación de los indicadores, en particular en la diferencia entre cobertura de información y tasa de empleabilidad.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_TocBibliografia"></a>

## BIBLIOGRAFÍA

- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). Wiley.
- Few, S. (2013). *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring* (2nd ed.). Analytics Press.
- Abran, A., & Moore, J. W. (2004). *SWEBOK: Guide to the Software Engineering Body of Knowledge*. IEEE Computer Society.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_TocWebgrafia"></a>

## WEBGRAFÍA

- Universidad Privada de Tacna: [https://www.upt.edu.pe](https://www.upt.edu.pe)
- Instituto de Calidad y Acreditación de Carreras de Ingeniería y Tecnología (ICACIT): [https://www.icacit.org.pe](https://www.icacit.org.pe)
- Documentación de DuckDB: [https://duckdb.org/docs/](https://duckdb.org/docs/)
- GitHub Pages: [https://docs.github.com/es/pages](https://docs.github.com/es/pages)
