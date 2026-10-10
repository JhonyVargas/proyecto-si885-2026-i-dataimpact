# ADR 004 — Publicación de agregados y navegación por secciones

Estado: aceptada. Fecha: 2026-10-10.

## Contexto

El tablero anterior exportaba 139 observaciones con identificadores seudónimos. Marcaba celdas pequeñas sin eliminar sus valores y el navegador recalculaba grupos individuales. Filtrar por sector producía 100 % de cobertura por construcción.

## Decisión

Publicar únicamente agregados protegidos. El umbral es 5: categorías menores se fusionan y sus etiquetas no se exportan. Una agrupación que no llega al umbral absorbe otra categoría. En pares se suprimen valor y complemento cuando cualquiera es pequeño; la cobertura por promoción aplica también supresión complementaria si solo hay una promoción oculta.

Las distribuciones laborales y confianza son marginales globales. No se ofrecen cruces entre promoción, sector, área y confianza. La promoción seleccionada se mantiene, pero los apartados de perfil y calidad no revelan detalle de esa promoción. Seleccionar una categoría consulta su agregado global.

La interfaz se divide en Resumen, Promociones, Perfil, Calidad y Ayuda. Esta última contiene el diagrama de arquitectura. Sin cargo declarado, área y afinidad se mantienen desconocidas: se corrige el caso del instituto antes clasificado como docencia. El denominador de afinidad pasa de 12 a 11; los 11 conocidos son afines. Esto describe únicamente esos casos.

## Consecuencias y límites

La protección reduce el detalle disponible: no se muestran rankings de empleadores con 1–4 casos ni ubicaciones pequeñas. El perfil laboral no tiene filtros cruzados. El gráfico de áreas incluye la categoría desconocida para mantener visible la base de 35 casos.

No se afirma anonimato frente a fuentes externas. La semilla versionada continúa disponible a quien acceda al repositorio; esta decisión protege el paquete del dashboard y no elimina ese riesgo independiente. No se publica ni se configura hosting en este cambio.
