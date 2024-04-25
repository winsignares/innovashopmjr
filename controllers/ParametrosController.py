from flask import Blueprint, Flask, render_template, request,session,redirect,url_for
from config.db import bd, ma, app
from models.ParametrosModels import Parametros, ParametroSchema 

Parametros_schema = ParametroSchema()
Parametros_schema = ParametroSchema(many=True)


ruta_Parametros = Blueprint("ruta_Parametros", __name__)

@ruta_Parametros.route('/Parametros')
def indexParametros():

    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        parametros = Parametros.query.all()
        return render_template("Parametros.html", parametros=parametros,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin')) 
    

