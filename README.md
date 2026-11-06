# Ejecución Secuencial en Python: Lavado de Ropa

Este proyecto demuestra el funcionamiento de la **ejecución secuencial** en programación simulando el lavado de 3 tandadas de ropa (`Ropa Blanca`, `Ropa de Color` y `Ropa Delicada`). 

Cada tandada tiene un tiempo de espera simulado de **4 segundos**. Al ejecutarse de manera secuencial, cada ciclo debe esperar a que el anterior termine por completo antes de iniciar, sumando un tiempo total aproximado de **12 segundos**.

## Estructura del Proyecto

Asegúrate de que los archivos en tu directorio tengan exactamente estos nombres:

```text
.
├── Secuencial_lavado_ropa.py   # Script en Python con la lógica secuencial
├── docker-compose.yml          # Configuración del contenedor y montaje de volumen
└── README.md                   # Documentación del proyecto
```

## Requisitos Previos

* Tener instalado [Docker](https://docs.docker.com/get-docker/) y **Docker Compose** (incluido en Docker Desktop).

## Cómo ejecutar el script con Docker Compose

1. Abre una terminal (PowerShell, CMD o Bash) y ubícate en la carpeta donde se encuentran los archivos del proyecto.

2. Ejecuta el siguiente comando para descargar la imagen `python:3.11-alpine` (si no la tienes localmente), montar el directorio en `/app` y correr el script:

```bash
docker compose up
```

3. Una vez finalizada la ejecución, puedes eliminar el contenedor residual ejecutando:

```bash
docker compose down
```

## Salida Esperada

En la consola se observará el procesamiento en orden estricto y la medición final con `time.perf_counter()`:

```text
python-app-1  | Lavando Ropa Blanca...
python-app-1  | Ropa Blanca lavada.
python-app-1  | Lavando Ropa de Color...
python-app-1  | Ropa de Color lavada.
python-app-1  | Lavando Ropa Delicada...
python-app-1  | Ropa Delicada lavada.
python-app-1  | Tiempo total de lavado: 12.00 segundos
python-app-1 exited with code 0
```