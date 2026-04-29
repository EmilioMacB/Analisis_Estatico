# Pruebas Automatizadas de Buscadores Universitarios

Este proyecto utiliza Selenium, Behave (BDD) y Data-Driven Testing (DDT) para automatizar la búsqueda de términos académicos en Google y en los buscadores internos de distintas universidades (ITESO, UdeG, UNAM).

## Requisitos previos

Para poder ejecutar estas pruebas, necesitas tener instalado lo siguiente en tu sistema:
- Python 3.x
- El navegador Google Chrome
- pip (gestor de paquetes de Python)

## Instalación de dependencias

Abre tu terminal, navega a la carpeta principal de este proyecto y ejecuta los siguientes comandos para instalar las librerías necesarias:

pip install selenium
pip install behave

## Ejecución de las pruebas

Para correr la suite de pruebas completa, asegúrate de estar en el directorio raíz del proyecto (donde se encuentra la carpeta `features`) y ejecuta el siguiente comando en la terminal:

behave

## Notas adicionales

- Se implementó Data-Driven Testing mediante un `Scenario Outline` en el archivo `.feature`.
- Dependiendo de las protecciones anti-bot de los servidores web (especialmente en el caso de la UNAM), es posible que la ejecución sea bloqueada por la página web mediante un TimeoutError o un cierre forzado de la conexión. La lógica de localización e interacción del código está implementada correctamente.
