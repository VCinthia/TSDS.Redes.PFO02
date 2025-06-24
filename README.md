# 📌 PFO 2 – Sistema de Gestión de Tareas con API REST

Este proyecto forma parte de la Práctica Formativa Obligatoria N.º 2 de la materia Redes – TSDS.

Desarrollado por: **Cinthia Romina Vota**

---

## Funcionalidad

Se implementa una **API REST con Flask** que permite:

- Registro de usuarios con contraseña hasheada
- Inicio y cierre de sesión con `Flask session`
- Creación y visualización de tareas por usuario
- Persistencia de datos con SQLite
- Interfaz web personalizada para interactuar con la API

---

## Enlace al repositorio

[GitHub Repo](https://github.com/VCinthia/TSDS.Redes.PFO02)

---

## Endpoints de la API

Las rutas disponibles para consumir la API son:

| Método | Ruta                | Descripción                  |
|--------|---------------------|------------------------------|
| POST   | `/registro`         | Registrar usuario            |
| POST   | `/login`            | Iniciar sesión               |
| GET    | `/tareas`           | Listar tareas del usuario    |
| POST   | `/tareas`           | Crear nueva tarea            |
| POST   | `/logout`           | Cerrar sesión                |

> Las rutas requieren sesión activa, excepto `/registro` y `/login`.

Ejemplo de cuerpo para registro/login:

```json
{
  "usuario": "nombreusuario",
  "contraseña": "1234"
}
```

Ejemplo para crear tarea:

```json
{
  "titulo": "Examen",
  "descripcion": "Pendiente"
}
```

---

## Tecnologías utilizadas

- Python 3.13
- Flask
- SQLite
- Flask-Bcrypt
- HTML + CSS (custom)
- JavaScript (fetch)

---

## Estructura del proyecto

```
PFO 02 - REDES/
  ├── instance/
  │ └── tareas.db # Base de datos SQLite (persistencia local)
  │
  ├── screenshot/
  │ └── consola/ # Capturas desde consola (inicio, cierre, creación, etc.)
  │ └── web/ # Capturas desde la interfaz web
  │
  ├── static/
  │ ├── global.css # Estilos globales
  │ ├── style.css # Estilos para la interfaz principal
  │ └── main.js # Funciones JavaScript que interactúan con la API
  │
  ├── templates/
  │ └── index.html # Interfaz HTML principal del sistema
  │
  ├── thunder-client/
  │ ├── thunder-collection_PFO 02.json # Colección de pruebas Thunder Client
  │ └── thunder-collection_postman_PFO 02.json # EColección de pruebas Postman
  │
  ├── venv/ # Entorno virtual de Python
  │
  ├── servidor.py # Código principal de la app Flask (define rutas y lógica)
  ├── requirements.txt # Dependencias del proyecto para pip
  ├── render.yaml # Configuración para despliegue en Render
  └── README.md # Documentación del proyecto
```

---

## Ejecución local

1. Crear y activar entorno virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Instalar dependencias

```bash
pip install -r requirements.txt
```

3. Ejecutar aplicación local

```bash
python servidor.py
```

4. Abrir en el navegador:

```
http://URL local donde la aplicación está corriendo/
```

---

## Versión en línea

- **Deploy Render:** [tsds-redes-pfo02.onrender.com](https://tsds-redes-pfo02.onrender.com/)
- La base de datos se incluye en la carpeta `instance/` y fue cargada al deploy.

---

## Capturas

Las imágenes de prueba están en la carpeta `/screenshot/`.

---

## Thunder Client Collections

Las colecciones tanto para Thunder Client como Postman se encuentran en la carpeta `/thunder-client/`.

---

## Respuestas Conceptuales

### ¿Por qué hashear contraseñas?

Hashear contraseñas protege los datos del usuario ante filtraciones o accesos no autorizados. El hash es irreversible y garantiza que las contraseñas nunca se almacenen en texto plano.

### Ventajas de usar SQLite en este proyecto

- Ligero y simple de configurar
- No requiere servidor adicional
- Ideal para proyectos pequeños
- Persistencia asegurada en archivo `.db`

---

**Materia:** Redes  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Docente:** Alan Portillo
