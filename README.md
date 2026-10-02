E-COMMERCE CON DJANGO

Pequeña plataforma de comercio electrónico (catálogo de productos) que ofrece las siguientes funcionalidades:

Visualización de un listado de productos que incluye imagen, nombre y precio.

Incorporación de nuevos artículos a través de un formulario HTML potenciado con JavaScript, el cual gestiona la carga de la imagen para almacenarla de forma persistente en el backend (base de datos y directorio de archivos).

Tecnologías Utilizadas
Python

-Django

-PostgreSQL

-HTML5

-CSS

-JavaScript

Requisitos Previos
Antes de poner en marcha el proyecto, es indispensable contar con las siguientes herramientas instaladas:

-Python 3.14.x

-Git

-PostgreSQL

Instalación
Primero, instala la versión específica de Python mediante pyenv ejecutando el comando:

pyenv install 3.14.6

A continuación, crea un entorno virtual basado en dicha versión de Python con la instrucción:

pyenv virtualenv 3.14.6 ecommerce
Por último, activa el entorno para el proyecto:

pyenv local ecommerce
Dependencias
Instala los paquetes y librerías necesarios para el funcionamiento del sistema utilizando el archivo requirements.txt mediante el siguiente comando:

pip install -r requirements.txt

Variables de Entorno
Este proyecto requiere de variables de entorno configuradas en un archivo .env. En el repositorio encontrarás una plantilla denominada .env.example que detalla los parámetros requeridos para que redactes tu propio archivo .env de forma local.

Nota: Es fundamental que los datos de acceso especificados en este archivo coincidan exactamente con tu configuración de PostgreSQL para garantizar una conexión exitosa.

Migraciones
Una vez configurado lo anterior, resta aplicar las migraciones de los modelos hacia la base de datos de PostgreSQL (asegúrate de haber creado la base de datos previamente). Ejecuta los comandos:

Bash
python manage.py makemigrations
Y posteriormente:

Bash
python manage.py migrate
Con esto, todas las tablas necesarias quedarán configuradas en la base de datos.

Ejecución
Para finalizar, arranca el servidor de desarrollo de Django con la instrucción:

Bash
python manage.py runserver
El sistema proporcionará una URL para realizar pruebas y validar el funcionamiento de la plataforma; por lo general, la dirección generada será similar a esta:
(http://127.0.0.1:8000/)
