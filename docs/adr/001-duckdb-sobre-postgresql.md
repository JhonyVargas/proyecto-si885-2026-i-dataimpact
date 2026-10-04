# ADR 001 — DuckDB en lugar de PostgreSQL

**Estado:** aceptada · **Fecha:** 2026-09-20

## Contexto

El informe de factibilidad (FD01) propuso PostgreSQL como almacén. El universo
real del proyecto es de 139 egresados, con cargas semestrales o anuales, y
lecturas exclusivamente analíticas.

## Decisión

Usar DuckDB, embebido en un archivo, como motor del data mart.

## Alternativas descartadas

- **PostgreSQL.** Motor cliente-servidor pensado para escrituras concurrentes.
  Nuestro patrón es carga masiva infrecuente y lectura analítica. Exige un
  servidor encendido, credenciales, backups y un responsable de mantenimiento.
- **SQLite.** Sin problema de escala, pero orientado a filas; DuckDB es columnar
  y está hecho para las agregaciones que domina este proyecto.

## Consecuencias

- El almacén es un archivo: se copia, se adjunta, se versiona si hiciera falta.
- Costo operativo cero. El proyecto sobrevive al egreso del equipo, que es el
  modo habitual de muerte de los proyectos académicos.
- Si la UPT exigiera PostgreSQL, el SQL es estándar y la migración es de
  conector, no de modelo.
