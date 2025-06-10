# Sistema de Registro de Avistamiento de Aves BirdWatch 🐦

Este proyecto es una aplicación web hecha con Python y Flask para registrar, ordenar y clasificar avistamientos de aves usando estructuras de datos como listas, colas y árboles.

## Estructuras implementadas:
- Listas dinámicas
- Colas FIFO (`deque`)
- Árbol binario de búsqueda

## Cómo ejecutar:

* Descargar el archivo .Zip del repo y descomprimirlo.
* Una vez en abierta la carpeta en vs code desde la teminal ejecutar:
  ```bash
  * python -m venv venv (Crea el Entorno Virutla)
  * venv\Scripts\activate (Activa el Venv previamente creado)
  * pip install flask (instala flask)
  * python run.py (ejecutar la app)
  * Luego abre tu navegador y ve a:  👉 http://127.0.0.1:5000
 
En caso de que se llege a presentar un problema de "Seguridad" porque Windows no deja iniciar el Ven utilizar:  
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

 
