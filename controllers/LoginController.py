from flask import Blueprint, Flask, render_template, request,jsonify,session, redirect,url_for
from config.db import bd, ma, app
from models.UserModels import User, UserSchema 

ruta_Login = Blueprint("ruta_Login", __name__)

@ruta_Login.route('/Login')
def indexLogin():
    # Verificar si ya hay una sesión activa
    if 'username' in session:
        return render_template("layout.html")  # Si hay sesión activa, redirigir al usuario a la página de inicio
    else:
        return render_template("login.html")  # Si no hay sesión activa, renderizar la página de inicio de sesión

@ruta_Login.route('/validate_user', methods=['POST'])
def validate_user():
    username = request.json['user']
    password = request.json['password']
    user = User.query.filter_by(nombre=username).first()
    
    if user:
        if user.contraseña == password:
            session['username'] = username  # Establecer la sesión para el usuario
            session['rol'] = user.rol
            return jsonify({'success': True, 'message': 'Inicio de sesión exitoso.'})
        else:
            return jsonify({'success': False, 'message': 'ErrorPass'})
    else:
        return jsonify({'success': False, 'message': 'Usuario no encontrado.' })



@ruta_Login.route('/close_session')
def logout():

    session.pop('username', None) 
    session.pop('role', None)  

    return redirect(url_for('ruta_Login.indexLogin'))