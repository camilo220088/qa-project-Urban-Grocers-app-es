# QA Project: Urban Grocers App - Kits

Proyecto de automatización de pruebas para la API de Urban Grocers, enfocado en el endpoint de creación de kits (`POST /api/v1/kits`). Las pruebas aplican técnicas de partición de equivalencia y análisis de valores límite (boundary value analysis) sobre el campo `name`, cubriendo 9 casos de prueba entre escenarios positivos y negativos.

## Tecnologías

- Python
- pytest
- requests

## Cómo ejecutar las pruebas

1. Clona el repositorio:
2. Crea y activa un entorno virtual:
3. Instala las dependencias:
4. Actualiza la URL del servidor en `configuration.py` con la URL activa de tu entorno de pruebas.
5. Ejecuta las pruebas:


## Resultados

De los 9 casos de prueba, 4 detectaron inconsistencias entre el comportamiento documentado de la API y su comportamiento real (falta de validación de longitud, tipo de dato y presencia del campo `name`).