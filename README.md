# Dashboard de seguimiento laboral — EPIS UPT

Proyecto de Inteligencia de Negocios para describir la evidencia laboral pública de los egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna, promociones 2017–2024. Curso SI885, 2026-I.

## Alcance

La semilla contiene 141 registros. Se excluyen 2 segundos grados y se analizan 139 casos, de los cuales 35 tienen evidencia laboral pública: **25,2 % de cobertura de información**.

La cobertura no es tasa de empleabilidad. Los 104 restantes tienen situación laboral desconocida; no pueden considerarse desempleados. Los perfiles observados no representan necesariamente al universo ni miden demanda laboral.

No se estiman salarios, desempleo, tiempo de inserción ni evolución histórica. Los años de grado identifican promociones, no fechas de observación laboral. El corte documentado es setiembre de 2026; generar otra vez el HTML no actualiza las fuentes.

## Ejecutar con los datos existentes

En PowerShell, desde la raíz del proyecto:

```powershell
python -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
python -m empleabilidad.modelo
python -m empleabilidad.kpis
python -m empleabilidad.tablero
Start-Process .\dashboard\index.html
```

El tablero funciona desde disco, sin servidor ni conexión de red. No se ha configurado ni realizado un despliegue.

El flujo completo `python -m empleabilidad.pipeline` comienza por la nómina nominal privada y requiere `data/raw/nomina_oficial_upt.csv`. Para trabajar únicamente con la semilla pública, utiliza los comandos anteriores.

## Secciones

- **Resumen:** cuatro tarjetas (universo, evidencia, cobertura y situación desconocida), estado de información global y comparación breve por promoción.
- **Promociones:** comparación ordenable, selección por año, referencia global descriptiva y gráfico de volumen por promoción.
- **Perfil laboral observado:** una tarjeta de afinidad entre casos conocidos, con la base laboral como contexto, cuatro gráficos simultáneos (sectores, áreas, empleadores y ámbito) y disponibilidad de afinidad.
- **Calidad:** cuatro tarjetas (empleador, cargo, ámbito y pendientes); área y afinidad se conservan en el gráfico de completitud, gráficos de completitud, confianza y estados de información, y vacíos de datos.
- **Ayuda y metodología:** instrucciones, reglas, fichas con pregunta, fórmula, denominador, fuente, interpretación y decisión; arquitectura y diagrama del modelo dimensional implementado.

El menú se pliega en computadora y se despliega en celular. Se conserva la promoción al navegar. Las definiciones y tablas se abren mediante controles nativos accesibles con teclado y táctil. Se mantienen temas claro y oscuro.

## Indicadores y denominadores

| Indicador | Definición | Resultado del corte |
|---|---|---|
| Universo | Registros excluyendo segundos grados | 139 |
| Cobertura | Evidencia laboral / universo × 100 | 35 / 139 = 25,2 % |
| Empleador identificado | Empleador con contenido / casos con empleo verificado | 28 / 35 = 80 % |
| Cargo identificado | Cargo con contenido / casos con empleo verificado | 11 / 35 = 31,4 % |
| Ámbito conocido | Ámbito distinto de no determinado / casos con empleo verificado | 13 / 35 = 37,1 % |
| Afinidad conocida | Afinidad 0 o 1 / casos con empleo verificado | 11 / 35 |
| Afinidad entre conocidos | Afines / afinidad conocida × 100 | 11 / 11 = 100 % |

El último porcentaje describe solo 11 casos, no al universo. Se corrigió la inferencia de docencia desde un instituto sin cargo declarado. El modelo también normaliza semillas anteriores: sin cargo, área y afinidad permanecen desconocidas.

Cargo identificado, área determinada y afinidad conocida son conceptos distintos, aunque sus cantidades coincidan en este corte. El ámbito corresponde al empleador, no a residencia ni lugar efectivo de trabajo.

## Filtros y protección del paquete público

`dashboard/datos.json` y el HTML contienen únicamente agregados; no contienen identificadores ni observaciones individuales.

