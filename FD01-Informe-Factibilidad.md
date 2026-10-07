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

**Sistema *Dashboard de Empleabilidad de Egresados EPIS-UPT***

**Informe de Factibilidad**

**Versión *1.1***

| CONTROL DE VERSIONES | | | | | |
| :-: | :- | :- | :- | :- | :- |
| **Versión** | **Hecha por** | **Revisada por** | **Aprobada por** | **Fecha** | **Motivo** |
| 1.0 | AJV | P. Cuadros Q. | P. Cuadros Q. | 22/08/2026 | Versión original completa |
| 1.1 | Equipo del proyecto | | | 06/10/2026 | Alineación con la solución implementada: DuckDB y tablero web estático en lugar de PostgreSQL y Power BI; indicador de cobertura de información; recálculo de costos y del análisis financiero |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# ÍNDICE GENERAL

1. [Descripción del Proyecto](#_Toc1)
2. [Riesgos](#_Toc2)
3. [Análisis de la Situación actual](#_Toc3)
4. [Estudio de Factibilidad](#_Toc4)
   - 4.1 [Factibilidad Técnica](#_Toc41)
   - 4.2 [Factibilidad Económica](#_Toc42)
   - 4.3 [Factibilidad Operativa](#_Toc43)
   - 4.4 [Factibilidad Legal](#_Toc44)
   - 4.5 [Factibilidad Social](#_Toc45)
   - 4.6 [Factibilidad Ambiental](#_Toc46)
5. [Análisis Financiero](#_Toc5)
6. [Conclusiones](#_Toc6)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Informe de Factibilidad

<a id="_Toc1"></a>

## 1. Descripción del Proyecto

### 1.1 Nombre del proyecto

*Dashboard de empleabilidad de los egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna*.

### 1.2 Duración del proyecto

La duración estimada del proyecto es de 16 semanas, equivalentes a cuatro meses. Este periodo comprende el levantamiento de requerimientos, la recopilación y depuración de datos, el desarrollo del dashboard, las pruebas, el despliegue y la capacitación de los usuarios clave de la Escuela Profesional.

### 1.3 Descripción

La empleabilidad de los egresados constituye un indicador fundamental para evaluar la pertinencia de la formación universitaria y su alineación con las demandas del mercado laboral tecnológico. La Universidad Privada de Tacna (UPT), mediante el programa GPS Alumni y las iniciativas de la Escuela Profesional de Ingeniería de Sistemas (EPIS), realiza el seguimiento de sus egresados para conocer sus trayectorias profesionales.

Actualmente, la información sobre la situación laboral de los egresados se encuentra dispersa y es incompleta: no existe un repositorio integrado y, para la mayoría de los egresados, la Escuela no dispone de ningún dato laboral.

El proyecto desarrolla un dashboard de Inteligencia de Negocios para el seguimiento de los egresados de Ingeniería de Sistemas de las promociones **2017 a 2024**. El universo de estudio es la nómina de graduados obtenida de la página web oficial de la UPT, con **139 egresados únicos**. Sobre ese universo se integra la evidencia laboral disponible en los perfiles públicos de LinkedIn, se clasifica de forma auditable y se carga en un data mart dimensional. El tablero resultante muestra indicadores por promoción, sector del empleador, área de desempeño, ubicación y confiabilidad de la evidencia.

Un principio metodológico guía todo el proyecto: **la cobertura de información no es la tasa de empleabilidad**. De los 139 egresados, 35 tienen empleo verificable en fuentes públicas, lo que representa una cobertura del 25.2 %. Los 104 restantes no son desempleados, sino casos sin información. Por ello, el sistema reporta la cobertura de información y declara la tasa de empleabilidad como no estimable con las fuentes disponibles. Su cálculo, junto con el tiempo de inserción laboral y el rango salarial, queda condicionado a la aplicación de una encuesta directa a los egresados.

Esta herramienta facilitará la toma de decisiones relacionadas con el seguimiento de egresados, la actualización curricular y los procesos de acreditación de la carrera.

### 1.4 Objetivos

#### 1.4.1 Objetivo general

Desarrollar un dashboard de Inteligencia de Negocios que permita analizar y realizar el seguimiento de la empleabilidad de los egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna, mediante indicadores que distingan la información conocida de la desconocida y apoyen la toma de decisiones académicas.

#### 1.4.2 Objetivos específicos

- Construir el marco censal de egresados de las promociones 2017 a 2024 a partir de la nómina de graduados publicada en la página web oficial de la UPT, protegiendo su identidad mediante seudonimización.
- Integrar y clasificar la evidencia laboral disponible en los perfiles públicos de LinkedIn: empleador, cargo, sector, área de desempeño, ubicación y nivel de confiabilidad de la fuente.
- Diseñar un modelo dimensional (data mart) que registre cada observación laboral junto con su fuente, de modo que puedan distinguirse evidencias de distinto peso.
- Definir indicadores clave (KPIs) con denominadores explícitos: cobertura de información, cobertura por promoción, distribución por sector y área, afinidad formativa y concentración de empleadores.
- Implementar un dashboard web interactivo con filtros por promoción y sector, que pueda consultarse desde cualquier navegador sin instalación ni licencias.
- Identificar las brechas de información sobre los egresados y proponer la encuesta directa necesaria para medir la empleabilidad real y el tiempo de inserción laboral.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc2"></a>

## 2. Riesgos

A continuación, se presentan los principales riesgos que podrían afectar el desarrollo, la implementación y la continuidad del proyecto, junto con su estado a la fecha de esta versión.

| N.º | Riesgo | Tipo | Probabilidad | Impacto | Estrategia de mitigación | Estado |
| ---: | --- | --- | :---: | :---: | --- | --- |
| 1 | Información incompleta, dispersa o inconsistente sobre los egresados | Técnico | Alta | Alto | Contrato de datos en la ingesta que rechaza nombres vacíos, fechas inválidas o fuera de rango y registros duplicados; clasificación curada y auditable de empleadores y cargos. | Mitigado |
| 2 | Las fuentes públicas no permiten distinguir a un egresado desempleado de uno sin información | Metodológico | Alta | Alto | Reportar cobertura de información en lugar de tasa de empleabilidad y mostrar la advertencia dentro del propio tablero. | Materializado y mitigado |
| 3 | Cambios o retiro de la información publicada en las fuentes (página web de la UPT y perfiles de LinkedIn) | Operativo | Media | Alto | Conservar una copia seudonimizada de cada extracción, registrar la fecha y la fuente de cada observación y solicitar a la Escuela la nómina oficial como respaldo. | Pendiente |
| 4 | Baja participación de los egresados en una futura encuesta | Operativo | Alta | Alto | Utilizar diferentes canales (correo institucional, LinkedIn, grupos de egresados) y diseñar encuestas breves y adaptadas a dispositivos móviles. | Pendiente |
| 5 | Reidentificación de egresados en cruces de filtros con pocos casos | Legal | Media | Alto | Seudonimización con SHA-256 y sal secreta; marcado de los cortes con menos de 5 casos y advertencia de lectura en el tablero; ningún nombre ni DNI en el tablero. Pendiente: evaluar si el tablero público debe incluir registros individuales seudonimizados. | Parcialmente mitigado |
| 6 | Filtración de la nómina con datos personales | Legal y tecnológico | Media | Alto | La nómina nominal no se versiona (`data/raw/` excluido del repositorio) y la integración continua verifica en cada cambio que no se haya subido. | Mitigado |
| 7 | Falta de licencias o infraestructura para publicar el dashboard | Técnico y económico | Media | Alto | Uso de un tablero web estático, publicable en GitHub Pages o en cualquier hosting institucional, sin licencias ni servidor. | Eliminado |
| 8 | Baja utilización del dashboard por parte de los usuarios institucionales | Operativo | Media | Medio | Involucrar a los usuarios en la definición de los indicadores, incluir una nota metodológica en el tablero y brindar capacitación sobre su interpretación. | Pendiente |
| 9 | Desactualización de la información después de finalizar el proyecto | Operativo | Alta | Alto | Pipeline reproducible de un solo comando, documentación de decisiones de arquitectura y designación de un responsable de la actualización semestral. | Parcialmente mitigado |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc3"></a>

## 3. Análisis de la Situación actual

### 3.1 Planteamiento del problema

Actualmente, el seguimiento de la empleabilidad de los egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna se realiza de manera manual y desarticulada. Aunque existen iniciativas como GPS Alumni y encuestas aplicadas por las áreas académicas, la información no está integrada en un repositorio centralizado para su análisis.

El diagnóstico realizado en el proyecto cuantificó el problema: de los 139 egresados de las promociones 2017 a 2024, solo 35 (25.2 %) tienen una situación laboral verificable en fuentes públicas. Para el 74.8 % restante, la Escuela no dispone de información laboral.

Como consecuencia, la Escuela Profesional no puede responder con rapidez a preguntas estratégicas como las siguientes:

- ¿Qué porcentaje de egresados se encuentra trabajando?
- ¿Qué porcentaje trabaja en un área relacionada con Ingeniería de Sistemas?
- ¿Cuál es el tiempo promedio de inserción laboral después del egreso?
- ¿En qué sectores y áreas profesionales se desempeñan los egresados?
- ¿Los egresados permanecen en Tacna o migran a otras ciudades?
- ¿Cómo ha evolucionado el conocimiento sobre los egresados según el año de egreso?

Algunas de estas preguntas pueden responderse con la información disponible (sectores, áreas, ubicación y cobertura por promoción); otras, como la tasa de empleo real y el tiempo de inserción, requieren una encuesta directa. La falta de información integrada dificulta la actualización del plan de estudios y la presentación de evidencias durante los procesos de acreditación. Por ello, se propone desarrollar un dashboard de Inteligencia de Negocios que centralice, procese y visualice la información disponible y haga explícitas sus brechas.

### 3.2 Consideraciones de hardware y software

#### 3.2.1 Hardware requerido

| Recurso | Especificaciones recomendadas | Finalidad |
| --- | --- | --- |
| Equipo de desarrollo | Procesador Intel Core i5 o AMD Ryzen 5, 8 GB de RAM y almacenamiento SSD | Desarrollo del proceso ETL, modelado de datos y elaboración del dashboard |
| Conexión a Internet | Conexión estable de banda ancha | Control de versiones, integración continua y publicación del dashboard |
| Equipos de los usuarios | Computadora, tableta o teléfono con navegador web actualizado | Acceso y consulta del dashboard |

No se requiere un servidor de base de datos ni un servidor de aplicaciones. El almacén analítico es un archivo DuckDB y el dashboard es una página web estática que funciona incluso abierta directamente desde el disco.

#### 3.2.2 Software seleccionado

| Componente | Tecnología seleccionada | Finalidad |
| --- | --- | --- |
| Base de datos analítica | DuckDB (embebida, en un archivo) | Almacenar el data mart dimensional y calcular los indicadores |
| Procesamiento y ETL | Python 3.12 | Ingesta, validación, seudonimización, clasificación y carga de los datos |
| Visualización | HTML, CSS y JavaScript sin dependencias externas | Tablero interactivo con indicadores, gráficos, tablas y filtros |
| Publicación | GitHub Pages o hosting institucional estático | Publicar el dashboard sin servidor ni licencias |
| Pruebas | pytest | Pruebas automatizadas del contrato de datos y de las reglas de clasificación |
| Integración continua | GitHub Actions | Ejecutar las pruebas, verificar que no se suban datos personales y reconstruir el tablero en cada cambio |
| Control de versiones | Git y GitHub | Gestionar los cambios realizados en los archivos del proyecto |

Todas las tecnologías seleccionadas son de código abierto o gratuitas. En la versión 1.0 de este informe se había propuesto PostgreSQL y Power BI; el cambio se justifica en la sección 4.1.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc4"></a>

## 4. Estudio de Factibilidad

El estudio de factibilidad evalúa la viabilidad del proyecto en las dimensiones técnica, económica, operativa, legal, social y ambiental. El propósito es determinar si el sistema puede desarrollarse e implementarse con los recursos disponibles y bajo las condiciones establecidas por la Escuela Profesional de Ingeniería de Sistemas.

<a id="_Toc41"></a>

### 4.1 Factibilidad Técnica

El proyecto requiere equipos de cómputo para el desarrollo, un almacén analítico, herramientas para el procesamiento de la información y un medio para publicar el dashboard. Todos estos requerimientos se atienden con tecnologías de código abierto que no requieren equipos especializados.

**Arquitectura de la solución.** El proceso se ejecuta con un solo comando y consta de cuatro etapas:

1. **Ingesta:** lee la nómina de graduados, valida el contrato de datos y reemplaza la identidad de cada egresado por un seudónimo. Es la única etapa que procesa nombres.
2. **Modelo:** construye un modelo estrella en DuckDB cuya tabla de hechos registra una observación de la situación laboral de un egresado, en una fecha y según una fuente, junto con las dimensiones de egresado, empleador, área, fuente y tiempo.
3. **Indicadores:** calcula los KPIs con denominadores explícitos y marca como suprimidos los cortes por sector y área con menos de 5 casos.
4. **Tablero:** genera una página HTML autocontenida con los datos embebidos.

**Decisiones tecnológicas.** Respecto de la propuesta inicial, se adoptaron las siguientes decisiones:

| Propuesta inicial | Solución adoptada | Justificación |
| --- | --- | --- |
| PostgreSQL | DuckDB | El universo es de 139 registros con cargas semestrales y consultas exclusivamente analíticas. Un motor cliente-servidor exige un servidor encendido, credenciales, copias de seguridad y un responsable de mantenimiento, sin aportar beneficio a esta escala. DuckDB es columnar, está orientado a agregaciones y el almacén es un único archivo. |
| Power BI Desktop y Power BI Service | Tablero web estático | No requiere licencias, servidor ni proceso de compilación. Funciona en cualquier navegador y puede publicarse indefinidamente sin costo. |
| Pandas y SQLAlchemy | Python con DuckDB | DuckDB lee archivos CSV y ejecuta SQL directamente, por lo que no se necesitan librerías adicionales. |

Si la Universidad exigiera PostgreSQL en el futuro, el SQL del modelo es estándar y la migración consistiría en cambiar el conector, no el modelo.

**Calidad y seguridad.** El proyecto incluye pruebas automatizadas que validan el contrato de datos, el carácter determinista de los seudónimos y las reglas de clasificación (por ejemplo, que un titular profesional como "Bachiller en Ingeniería de Sistemas" no se cuente como empleo). La integración continua ejecuta estas pruebas y verifica que la nómina nominal no se haya subido al repositorio.

Por lo tanto, el proyecto se considera **técnicamente factible**: la solución está implementada, es reproducible y no depende de infraestructura ni licencias externas.

<a id="_Toc42"></a>

### 4.2 Factibilidad Económica

La factibilidad económica analiza los recursos monetarios necesarios para desarrollar e implementar el proyecto. Para ello, se consideran los costos generales, operativos, tecnológicos y de personal correspondientes a las 16 semanas de ejecución.

Los montos presentados son estimaciones referenciales y deberán validarse antes de aprobar el presupuesto definitivo.

#### 4.2.1 Costos generales

Gastos en material de oficina, suministros de escritorio y depreciación de equipos existentes:

| Concepto | Cantidad | Costo unitario (S/) | Costo total (S/) |
| --- | ---: | ---: | ---: |
| Material de escritorio y papelería | 1 lote | 150.00 | 150.00 |
| Servicios de impresión y empastado | 1 lote | 100.00 | 100.00 |
| Depreciación de equipos de cómputo por cuatro meses | 3 unidades | 300.00 | 900.00 |
| **Total de costos generales** | | | **1,150.00** |

El costo de depreciación de los equipos deberá validarse considerando su valor de adquisición, vida útil estimada y tiempo de uso durante el proyecto.

#### 4.2.2 Costos operativos durante el desarrollo

Los costos operativos corresponden al consumo proporcional de los servicios y recursos utilizados durante las 16 semanas de desarrollo del proyecto.

| Servicio o recurso | Meses | Costo mensual estimado (S/) | Costo total (S/) |
| --- | ---: | ---: | ---: |
| Consumo proporcional de energía eléctrica | 4 | 120.00 | 480.00 |
| Uso proporcional de la conexión a Internet | 4 | 150.00 | 600.00 |
| Uso del espacio físico de trabajo | 4 | 200.00 | 800.00 |
| **Total de costos operativos** | | | **1,880.00** |

Si la Universidad Privada de Tacna proporciona la conexión a Internet y el espacio físico sin generar pagos adicionales, estos conceptos deberán registrarse como costos indirectos o recursos institucionales disponibles.

#### 4.2.3 Costos del ambiente

Los costos del ambiente tecnológico comprenden las herramientas de software, el licenciamiento y los servicios necesarios para desarrollar, publicar y consultar el dashboard.

| Componente | Tipo de licencia o disponibilidad | Cantidad | Costo estimado (S/) |
| --- | --- | ---: | ---: |
| DuckDB | Código abierto (MIT) | 1 | 0.00 |
| Python y pytest | Código abierto | 1 | 0.00 |
| Tablero web (HTML, CSS y JavaScript) | Desarrollo propio | 1 | 0.00 |
| GitHub, GitHub Actions y GitHub Pages | Gratuito para repositorios públicos | 1 | 0.00 |
| **Total de costos del ambiente tecnológico** | | | **0.00** |

Al reemplazar Power BI Service por un tablero web estático, se elimina el costo de licencias de S/240.00 previsto en la versión 1.0 y el costo recurrente por cada usuario adicional.

#### 4.2.4 Costos de personal

Los costos de personal se estiman de acuerdo con las funciones, las horas de participación y la tarifa asignada a cada rol durante las 16 semanas del proyecto.

| Rol | Horas totales | Promedio de horas semanales | Tarifa por hora (S/) | Costo total (S/) |
| --- | ---: | ---: | ---: | ---: |
| Jefe de proyecto y arquitecto BI | 80 | 5.00 | 35.00 | 2,800.00 |
| Ingeniero de datos y responsable del proceso ETL | 120 | 7.50 | 25.00 | 3,000.00 |
| Desarrollador BI y dashboard | 120 | 7.50 | 25.00 | 3,000.00 |
| Analista de calidad y pruebas | 60 | 3.75 | 20.00 | 1,200.00 |
| **Total de costos de personal** | **380** | | | **10,000.00** |

Aunque el desarrollo sea realizado por estudiantes y no genere un pago directo, estos montos representan el valor económico estimado del trabajo realizado.

#### 4.2.5 Costos totales del desarrollo del sistema

| Categoría de costo | Monto (S/) | Porcentaje |
| --- | ---: | ---: |
| Costos generales | 1,150.00 | 8.83 % |
| Costos operativos | 1,880.00 | 14.43 % |
| Costos del ambiente tecnológico | 0.00 | 0.00 % |
| Costos de personal | 10,000.00 | 76.75 % |
| **Costo total estimado del proyecto** | **13,030.00** | **100.00 %** |

*Nota: los porcentajes están redondeados a dos decimales, por lo que su suma puede diferir en 0.01 % del total.*

El costo total estimado para desarrollar e implementar el sistema durante las 16 semanas es de **S/13,030.00**. El mayor componente corresponde al trabajo del equipo del proyecto, que representa el 76.75 % del presupuesto total.

#### 4.2.6 Financiamiento propuesto

Se propone que el proyecto sea financiado mediante recursos institucionales de la Escuela Profesional de Ingeniería de Sistemas o fondos internos destinados al desarrollo de proyectos, sujeto a la aprobación de las autoridades correspondientes.

En caso de aprobarse el financiamiento, el presupuesto podría distribuirse de acuerdo con los principales entregables del proyecto:

- 30 % después de la aprobación del estudio de factibilidad.
- 40 % después de completar la integración, limpieza y procesamiento de los datos.
- 30 % después del despliegue y aceptación del dashboard.

Por lo tanto, el proyecto se considera **económicamente factible**: la inversión es moderada, no requiere gastos en licencias ni infraestructura y su costo de operación posterior es mínimo.

<a id="_Toc43"></a>

### 4.3 Factibilidad Operativa

El proyecto responde a la necesidad de disponer de información integrada sobre los egresados. El dashboard reduce el tiempo necesario para consultar y elaborar reportes institucionales, y además mide por primera vez cuánto conoce la Escuela sobre sus egresados.

#### Beneficios operativos

- Centralización de la información disponible de los egresados en un único data mart.
- Actualización mediante un pipeline reproducible que se ejecuta con un solo comando.
- Consulta de indicadores mediante filtros por promoción y sector, sin instalar software.
- Identificación de las promociones con menor información, para focalizar el seguimiento.
- Generación de evidencias para los procesos de acreditación.
- Continuidad del sistema después del egreso del equipo, al no depender de servidores ni licencias.

#### Principales interesados

| Interesado | Participación en el proyecto |
| --- | --- |
| Dirección de la EPIS | Utilizará el dashboard para la toma de decisiones y la planificación académica |
| Comité de Acreditación | Consultará los indicadores y reportes de empleabilidad |
| Programa GPS Alumni | Podrá aplicar, en coordinación con la Escuela, la futura encuesta a egresados |
| Equipo del proyecto | Desarrolla, prueba y documenta la solución |
| Egresados | Fuente de información, actualmente mediante sus perfiles públicos de LinkedIn y, en el futuro, mediante encuestas |
| Estudiantes | Serán beneficiados indirectamente mediante la mejora de la formación académica |

Para garantizar la continuidad del sistema, deberá designarse un responsable de actualizar la nómina y la evidencia laboral cada semestre y de volver a ejecutar el pipeline. La documentación del repositorio y el registro de decisiones de arquitectura facilitan esta transferencia.

Por lo tanto, el proyecto se considera **operativamente factible**, condicionado a la designación de un responsable de la actualización y a la capacitación de los usuarios en la interpretación de los indicadores.

<a id="_Toc44"></a>

### 4.4 Factibilidad Legal

El proyecto trata información de personas identificables (nombres, fechas de grado y datos laborales). Por esta razón, debe cumplir con la Ley N.º 29733, Ley de Protección de Datos Personales, y con su reglamento vigente, aprobado mediante el Decreto Supremo N.º 016-2024-JUS.

Medidas implementadas:

- **Minimización:** solo la etapa de ingesta procesa nombres; las etapas posteriores operan sobre seudónimos.
- **Seudonimización:** los identificadores se generan con SHA-256 y una sal secreta que se guarda fuera del repositorio. Sin la sal, no es posible reconstruir la identidad comparando con la lista de egresados.
- **Exclusión de datos personales del repositorio:** la nómina nominal (`data/raw/`) está excluida del control de versiones desde el primer commit, y la integración continua lo verifica en cada cambio.
- **Control de divulgación estadística:** los cortes por sector y área con menos de 5 casos se marcan como suprimidos, y el tablero advierte que los cruces de filtros con pocos casos deben leerse con cautela, porque con cohortes de alrededor de 20 personas un cruce podría aislar a un individuo.
- **Sin datos de contacto:** el tablero no contiene nombres, DNI, correos ni teléfonos.

Medidas pendientes antes de ampliar el alcance:

- Obtener la autorización institucional formal para el uso de la nómina de graduados.
- Solicitar el consentimiento informado de los egresados en la futura encuesta.
- Establecer un periodo de conservación y un procedimiento para atender los derechos de acceso, rectificación, cancelación y oposición.
- Verificar si el banco de datos debe registrarse ante la autoridad correspondiente.
- Evaluar si el tablero público debe seguir incluyendo registros individuales seudonimizados (promoción, empleador y área), que permiten recalcular los indicadores en el navegador pero podrían facilitar la reidentificación en promociones pequeñas, o si debe publicar solo agregados.

Por lo tanto, el proyecto se considera **legalmente factible**, siempre que se obtengan las autorizaciones institucionales indicadas.

<a id="_Toc45"></a>

### 4.5 Factibilidad Social

El proyecto presenta una contribución social favorable porque permite conocer con mayor precisión la situación laboral de los egresados de Ingeniería de Sistemas y, sobre todo, cuánto se desconoce de ella.

Los principales beneficios sociales del proyecto son los siguientes:

- Fortalecer el vínculo entre la universidad, los egresados y el mercado laboral.
- Proporcionar información que contribuya a mejorar la formación académica.
- Orientar a los estudiantes sobre los sectores y áreas en que se desempeñan los egresados.
- Evitar conclusiones erróneas sobre los egresados, al no presentar como desempleados a quienes simplemente no tienen información pública.
- Contribuir al seguimiento de los egresados y a la mejora continua de la carrera.

El dashboard presenta los resultados de manera agregada y sin comparaciones discriminatorias entre egresados. La participación en futuras encuestas deberá ser informada y voluntaria.

Por lo tanto, el proyecto se considera **socialmente factible**.

<a id="_Toc46"></a>

### 4.6 Factibilidad Ambiental

El proyecto presenta un impacto ambiental mínimo: utiliza equipos de cómputo existentes y no requiere servidores dedicados encendidos de forma permanente, ya que el dashboard es una página estática.

La distribución digital de la información reduce el uso de papel, tinta y materiales de impresión empleados en la elaboración de reportes.

Para promover el uso eficiente de los recursos, se consideran las siguientes medidas:

- Utilizar equipos e infraestructura tecnológica existentes.
- Evitar impresiones innecesarias de reportes.
- Apagar o suspender los equipos cuando no estén siendo utilizados.
- Gestionar correctamente los residuos electrónicos cuando los equipos sean retirados.

Por lo tanto, el proyecto se considera **ambientalmente factible**.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc5"></a>

## 5. Análisis Financiero

El análisis financiero evalúa la viabilidad económica del proyecto durante un horizonte de tres años. Para ello, se consideran la inversión inicial, los costos anuales de mantenimiento, los beneficios tangibles esperados y un costo de oportunidad del capital del 10 %.

Los valores utilizados son estimaciones preliminares y deberán validarse con información institucional antes de aprobar la inversión.

### 5.1 Justificación de la inversión

#### 5.1.1 Beneficios del proyecto

**Beneficios tangibles**

| Beneficio | Ahorro anual estimado (S/) |
| --- | ---: |
| Reducción del tiempo de elaboración de reportes de seguimiento de egresados, de 80 horas/año a 5 horas/año, en horas de personal administrativo y docente | 4,500.00 |
| Eliminación de impresiones y papelería física en reportes | 1,200.00 |
| Evitación de consultorías externas de evaluación de empleabilidad (S/8,000.00 cada dos años) | 4,000.00 |
| **Total de beneficios tangibles anuales estimados** | **9,700.00** |

**Beneficios intangibles**

- Medición, por primera vez, de la cobertura de información sobre los egresados, un indicador accionable para el seguimiento y la acreditación.
- Disponibilidad oportuna de información confiable para los procesos de reacreditación ICACIT.
- Base técnica lista para incorporar los resultados de una encuesta, ya que el modelo reserva las columnas de tiempo de inserción laboral.

#### 5.1.2 Criterios de inversión

Para el flujo financiero se considera una inversión inicial de **S/13,030.00**, un costo de mantenimiento anual de **S/1,500.00** (horas de actualización semestral de los datos) y beneficios tangibles de **S/9,700.00** anuales durante 3 años, con un costo de oportunidad del capital (COK) del **10 %**.

| Año | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| Inversión (S/) | -13,030.00 | | | |
| Beneficios (S/) | | 9,700.00 | 9,700.00 | 9,700.00 |
| Mantenimiento (S/) | | -1,500.00 | -1,500.00 | -1,500.00 |
| **Flujo neto (S/)** | **-13,030.00** | **8,200.00** | **8,200.00** | **8,200.00** |

##### 5.1.2.1 Relación Beneficio/Costo (B/C)

- Valor presente de los beneficios (VPB): S/24,122.46
- Valor presente de los costos (VPC): S/16,760.28
- **Relación B/C = 24,122.46 / 16,760.28 = 1.44**

*Criterio:* al ser B/C > 1 (1.44), por cada sol invertido se generan S/1.44 en beneficios, por lo que el proyecto **es financieramente aceptable**.

##### 5.1.2.2 Valor Actual Neto (VAN)

- **VAN = VPB − VPC = S/24,122.46 − S/16,760.28 = S/7,362.18**

*Criterio:* al ser el **VAN > 0** (S/7,362.18), el proyecto genera valor económico positivo para la institución y justifica la inversión.

##### 5.1.2.3 Tasa Interna de Retorno (TIR)

- **TIR calculada = 39.99 %**
- Costo de oportunidad del capital (COK) = 10.00 %

*Criterio:* al ser la **TIR (39.99 %) superior al COK (10.00 %)**, se concluye que el proyecto posee una alta rentabilidad y eficiencia financiera.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<a id="_Toc6"></a>

## 6. Conclusiones

- El proyecto **"Dashboard de empleabilidad de los egresados de Ingeniería de Sistemas de la UPT"** es **técnica, económica, operativa, legal, social y ambientalmente factible**.
- La factibilidad técnica se respalda en una solución implementada con Python, DuckDB y un tablero web estático, reproducible con un solo comando y verificada mediante pruebas automatizadas e integración continua.
- El reemplazo de PostgreSQL y Power BI elimina los costos de licencias e infraestructura y reduce la inversión a **S/13,030.00**.
- El análisis financiero demuestra la rentabilidad del proyecto con un **VAN de S/7,362.18**, una **TIR del 39.99 %** y una relación **Beneficio/Costo de 1.44**.
- El principal hallazgo es que la Escuela conoce la situación laboral de solo el **25.2 %** de sus egresados. La medición de la empleabilidad real y del tiempo de inserción laboral requiere aplicar una encuesta directa, que se recomienda como siguiente etapa del proyecto.
