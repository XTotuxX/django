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

FRONT-END

¿Cómo se lee el archivo que el usuario seleccionó en un ?
R./ Se obtiene mediante document.getElementById('imagen').files[0]. Al subir el archivo a través del elemento con el ID 'imagen', se accede a la propiedad files y se selecciona el primer elemento ([0]) para capturar la imagen seleccionada.

Si ya manda el formulario con JSON.stringify(dataForm), ¿por qué eso no funciona para mandar un archivo?
R./ JSON.stringify no es compatible con el envío de archivos binarios, ya que está diseñado exclusivamente para formatear datos de texto. Para transmitir archivos multimedia junto con los datos, es necesario emplear FormData.

¿Qué objeto de JavaScript se usa en su lugar para armar un cuerpo de petición que incluya archivos?
R./ Se utiliza el objeto FormData, el cual permite empaquetar de forma conjunta todos los campos de texto y los archivos adjuntos (como la imagen) en una constante para luego enviarla a través del método fetch.

Cuando se manda ese objeto en el fetch, ¿hace falta seguir poniendo el header Content-Type: application/json?
R./ Ya no es necesario. Al enviar un objeto FormData en el fetch, el navegador configura automáticamente el encabezado adecuado para datos multiparte. Si se especificara manualmente Content-Type: application/json, se generaría un error de interpretación, ya que el contenido enviado no tiene formato JSON.

BACK-END

Cuando la petición trae un archivo, ¿en qué atributo del request llega ese archivo? (no es en request.body, que es donde leíamos el JSON hasta ahora).
R./ La imagen llega a través del atributo request.FILES, mientras que el resto de los campos de texto del formulario se almacenan en request.POST.

Django necesita saber en qué carpeta del disco guardar los archivos, y con qué URL servirlos después. ¿Qué dos variables de settings.py controlan eso?
R./ Se configuran mediante dos variables específicas:

MEDIA_ROOT: Define la ruta física absoluta en el disco del servidor donde se guardarán los archivos.

MEDIA_URL: Define la ruta pública o URL base a través de la cual los archivos podrán visualizarse desde el navegador.

Si guardan el archivo con las herramientas propias de Django (django.core.files.storage), ¿qué hace esa herramienta por ustedes que tendrían que programar a mano si lo hicieran con Python puro (abrir el archivo, generar un nombre, escribirlo en disco)?
R./ El sistema de almacenamiento integrado de Django automatiza tareas que en Python puro requerirían desarrollo manual, tales como la apertura y escritura de flujos de datos en el disco, y la gestión o generación automática de nombres únicos para evitar sobreescrituras.

Una vez guardada la imagen, ¿qué dato exacto conviene guardar en la fila de la base de datos: la ruta completa del archivo en el disco del servidor, o una ruta relativa? ¿Por qué la respuesta importa si algún día cambian de servidor?
R./ Es preferible almacenar una ruta relativa. Esto es fundamental porque si el proyecto cambia de servidor o de directorio de instalación, las rutas absolutas dejarían de ser válidas y romperían los enlaces, mientras que las rutas relativas se mantienen funcionales independientemente de la ubicación física del entorno.