- Umbral de publicación de detalles: 5 casos.
- Categorías pequeñas se agrupan sin publicar sus etiquetas o cantidades individuales. Si el grupo resultante sigue pequeño, se incorpora otra categoría.
- En cobertura por promoción se protegen numerador, porcentaje y complemento. Si una sola promoción queda oculta, se suprime adicionalmente otra para evitar recuperarla restando del total.
- Los perfiles y confianza se publican como distribuciones marginales globales; no se permiten cruces entre dimensiones ni perfiles por promoción.
- Sectores y áreas se muestran en paneles globales simultáneos; no recalculan cobertura ni permiten cruzar dimensiones. Las tablas muestran el porcentaje de cada categoría sobre los 35 casos con evidencia.
- Resumen siempre muestra todas las promociones. El filtro de promoción aparece únicamente en Promociones. Perfil y Calidad mantienen siempre sus gráficos globales; la selección se conserva al regresar al seguimiento.

Esta protección reduce exposición en el tablero, pero no demuestra anonimato frente a información externa. **La semilla seudonimizada permanece en el repositorio:** si este es público, ese archivo tiene su propio riesgo de divulgación. No publiques la raíz del repositorio como paquete web; el paquete del tablero está separado.

## Arquitectura

```text
CSV semilla → Python/SQL → modelo estrella DuckDB → agregados protegidos → HTML
```

La nómina nominal solo se utiliza en ingesta y no se versiona. La semilla seudonimizada se procesa localmente. DuckDB no se ejecuta en el navegador. El almacén se reconstruye y no conserva historial laboral.

La ingesta utiliza `UPT_SALT` del entorno y tiene una sal de desarrollo por defecto. Para procesar datos nominales reales hay que configurar una sal privada; `.env` no se carga automáticamente. La seudonimización no equivale a anonimización.

## Verificación

```powershell
$env:PYTHONPATH = "src"
python -m pytest tests -q
```

Las pruebas cubren contrato, clasificación, cifras de la semilla, afinidad, denominadores, agregación, supresión complementaria y ausencia de observaciones individuales en la exportación. Después de cambios de interfaz, verifica menú, filtros, tablas y distribución a distintos anchos en navegador.

## Estructura

```text
data/raw/               nómina nominal privada, no versionada
data/seed/              fuente seudonimizada del corte
data/marts/             DuckDB generado
src/empleabilidad/      ingesta, clasificación, modelo, indicadores y render
sql/                    modelo dimensional
dashboard/              plantilla y artefactos generados
tests/                  comprobaciones del proceso
docs/adr/               decisiones originales de arquitectura
```

Los informes académicos originales se encuentran en la rama `Documentos`. Las decisiones originales en ADR se complementan con `docs/adr/004-publicacion-agregada.md`.


## Funciones de consulta y salida

- **CSV:** cada tabla ofrece descarga en el orden visible, con sección, corte, fuente y aviso de protección. Los valores protegidos permanecen como texto; no se recuperan datos ocultos. El archivo usa UTF-8 y separador punto y coma.
- **Ordenar:** pulsa un encabezado para alternar orden ascendente y descendente.
- **Comparar:** en Promociones, selecciona dos años para contrastar universo, evidencia, cobertura y situación desconocida del mismo corte. La protección se conserva.
- **Imprimir / guardar PDF:** disponible en Resumen general; imprime el resumen con fuentes y advertencias, sin menú ni controles. El navegador permite elegir Guardar como PDF.
- **Preferencias:** tema y plegado del menú se guardan localmente cuando el navegador permite almacenamiento; no se envían a ningún servicio.
- **Valores protegidos:** el botón de ayuda explica por qué se ocultan cantidades y complementos; protegido no equivale a cero.

- **Compartir vista:** genera un enlace con sección, promoción y comparación seleccionadas. En modo archivo local solo funciona donde exista el archivo; compartir entre dispositivos requiere publicar la web.
- **Buscar en Ayuda:** filtra las fichas de indicadores por texto, sin distinguir mayúsculas ni tildes.
- **Diferencia de cobertura:** compara cada promoción con la cobertura global en puntos porcentuales; los valores protegidos no se calculan ni revelan.
- **Guía de uso:** muestra instrucciones opcionales al inicio de Ayuda y metodología.
- **Restablecer preferencias:** elimina las preferencias locales de tema y menú y vuelve a su presentación inicial.
