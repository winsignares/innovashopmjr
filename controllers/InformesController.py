from flask import Blueprint, Flask, render_template, request, session,redirect,url_for
from config.db import bd, ma, app
from models.InformesModels import Informes, InformeSchema 

Informes_schema = InformeSchema()
Informes_schema = InformeSchema(many=True)

ruta_Informes = Blueprint("ruta_Informes", __name__)

@ruta_Informes.route('/Informes')
def indexInformes():

    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        informes = Informes.query.all()
        return render_template("informes.html", informes=informes,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin')) 

