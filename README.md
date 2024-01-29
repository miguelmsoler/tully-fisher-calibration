# Calibracion de Tully-Fisher 

Este repositorio contiene dos scripts de Python relacionados con la calibración y prueba de la relación de Tully-Fisher para galaxias. La relación de Tully-Fisher es una herramienta utilizada en la astronomía para estimar distancias a galaxias en función de su velocidad rotacional y luminosidad.

La calibración se basa en los datos disponibles en [este enlace](https://academic.oup.com/mnras/article/463/4/4052/2646316).

Este código forma parte de un trabajo práctio de Estructura y Dinámica Galáctica, en el Máster Universitario en Astrofísica y Técnicas de Observación en Astronomía de UNIR.

## Scripts Disponibles

### tully_fisher_cal.py

Este script realiza la calibración de la relación de Tully-Fisher utilizando datos de galaxias y ajusta un modelo a los datos para obtener los parámetros de la relación. Aquí están los pasos principales que realiza:

1. Carga los datos de galaxias desde un archivo CSV llamado 'tully_fisher_cal.csv'.
2. Calcula las magnitudes absolutas y la luminosidad de las galaxias.
3. Realiza un ajuste de regresión para obtener los parámetros de la relación de Tully-Fisher.
4. Grafica los datos y el ajuste resultante.
5. Imprime los resultados del ajuste.

### tully_fisher_test.py

Este script permite a los usuarios introducir el nombre de una galaxia y estimar su distancia utilizando la relación de Tully-Fisher. Aquí están los pasos principales que realiza:

1. Lee los datos de galaxias desde un archivo CSV llamado 'tully_fisher_cal.csv'.
2. Pide al usuario el nombre de la galaxia de interés (tiene que estar incluida en los datos del artículo).
3. Encuentra los datos de la galaxia en el archivo.
4. Pide al usuario los parámetros de la relación de Tully-Fisher (alpha y A).
5. Calcula la luminosidad y la distancia estimada para la galaxia.
6. Muestra los resultados y compara la distancia estimada con la distancia conocida en los datos.

## Requisitos

Asegúrate de tener Python y las bibliotecas requeridas instaladas. Puedes instalar las dependencias utilizando el archivo `requirements.txt`.

## Uso

1. Clona este repositorio en tu máquina local.
2. Ejecuta los scripts desde tu terminal o entorno de desarrollo Python.

### Ejemplo de uso (tully_fisher_test.py):

```bash
python tully_fisher_test.py
```
