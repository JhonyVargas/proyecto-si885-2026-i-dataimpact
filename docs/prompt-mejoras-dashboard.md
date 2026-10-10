# Prompt para mejorar el dashboard de seguimiento laboral

Actúa como ingeniero de Inteligencia de Negocios y desarrollador web. Implementa las mejoras descritas en el proyecto existente de seguimiento laboral de egresados de Ingeniería de Sistemas de la Universidad Privada de Tacna.

Trabaja directamente sobre el repositorio. Revisa primero las instrucciones del proyecto, la documentación y el código. No te limites a proponer un diseño: implementa, ejecuta el proceso y verifica el resultado.

## Contexto y arquitectura

El proyecto analiza las promociones 2017–2024 mediante una nómina y fuentes públicas.

La fuente de trabajo disponible es:

`data/seed/egresados_seed.csv`

El flujo actual es:

`CSV → modelo dimensional DuckDB → dashboard/datos.json → dashboard/index.html`

Archivos principales:

- `src/empleabilidad/clasificacion.py`
- `src/empleabilidad/ingest.py`
- `src/empleabilidad/modelo.py`
- `src/empleabilidad/kpis.py`
- `src/empleabilidad/tablero.py`
- `src/empleabilidad/pipeline.py`
- `sql/modelo_estrella.sql`
- `dashboard/plantilla.html`
- `tests/`
- `README.md`

Mantén Python, SQL, DuckDB y el dashboard estático con datos embebidos. Debe funcionar al abrir el HTML desde el disco y en un alojamiento estático, sin servidor ni dependencias de red. No agregues API, encuestas ni fuentes externas.

Conserva el estilo visual existente, los temas claro y oscuro y los botones para consultar tablas.

## Reglas metodológicas

Los resultados actuales son una referencia de comprobación, no valores para escribir manualmente en la interfaz:

- 141 registros en la semilla.
- 2 registros marcados como segundos grados.
- 139 casos analizados.
- 35 casos con evidencia laboral pública.
- Cobertura global de 25,2 %.
- 104 casos sin situación laboral verificable.

Verifica estas cifras contra el CSV.

La cobertura NO es la tasa de empleabilidad. La ausencia de información NO significa desempleo.

Los sectores, empleadores y áreas describen los casos encontrados. No representan necesariamente a todos los egresados ni permiten estimar demanda laboral.

Comparar promociones no equivale a observar evolución temporal del empleo: son grupos de distintos años de grado observados en un mismo corte.

El ámbito del empleador no confirma residencia ni ubicación efectiva del trabajador.

No calcules salarios, desempleo, tiempo de inserción, vigencia por caso ni tendencias históricas: faltan datos para ello.

## 1. Corregir y formalizar los indicadores

Documenta para cada indicador su pregunta, fórmula, numerador, denominador, filtros válidos y limitaciones.

Revisa la clasificación de afinidad. Existe un caso clasificado como “Docencia” y no afín a partir del empleador, sin cargo declarado. Corrige esa inferencia y revisa casos equivalentes.

Sin información suficiente sobre el cargo, la afinidad debe ser desconocida (`NULL`), nunca negativa por defecto.

Distingue:

- Cargo identificado.
- Área determinada.
- Afinidad clasificada.

No supongas que tienen el mismo denominador.

Calcula los siguientes indicadores nuevos sobre los casos con empleo verificado:

- Empleador identificado: cantidad y porcentaje.
- Cargo identificado: cantidad y porcentaje.
- Ámbito del empleador conocido: cantidad y porcentaje.

Los registros pendientes de revisión no deben contar como cargos identificados de empleo verificado.

## 2. Incorporar menú lateral y secciones

Crea un menú lateral plegable con icono y nombre de sección. Debe destacar la sección activa y tener nombres accesibles cuando esté plegado.

En celular, utiliza un menú desplegable que no tape permanentemente el contenido.

Organiza estas cinco secciones:

### Resumen general

- Universo seleccionado.
- Casos con evidencia laboral.
- Cobertura de información.
- Situación laboral desconocida.
- Estado de la evidencia.

Mantén una jerarquía clara: cobertura como indicador principal; cantidades como contexto. No presentes cobertura y su complemento como hallazgos independientes.

Renombra la tarjeta “Sin información: 74,8 %” a “Situación laboral desconocida”, porque agrupa varios estados. Conserva “Sin información” para el estado específico correspondiente.

### Promociones

- Cantidad de egresados por año de grado.
- Casos con evidencia por promoción.
- Cobertura por promoción.
- Tabla comparativa con orden por año o cobertura.
- Comparación con la cobertura global del mismo corte.

La referencia global es descriptiva, no una meta. No uses semáforos arbitrarios.

### Perfil laboral observado

- Sectores.
- Empleadores.
- Áreas de desempeño.
- Afinidad, mostrando cantidad de afines, denominador conocido y casos desconocidos.
- Ámbito del empleador.

Cambia “¿Se quedan en Tacna?” por “Ámbito del empleador”.

Sustituye “Concentración de la absorción laboral” por un título descriptivo como “Empleadores con mayor presencia en los casos observados”.

### Calidad de información

