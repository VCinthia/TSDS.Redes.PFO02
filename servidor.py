from flask import Flask, request, jsonify, render_template, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "clave-super-secreta"  # Podés usar os.urandom(24) en producción

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modelos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('tareas', lazy=True))

# Crear base de datos
with app.app_context():
    db.create_all()

# Ruta principal que muestra el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint de login (POST /login)
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = Usuario.query.filter_by(usuario=datos.get("usuario")).first()
    if usuario and bcrypt.check_password_hash(usuario.contrasena, datos.get("contraseña")):
        session['usuario'] = usuario.usuario
        return jsonify({"mensaje": f"Bienvenido, {usuario.usuario}"})
    return jsonify({"mensaje": "Credenciales incorrectas"}), 401

# Endpoint de logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)
    return jsonify({"mensaje": "Sesión cerrada"})

# Endpoint para registrar usuarios (POST /registro)
@app.route('/registro', methods=['POST'])
def registrar():
    datos = request.get_json()
    if not datos or not datos.get("usuario") or not datos.get("contraseña"):
        return jsonify({"mensaje": "Faltan datos"}), 400

    if Usuario.query.filter_by(usuario=datos["usuario"]).first():
        return jsonify({"mensaje": "El usuario ya existe"}), 400

    contrasena_hashed = bcrypt.generate_password_hash(datos["contraseña"]).decode('utf-8')
    nuevo_usuario = Usuario(usuario=datos["usuario"], contrasena=contrasena_hashed)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario registrado con éxito"})

# Endpoint para obtener tareas del usuario en sesión
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    usuario_nombre = session.get('usuario')
    if not usuario_nombre:
        return jsonify({"mensaje": "Sesión no iniciada"}), 401

    usuario = Usuario.query.filter_by(usuario=usuario_nombre).first()
    if not usuario:
        return jsonify({"mensaje": "Usuario no válido"}), 404

    tareas = [
        {"titulo": t.titulo, "descripcion": t.descripcion}
        for t in usuario.tareas
    ]
    return jsonify(tareas)

# Endpoint para crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    usuario_nombre = session.get('usuario')
    if not usuario_nombre:
        return jsonify({"mensaje": "Sesión no iniciada"}), 401

    datos = request.get_json()
    titulo = datos.get("titulo")
    descripcion = datos.get("descripcion", "")

    if not titulo:
        return jsonify({"mensaje": "El título es obligatorio"}), 400

    usuario = Usuario.query.filter_by(usuario=usuario_nombre).first()
    if not usuario:
        return jsonify({"mensaje": "Usuario no válido"}), 404

    nueva = Tarea(titulo=titulo, descripcion=descripcion, usuario=usuario)
    db.session.add(nueva)
    db.session.commit()

    return jsonify({"mensaje": "Tarea creada con éxito"})

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
