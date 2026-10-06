# Propuesta de Proyecto de Inteligencia de Negocios

## 1. Título del Proyecto
**Desarrollo de una aplicación de Inteligencia de Negocios (BI) basada en analítica geoespacial para la centralización de reportes, clasificación automatizada de alertas y priorización de avisos por daño vial en la Provincia de Tacna**

---

## 2. Problema Detallado con Fuentes

### Definición del Problema
Las calles y avenidas principales de la provincia de Tacna sufren una degradación constante en su capa asfáltica. Vías de alto tránsito como la Av. Municipal en Coronel Gregorio Albarracín Lanchipa, la Av. Internacional en Ciudad Nueva y la Av. Jorge Basadre Grohmann presentan baches profundos, hundimientos estructurales y grietas severas. Sin embargo, el problema crítico institucional no es solo el daño físico de las pistas, sino la **ineficiencia actual para recibir, procesar y clasificar los reportes viales para avisar de manera oportuna a las autoridades municipales**.

Actualmente, el flujo de información y la toma de decisiones adolecen de tres deficiencias principales:
1. **Descentralización y desorden en los avisos:** Cuando un conductor de transporte público (rutas locales) o un ciudadano identifica un bache peligroso, los reportes se emiten de manera informal a través de llamadas a radios locales (como Radio Uno), quejas en redes sociales o solicitudes físicas en mesa de partes. Esta información llega dispersa, sin coordenadas precisas y en formatos incompatibles.
2. **Subjetividad y falta de priorización técnica:** La Municipalidad Provincial de Tacna procesa las quejas de forma manual en hojas de cálculo aisladas. Al no contar con una aplicación analítica, no se puede medir la gravedad real de los incidentes. Un bache profundo en una vía rápida de alta velocidad se trata con la misma urgencia que una grieta menor en un pasaje residencial, lo que satura las áreas operativas con datos irrelevantes y deja las verdaderas emergencias sin atender.
3. **Ausencia de un motor de alertas inteligente:** La gerencia municipal carece de una plataforma de Inteligencia de Negocios que combine los reportes ciudadanos con datos internos de la ciudad (jerarquía de avenidas, recurrencia de quejas en un mismo punto o historial de contratistas). Como la entidad no se entera a tiempo ni de forma clasificada, las pistas siguen empeorando, lo que genera un incremento en los accidentes de tránsito, congestión vehicular y un gasto público ineficiente al reparar calles de forma reactiva cuando ya colapsaron.

### Fuentes de Información y Sustento
* **Registros de Incidencias Locales:** Informes de atención al ciudadano de la Municipalidad Provincial de Tacna, reclamos documentados por los sindicatos de transportistas y colectiveros de la región, y reportes de denuncias ciudadanas en medios de comunicación de Tacna.
* **Datos de Seguridad Vial y Normativa:** Estadísticas de siniestralidad vial de las comisarías de la Policía Nacional del Perú (PNP) en Tacna y los reportes del Observatorio Nacional de Seguridad Vial del Ministerio de Transportes y Comunicaciones (MTC), que evidencian los accidentes provocados por fallas en la calzada.
* **Metodología de BI y Clasificación Vial:** Lineamientos internacionales del Índice de Condición del Pavimento (PCI) para tipificar fallas (baches, hundimientos, grietas longitudinales y piel de cocodrilo) adaptados a la metodología de modelado dimensional de Ralph Kimball para el diseño de almacenes de datos (*Data Warehouses*) corporativos.

---

## 3. Objetivos de Investigación

### Objetivo General
* Diseñar e implementar una **aplicación de Inteligencia de Negocios (BI)** que centralice, procese y clasifique de forma automatizada los reportes de daños viales en Tacna, funcionando como un sistema analítico que **avise y emita alertas tempranas de prioridad** a las gerencias municipales para optimizar la toma de decisiones.

### Objetivos Específicos
1. **Diagnosticar y estandarizar** los canales de captura de datos de daños en las calzadas (reportes ciudadanos, inspectores y redes sociales) para unificar la información en una base de datos limpia.
2. **Diseñar el backend dimensional** (esquema estrella) de la aplicación, relacionando los avisos de daños con las dimensiones de ubicación geográfica (coordenadas GPS/distritos de Tacna), tipo de vía, volumen de tráfico y nivel de severidad técnica.
3. **Desarrollar el motor lógico de la aplicación** mediante un proceso ETL (Extracción, Transformación y Carga) que calcule de forma matemática una matriz de puntuación de prioridad para cada reporte ingresado.
4. **Implementar la interfaz de usuario de la aplicación (*Dashboard*) con mapas geoespaciales** que pinten mediante un semáforo analítico (Alerta Roja, Amarilla y Verde) las emergencias viales activas para avisar inmediatamente a los tomadores de decisiones de la municipalidad.

---

## 4. Solución Medible (Indicadores de Éxito)

La propuesta técnica consiste en una **aplicación analítica de monitoreo y avisos automatizados** (desarrollada en Power BI o Tableau conectada a un servidor SQL Server). El éxito y la viabilidad del proyecto se evaluarán mediante las siguientes métricas cuantificables:

* **Métrica de Velocidad del Aviso:** Reducir el tiempo de procesamiento y notificación formal de un reporte crítico a la gerencia correspondiente, pasando de un promedio de 15 días hábiles a **menos de 2 horas** mediante el envío de alertas automáticas en la pantalla de la aplicación municipal.
* **Métrica de Precisión de la Clasificación:** Lograr que el motor de la aplicación clasifique correctamente el nivel de riesgo de al menos el **95% de los avisos recibidos**, garantizando que las alertas rojas (baches en avenidas principales) se posicionen en la cima de la pantalla de forma automática.
* **Métrica de Filtrado e Inteligencia Social:** Conseguir un **100% de efectividad en la eliminación de avisos duplicados**, logrando que la aplicación identifique mediante proximidad de coordenadas GPS si múltiples reportes pertenecen al mismo bache, agrupándolos y sumando puntos de urgencia por presión ciudadana en lugar de saturar el mapa.
* **Métrica de Productividad y Adopción:** Reducir en un **90% el tiempo empleado por el personal administrativo** para elaborar el consolidado mensual de estado de pistas en Tacna, sustituyendo los reportes manuales en Excel por la actualización automática de la aplicación que muestra el mapa de calor de alertas viales en tiempo real.