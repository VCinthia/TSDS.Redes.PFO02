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
├── servidor.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── global.css
│   └── main.js
├── tareas.db (se genera automáticamente)
└── venv/
```

---

## Instrucciones para ejecutar el proyecto

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno virtual

- En Windows:

```bash
.\venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install flask flask_sqlalchemy flask_bcrypt
```

### 4. Ejecutar la aplicación

```bash
python servidor.py
```

Abrir en el navegador:

```
http://URL local donde la aplicación está corriendo/
```

---

## Pruebas

### Usuario de prueba

```json
Usuario: nombreusuario
Contraseña: 1234
```

### Capturas de pantalla

- Las capturas se incluyen en la carpeta `/capturas/`.

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

## Enlace al repositorio

[TSDS.Redes.PFO02](https://github.com/VCinthia/TSDS.Redes.PFO02)

---

**Materia:** Redes  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Docente:** [Alan Portillo]  
