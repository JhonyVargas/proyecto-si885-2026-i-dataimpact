<center>

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto *Dashboard de empleabilidad de los egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna***

Curso: *Inteligencia de Negocios*

Docente: *CUADROS QUIROGA, PATRICK JOSE*

Integrantes:

***Pacompía Ortiz Abel Fernando  (2023076797)***

**Tacna – Perú**

***2026***

</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1.0|AJV|P. Cuadros Q.|P. Cuadros Q.|22/08/2026|Versión inicial|

<br>

**Sistema *Dashboard de Empleabilidad de Egresados EPIS-UPT***

**Documento de Visión**

**Versión *1.0***

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **ÍNDICE GENERAL**

[1. Introducción](#_Toc52661346)

[1.1 Propósito](#_Toc11)

[1.2 Alcance](#_Toc12)

[1.3 Definiciones, Siglas y Abreviaturas](#_Toc13)

[1.4 Referencias](#_Toc14)

[1.5 Visión General](#_Toc15)

[2. Posicionamiento](#_Toc52661347)

[2.1 Oportunidad de negocio](#_Toc21)

[2.2 Definición del problema](#_Toc22)

[3. Descripción de los interesados y usuarios](#_Toc52661348)

[3.1 Resumen de los interesados](#_Toc31)

[3.2 Resumen de los usuarios](#_Toc32)

[3.3 Entorno de usuario](#_Toc33)

[3.4 Perfiles de los interesados](#_Toc34)

[3.5 Perfiles de los Usuarios](#_Toc35)

[3.6 Necesidades de los interesados y usuarios](#_Toc36)

[4. Vista General del Producto](#_Toc52661349)

[4.1 Perspectiva del producto](#_Toc41)

[4.2 Resumen de capacidades](#_Toc42)

[4.3 Suposiciones y dependencias](#_Toc43)

[4.4 Costos y precios](#_Toc44)

[4.5 Licenciamiento e instalación](#_Toc45)

[5. Características del producto](#_Toc52661350)

[6. Restricciones](#_Toc52661351)

[7. Rangos de calidad](#_Toc52661352)

[8. Precedencia y Prioridad](#_Toc52661353)

[9. Otros requerimientos del producto](#_Toc52661354)

[CONCLUSIONES](#_Toc52661355)

[RECOMENDACIONES](#_Toc52661356)

[BIBLIOGRAFIA](#_Toc52661357)

[WEBGRAFIA](#_Toc52661358)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Visión</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Introducción**

    1.1 <span id="_Toc11" class="anchor"></span>**Propósito**
    
    El propósito del presente Documento de Visión es definir el alcance, los objetivos, los interesados, las necesidades, las características principales y las restricciones del sistema denominado *Dashboard de empleabilidad de egresados EPIS-UPT*.

    Este documento proporcionará una visión general de la solución y servirá como referencia para que el equipo del proyecto, la Dirección de la Escuela Profesional de Ingeniería de Sistemas, el Comité de Acreditación y los responsables de GPS Alumni comprendan la finalidad y las capacidades esperadas del sistema.

    La solución estará orientada a integrar, procesar y visualizar información sobre la situación laboral de los egresados mediante indicadores, gráficos, tablas y filtros interactivos que apoyen la toma de decisiones académicas.

    1.2 <span id="_Toc12" class="anchor"></span>**Alcance**
    
    El proyecto comprende el desarrollo de un dashboard de Inteligencia de Negocios para analizar y realizar el seguimiento de la empleabilidad de los egresados de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna.

    El alcance del sistema incluye:

    - Recopilar información procedente de encuestas a egresados, registros de la Escuela Profesional y datos del programa GPS Alumni, siempre que se cuente con la autorización institucional correspondiente.

    - Integrar y almacenar la información consolidada en una base de datos PostgreSQL.

    - Ejecutar procesos de extracción, limpieza, transformación y carga de datos mediante Python, Pandas y SQLAlchemy.

    - Analizar información relacionada con la situación laboral, año de egreso, tiempo de inserción laboral, área de desempeño, ubicación geográfica, rango salarial, correspondencia entre la formación y el empleo, y competencias tecnológicas requeridas.

    - Calcular indicadores clave de empleabilidad, como la tasa de egresados empleados, el porcentaje que trabaja en un área relacionada con Ingeniería de Sistemas y el tiempo promedio de inserción laboral.

    - Diseñar un dashboard interactivo en Power BI con gráficos, tablas, mapas y filtros dinámicos.

    - Permitir la consulta de información por parte de los usuarios autorizados de la Dirección de la EPIS, el Comité de Acreditación y GPS Alumni.

    - Generar reportes consolidados que apoyen la toma de decisiones académicas y los procesos de acreditación.

    - Desarrollar, probar e implementar la solución durante un periodo estimado de 16 semanas.


    ### Exclusiones del alcance
    
    El sistema no incluirá:
    
    - La gestión de trámites de egreso, grados académicos o titulación.
    - La administración de ofertas laborales o procesos de contratación.
    - El funcionamiento como bolsa de trabajo.
    - La modificación directa de la información del sistema académico institucional.
    - El análisis predictivo de tendencias laborales durante la primera versión.
    - La publicación de datos personales identificables de los egresados.
  


    1.3 <span id="_Toc13" class="anchor"></span>**Definiciones, Siglas y Abreviaturas**
    - **UPT**: Universidad Privada de Tacna.
    - **EPIS**: Escuela Profesional de Ingeniería de Sistemas.
    - **BI (Business Intelligence)**: Inteligencia de Negocios; conjunto de estrategias, aplicaciones y tecnologías enfocadas a la administración y creación de conocimiento a través del análisis de datos.
    - **ETL (Extract, Transform, Load)**: Proceso de Extracción, Transformación y Carga de datos desde fuentes origen hacia una base de datos analítica.
    - **KPI (Key Performance Indicator)**: Indicador Clave de Desempeño cuantificable.
    - **GPS Alumni**: Programa institucional de seguimiento a egresados de la Universidad Privada de Tacna.
    - **ICACIT**: Instituto de Calidad y Acreditación de Carreras de Ingeniería y Tecnología.
    - **Ley N° 29733**: Ley de Protección de Datos Personales en el Perú.


    1.4 <span id="_Toc14" class="anchor"></span>**Referencias**
    - Proyecto de Inteligencia de Negocios EPIS-UPT (2026). *Bases del Dashboard de Empleabilidad de Egresados*.
    - Estatuto Universitario y Reglamento de Seguimiento al Egresado de la Universidad Privada de Tacna.
    - Estándares de Acreditación de Carreras Universitarias de Ingeniería de Sistemas (ICACIT / SINEACE).
    - Informe de factibilidad (FD01)


    1.5 <span id="_Toc15" class="anchor"></span>**Visión General**
    
    El presente Documento de Visión describe el propósito y alcance del sistema, el problema que se busca resolver, los interesados y usuarios involucrados, las necesidades identificadas y las principales características del producto.

    Asimismo, presenta las capacidades esperadas del dashboard, las tecnologías seleccionadas, las restricciones del proyecto, los criterios de calidad, las prioridades de implementación y los requerimientos relacionados con la seguridad y protección de los datos.

    Este documento deberá utilizarse junto con el FD01 – Informe de factibilidad, debido a que ambos establecen las condiciones técnicas, económicas, operativas y funcionales necesarias para desarrollar el sistema durante las 16 semanas previstas.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



2. <span id="_Toc52661347" class="anchor"></span>**Posicionamiento**

    2.1 <span id="_Toc21" class="anchor"></span>**Oportunidad de negocio**
    
    La Escuela Profesional de Ingeniería de Sistemas requiere información integrada y actualizada para conocer la situación laboral de sus egresados y evaluar la correspondencia entre la formación académica y las necesidades del mercado laboral.

    La implementación del dashboard representa una oportunidad para transformar los datos recopilados mediante GPS Alumni, encuestas y registros institucionales en indicadores que faciliten su análisis. Esta información permitirá identificar tendencias de empleabilidad, áreas de desempeño, tiempos de inserción laboral, competencias tecnológicas requeridas y posibles brechas entre la formación recibida y los puestos ocupados.

    Los resultados obtenidos podrán apoyar la actualización del plan de estudios, el diseño de actividades de capacitación, el seguimiento de los egresados y la presentación de evidencias durante los procesos de acreditación.

    Por lo tanto, la oportunidad institucional consiste en mejorar el uso de la información disponible y fortalecer la toma de decisiones académicas basada en datos.



   2.2 <span id="_Toc22" class="anchor"></span>**Definición del problema**

    | Aspecto | Descripción |
    |---|---|
    | **Problema identificado** | La información sobre la situación laboral y trayectoria profesional de los egresados se encuentra dispersa en hojas de cálculo, encuestas y registros institucionales que no están integrados. |
    | **Personas y áreas afectadas** | La Dirección de la EPIS, el Comité de Acreditación, los responsables de GPS Alumni y, de manera indirecta, los estudiantes y egresados. |
    | **Impacto del problema** | Incremento del tiempo necesario para consolidar la información, dificultad para calcular indicadores de empleabilidad, limitada capacidad para identificar tendencias laborales y demora en la elaboración de reportes para la toma de decisiones y los procesos de acreditación. |
    | **Causas principales** | Falta de una base de datos consolidada, formatos de información no estandarizados, registros incompletos y ausencia de una herramienta interactiva para analizar los datos. |
    | **Solución propuesta** | Desarrollar un dashboard de Inteligencia de Negocios que permita integrar, depurar, procesar y visualizar la información mediante indicadores, gráficos, tablas, mapas y filtros dinámicos. |
    | **Resultado esperado** | Disponer de información organizada y actualizada que facilite el análisis de la empleabilidad y apoye la toma de decisiones académicas. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Descripción de los interesados y usuarios**

    3.1 <span id="_Toc31" class="anchor"></span>**Resumen de los interesados**

    | Nombre | Función / Rol | Representación |
    | :--- | :--- | :--- |
    | Director de la EPIS | Autoridad Académica | Toma decisiones sobre actualización curricular y convenios institucionales. |
    | Comité de Acreditación | Evaluadores de Calidad | Requiere métricas e indicadores de empleabilidad para renovar acreditaciones. |
    | Coordinación GPS Alumni UPT | Responsable de Egresados | Encargado del levantamiento y mantenimiento de datos de egresados. |
    | Egresados de la EPIS | Fuente de Información | Proveen datos sobre su estatus laboral y retroalimentan a la universidad. |

    3.2 <span id="_Toc32" class="anchor"></span>**Resumen de los usuarios**

    | Usuario | Descripción | Rol en el Sistema |
    | :--- | :--- | :--- |
    | **Administrador del Dashboard** | Personal técnico o docente de la EPIS. | Carga de datos, actualización de fuentes y mantenimiento de permisos. |
    | **Analista Académico / Directivo** | Director de Escuela, Miembros del Comité de Calidad. | Consulta de tableros, aplicación de filtros y exportación de reportes. |
    | **Docentes y Investigadores** | Plana docente de la carrera. | Consulta de tendencias de especialidad para proyectos de investigación y cursos. |

    3.3 <span id="_Toc33" class="anchor"></span>**Entorno de usuario**
    
    Los usuarios accederán al dashboard a través de navegadores web modernos (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari) desde computadoras de escritorio, laptops y tabletas, con conexión a la red intrainstitucional de la UPT o mediante enlace seguro en internet.

    3.4 <span id="_Toc34" class="anchor"></span>**Perfiles de los interesados**

    - **Perfil del Director de la EPIS**:
      - *Interés*: Conocer el porcentaje de graduados empleados y la afinidad de sus puestos con la formación recibida.
      - *Criterio de éxito*: Disponibilidad de gráficos claros ejecutivos y resúmenes exportables sin complejidad técnica.
    - **Perfil del Comité de Acreditación**:
      - *Interés*: Obtener tablas cuantitativas de inserción laboral por cohorte y tiempo transcurrido hasta el primer empleo.
      - *Criterio de éxito*: Exactitud de los datos y capacidad de filtrar información por años específicos.

    3.5 <span id="_Toc35" class="anchor"></span>**Perfiles de los Usuarios**

    - **Perfil del Analista / Directivo (Usuario Final)**:
      - *Nivel técnico*: Medio. Familiarizado con gráficos interactivos y filtros.
      - *Frecuencia de uso*: Mensual o trimestral (previo a sesiones de consejo de escuela y auditorías).
      - *Comportamiento*: Interactúa con segmentadores por año, área de desempeño y mapas regionales.

    3.6 <span id="_Toc36" class="anchor"></span>**Necesidades de los interesados y usuarios**

    | Necesidad | Inconveniente Actual | Solución Propuesta |
    | :--- | :--- | :--- |
    | Conocer la tasa de empleo de egresados. | Información dispersa en archivos Excel desconectados. | KPI visible en pantalla principal con porcentaje de empleo actualizado. |
    | Identificar áreas profesionales con mayor demanda. | Desconocimiento del perfil específico desempeñado (Dev, QA, Data, DevOps, Infraestructura). | Gráfico de barras interactivo con distribución por áreas tecnológicas. |
    | Medir el tiempo transcurrido para conseguir empleo. | Carencia de registros unificados de fecha de egreso vs. contratación. | Gráfico de distribución de meses transcurridos hasta la inserción laboral. |
    | Conocer la ubicación geográfica del empleo. | Dificultad para saber si laboran en Tacna, Lima o el extranjero. | Mapa interactivo de distribución regional y nacional. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Vista General del Producto**

    4.1 <span id="_Toc41" class="anchor"></span>**Perspectiva del producto**
    
    El *Dashboard de empleabilidad* se concibe como una solución analítica autónoma pero integrada formalmente en el ecosistema informático de la EPIS-UPT. Recibe datos limpios del proceso ETL alimentado por encuestas y por la base de datos institucional de egresados, exponiendo indicadores visuales mediante una interfaz moderna de Business Intelligence.

    4.2 <span id="_Toc42" class="anchor"></span>**Resumen de capacidades**

    | Área Funcional | Capacidad Clave |
    | :--- | :--- |
    | **Resumen Ejecutivo (General)** | Muestra KPIs principales: % Empleados, % en área de Sistemas, Tiempo Promedio de Inserción (meses), Rango Salarial Medio. |
    | **Análisis por Cohorte** | Permite filtrar y comparar indicadores por año de egreso (ej. 2020 a 2026). |
    | **Afinidad Formativa** | Visualiza el porcentaje de egresados que desempeñan cargos directamente relacionados con el plan de estudios. |
    | **Distribución Geográfica y Sectorial** | Mapa interactivo con concentración laboral (Tacna, otras regiones del Perú, remoto internacional) y tipo de empresa (Pública/Privada/Startup/Emprendimiento). |
    | **Capacitación Continua** | Gráficos con las tecnologías, certificaciones y posgrados requeridos por los egresados para su crecimiento. |

    4.3 <span id="_Toc43" class="anchor"></span>**Suposiciones y dependencias**
    - Se asume la disponibilidad continua de los registros históricos del programa GPS Alumni.
    - El acceso a los servidores o servicio BI estará habilitado por la coordinación de TI de la UPT.
    - Se asume una participación activa de los egresados al responder las encuestas institucionales.

    4.4 <span id="_Toc44" class="anchor"></span>**Costos y precios**
    
    El sistema será desarrollado para uso institucional de la Universidad Privada de Tacna y no tendrá un precio de venta comercial.

    De acuerdo con el FD01 – Informe de factibilidad, el costo total estimado del proyecto es de **S/13,270.00**, distribuido de la siguiente manera:

    | Categoría de costo | Monto (S/) | Porcentaje |
    |---|---:|---:|
    | Costos generales | 1,150.00 | 8.67 % |
    | Costos operativos | 1,880.00 | 14.17 % |
    | Costos del ambiente tecnológico | 240.00 | 1.81 % |
    | Costos de personal | 10,000.00 | 75.35 % |
    | **Costo total estimado del proyecto** | **13,270.00** | **100.00 %** |
    
    El monto de **S/240.00** corresponde únicamente al costo tecnológico estimado para una licencia de Power BI Service durante los cuatro meses de desarrollo. No representa el costo total del proyecto.
    
    Los montos deberán actualizarse si cambia la cantidad de licencias, el tipo de cambio, la infraestructura utilizada o la duración del proyecto.


    4.5 <span id="_Toc45" class="anchor"></span>**Licenciamiento e instalación**
    - Licencia de desarrollo: Software de código abierto o licencias educativas de Microsoft Power BI / Python.
    - Instalación: Despliegue en la infraestructura web o portal institucional de la Universidad Privada de Tacna.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

5. <span id="_Toc52661350" class="anchor"></span>**Características del producto**

    - **Filtros Dinámicos Integrados**: Segmentación interactiva por Año de Egreso, Sexo, Estado Laboral, Modalidad de Trabajo (Presencial, Remoto, Híbrido) y Región.
    - **Visualización de KPIs de Empleabilidad**: Tarjetas dinámicas con métricas de alto nivel (% Empleados, % en el Sector de TI, Tiempo medio de inserción).
    - **Gráfico de Sectores y Puestos de Trabajo**: Diagramas de barras y pastel con las principales áreas profesionales (Desarrollo de Software, Gestión de Proyectos, Seguridad Informática, Ciencia de Datos, Infraestructura/Redes).
    - **Mapa de Distribución Geográfica**: Representación geográfica interactiva que muestra la ubicación de los egresados a nivel regional, nacional e internacional.
    - **Gráfico de Afinidad Formación vs. Trabajo**: Evaluación de la coherencia entre el plan de estudios de la EPIS y los requerimientos del mercado laboral.
    - **Exportación de Reportes**: Capacidad para exportar vistas consolidadas a formatos PDF o Excel para la confección de expedientes de acreditación.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

6. <span id="_Toc52661351" class="anchor"></span>**Restricciones**

    - **Seguridad y Privacidad**: Ningún usuario no autorizado podrá visualizar datos personales identificables (Nombres, DNI, Correos) de los egresados. Los reportes serán agregados y anonimizados.
    - **Frecuencia de Actualización**: La actualización del Data Mart analítico se ejecutará periódicamente (semestral o anualmente) conforme se apliquen las encuestas de egresados.
    - **Compatibilidad**: El dashboard debe ser 100% compatible con navegadores web estándar sin necesidad de instalar complementos o plugins pesados en el cliente.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


7. <span id="_Toc52661352" class="anchor"></span>**Rangos de calidad**

    - **Usabilidad**: Interfaz intuitiva basada en principios de diseño de dashboards (UX/UI), permitiendo obtener cualquier indicador con menos de 3 clics.
    - **Rendimiento**: Tiempo de respuesta para la carga de visualizaciones e interacción con filtros inferior a **2 segundos**.
    - **Disponibilidad**: Disponibilidad del servicio del **99.5%** durante el periodo lectivo universitario.
    - **Confiabilidad**: Tasa de error en el procesamiento de datos del 0%, garantizando que las métricas reflejen exactamente los registros fuente.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

8. <span id="_Toc52661353" class="anchor"></span>**Precedencia y Prioridad**

    | Característica | Prioridad | Justificación |
    | :--- | :--- | :--- |
    | Integración ETL de Datos de Egresados | **Alta** | Fundamento indispensable para alimentar cualquier visualización. |
    | Tablero de KPIs de Empleabilidad y Tiempo de Inserción | **Alta** | Responde a la necesidad central del problema planteado. |
    | Visualización por Áreas de Desempeño y Afinidad | **Alta** | Requerimiento clave para la toma de decisiones curriculares. |
    | Mapa de Distribución Geográfica | **Media** | Complementa el análisis con la dimensión regional/nacional. |
    | Exportación de Reportes en PDF/Excel | **Media** | Facilita la labor administrativa para auditorías ICACIT. |
    | Análisis Predictivo de Tendencias | **Baja** | Funcionalidad avanzada para fases futuras del sistema. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

9. <span id="_Toc52661354" class="anchor"></span>**Otros requerimientos del producto**

    **b) Estándares legales**
    Cumplimiento de la Ley N° 29733 (Ley de Protección de Datos Personales de Perú) y normativas sobre propiedad intelectual de la Universidad Privada de Tacna.

    **c) Estándares de comunicación**
    Transmisión de datos encriptada mediante protocolo seguro HTTPS para las conexiones del dashboard en entornos web.

    **d) Estándares de cumplimiento de la plataforma**
    Diseño adaptativo (responsive web design) garantizando la visualización óptima en pantallas con resolución mínima de 1280x720 píxeles.

    **e) Estándares de calidad y seguridad**
    Autenticación de usuarios por roles para restringir el acceso a vistas administrativas o de actualización de datos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661355" class="anchor"></span>**CONCLUSIONES**

- El Documento de Visión establece con claridad el marco conceptual, alcance y especificaciones del *Dashboard de empleabilidad de los egresados de Ingeniería de Sistemas de la UPT*.
- La solución propuesta transforma la recolección pasiva de datos en un activo analítico de Inteligencia de Negocios de alto impacto para la gestión universitaria.
- Las características priorizadas garantizan la atención inmediata a las necesidades de la Dirección de Escuela y comités de acreditación, fortaleciendo la calidad de la formación profesional.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661356" class="anchor"></span>**RECOMENDACIONES**

- Se recomienda formalizar la frecuencia de aplicación del cuestionario de empleabilidad con la coordinación de GPS Alumni UPT para mantener actualizado el dashboard.
- Capacitar a las autoridades de la EPIS en el uso e interpretación de los indicadores visuales para maximizar la adopción de la herramienta.
- Promover la integración progresiva de nuevas variables como certificaciones internacionales y dominio de idiomas en versiones futuras del sistema.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661357" class="anchor"></span>**BIBLIOGRAFIA**

- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). Wiley.
- Few, S. (2013). *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring* (2nd ed.). Analytics Press.
- Abran, A., & Moore, J. W. (2004). *SWEBOK: Guide to the Software Engineering Body of Knowledge*. IEEE Computer Society.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661358" class="anchor"></span>**WEBGRAFIA**

- Universidad Privada de Tacna: [https://www.upt.edu.pe](https://www.upt.edu.pe)
- Instituto de Calidad y Acreditación de Carreras de Ingeniería y Tecnología (ICACIT): [https://www.icacit.org.pe](https://www.icacit.org.pe)
- Microsoft Power BI Documentation: [https://learn.microsoft.com/es-es/power-bi/](https://learn.microsoft.com/es-es/power-bi/)
