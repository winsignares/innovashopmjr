from flask import Blueprint, Flask, render_template, request,session,redirect,url_for
from config.db import bd, ma, app


ruta_Layout = Blueprint("ruta_Layout", __name__)

@ruta_Layout.route('/Layout')
def indexLayout():
    # Verificar si hay una sesión activa
    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        return render_template("layout.html", username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))  