- Los tres indicadores nuevos de completitud.
- Nivel de confianza de las fuentes.
- Estados de evidencia y registros pendientes de revisión.
- Vacíos de información relevantes.

No inventes puntuaciones de calidad ni fechas de verificación.

### Ayuda y metodología

- Instrucciones de navegación y filtros.
- Definiciones y fórmulas.
- Fuentes y corte.
- Exclusión de segundos grados.
- Afinidad desconocida.
- Diferencia entre cobertura y empleabilidad.
- Limitaciones geográficas.
- Protección de grupos pequeños.

Unifica las referencias a 141 registros y 139 casos analizados. Corrige la mención de 145 registros en la plantilla.

## 3. Mejorar filtros y exploración

Conserva la promoción seleccionada al navegar entre secciones.

Utiliza filtros pertinentes:

- Promoción para resumen y seguimiento.
- Sector y área para perfil laboral.
- Confianza para explorar evidencia y calidad.

Los filtros locales no deben alterar inadvertidamente los indicadores de otras secciones.

Corrige el filtro actual por sector: selecciona únicamente casos con empleo verificado y produce cobertura de 100 % por construcción. En esas selecciones muestra cantidades y distribución laboral; evita presentar ese porcentaje como cobertura de seguimiento.

Incluye:

- Contexto visible de selección y denominador.
- Botón para restablecer filtros.
- Mensajes para selecciones vacías.
- Tablas agregadas coherentes con los gráficos.
- Selección desde gráficos cuando aporte valor y sea accesible.

## 4. Añadir indicaciones y lecturas dinámicas

Cada sección debe tener una descripción breve de su pregunta y propósito.

Añade controles ⓘ junto a indicadores y gráficos para consultar definición, fórmula, denominador y limitación. Deben funcionar con teclado y táctil, no solamente al pasar el cursor.

Mantén visible una advertencia breve:

“Cobertura de información ≠ tasa de empleabilidad”.

Deja la explicación extensa en Ayuda y metodología.

Añade lecturas breves calculadas desde los resultados de la selección. Por ejemplo:

“Esta promoción presenta menor cobertura que el conjunto del corte. Esto no demuestra menor empleabilidad”.

No escribas conclusiones fijas ni deduzcas desempleo, residencia, demanda laboral o causas no sustentadas.

Diferencia fecha de generación del tablero y corte de los datos. La primera no demuestra que la información laboral se haya actualizado.

## 5. Proteger los datos publicados

La implementación actual marca algunos agregados como `suprimido`, pero conserva las cantidades y publica filas individuales seudonimizadas. El navegador recalcula y muestra grupos pequeños.

Corrige la publicación:

- No incluyas filas individuales ni identificadores de egresados en el HTML o JSON públicos.
- Aplica el umbral existente de 5 casos a los detalles publicables.
- No conserves valores protegidos en atributos, tooltips, tablas ocultas o datos embebidos.
- Considera todos los cruces y filtros disponibles.
- Evita que un valor suprimido se reconstruya fácilmente mediante totales o diferencias; utiliza agrupación o supresión complementaria cuando sea necesario.
- Si una selección no puede mostrarse con protección suficiente, explica que el detalle no está disponible.
- No describas los datos seudonimizados como anónimos.

Diseña agregados para las combinaciones de filtros que admita la interfaz. El resultado debe seguir funcionando sin servidor.

La advertencia “leer con cautela” no sustituye la supresión efectiva.

## 6. Diseño y accesibilidad

Conserva la identidad visual del dashboard actual.

Reduce espacios vacíos y paneles excesivamente altos. Prioriza entre 3 y 5 métricas principales por vista, sin llenar espacio con tarjetas redundantes.

Usa gráficos adecuados a cada pregunta, etiquetas legibles y denominadores explícitos. Evita depender exclusivamente del color.

Verifica:

- Computadora y celular.
- Navegación por teclado.
- Foco visible.
- Contraste en ambos temas.
- Menú plegado y desplegado.
- Contenido sin cortes ni desbordamiento horizontal.
- Tablas accesibles y mensajes claros.

## 7. Verificación y entrega

Ejecuta las pruebas existentes y añade comprobaciones significativas para:

- Fórmulas y denominadores.
- Exclusión de segundos grados.
- Afinidad desconocida cuando no hay cargo.
- Filtros y selecciones vacías.
- Consistencia entre tarjetas, gráficos y tablas.
- Ausencia de filas individuales y valores protegidos en los artefactos públicos.
- Generación del tablero desde la semilla.

Para reconstruir con el CSV existente, utiliza:

```powershell
$env:PYTHONPATH = "src"
python -m empleabilidad.modelo
python -m empleabilidad.kpis
python -m empleabilidad.tablero
```

Para ejecutar las pruebas:

```powershell
$env:PYTHONPATH = "src"
python -m pytest tests -q
```

No dependas de la nómina privada: `empleabilidad.pipeline` comienza por la ingesta y puede requerir ese archivo.

Actualiza el README con las secciones, indicadores, reglas y comandos necesarios.

Entrega la implementación y una explicación breve de:

- Qué cambió.
- Qué resultados se verificaron.
- Qué limitaciones permanecen.
- Cómo abrir el dashboard.

No realices cambios ajenos al alcance, no inventes datos y no publiques ni despliegues el proyecto.
