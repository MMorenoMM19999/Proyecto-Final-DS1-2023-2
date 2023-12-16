# PROYECTO CONCESIONARIO-APP - GRUPO G

## Universidad del Valle
### Asignatura: Desarrollo de Software I

### Integrantes: 
- ANDRÉS FELIPE LÓPEZ RODRÍGUEZ - 202128542
- MIGUEL ÁNGEL MORENO ROMERO - 202125737
- JHOIMAR ENRIQUE SILVA TORRES - 202177167
- YHAN CARLOS TRUJILLO CASTRO - 202026415
- KEVIN ALEJANDRO VELEZ AGUDELO - 202123281

### Descarga del proyecto
Se recomienda descargar el proyecto directamente desde la siguiente carpeta de drive: [Descargar Proyecto](https://drive.google.com/drive/folders/1YowBrpQqeAjtT3YJOWzCbJTWIeoDTSeG?usp=sharing)

## Guía de Instalación del proyecto en una máquina local:

1. Descargar e instalar la versión 3.10.0 de Python de 64 bits en: [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)

2. Instalar la libreria virtualenv con el comando: 
pip install virtualenv
Luego inicia sesión con la consola SQL de PostgreSQL o entrar a pgadmin y crear una base de datos con el siguiente comando:
CREATE DATABASE concesionariobd;
o con nombre: concesionariobd

3. Extraer el archivo zip del proyecto

4. Importar la base de datos directamente desde el archivo sql llamado "concesionariobd"

5. Abrir la carpeta concesionario y ejecutar el Command Prompt en esta carpeta y activa el entorno virtual con el comando:
pvenv\Script\activate

*NOTA: este comando es para Windows*

6. Entrar a la carpeta concesionario y editar el archivo settings.py dependiendo del puerto y contraseñas del equipo local.

7. Ejecutar e instalar las librerias necesarias del proyecto con el comando: 
pip install -r requirements.txt

8. Migrar la base de datos con el comando:
python manage.py migrate

9. Crear un superusuario de django con el comando: 
python manage.py createsuperuser
e ingresa los datos que pida la consola. Se recomienda usar usuario admin y con contraseña admin.

10. Iniciar el proyecto con el comando:
 python manage.py runserver


*Nota: Para entrar al sitio web de Superusuario, sobre el enlace de localhost agrega /admin*



