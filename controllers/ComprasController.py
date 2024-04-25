from flask import Blueprint, Flask, render_template, request, session,redirect,url_for
from config.db import bd, ma, app
from models.ComprasModels import Compra, CompraSchema 

Compras_schema = CompraSchema()
Compras_schema = CompraSchema(many=True)


ruta_Compras = Blueprint("ruta_Compras", __name__)

@ruta_Compras.route('/Compras')
def indexCompras():
    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        compras = Compra.query.all()
        return render_template("Compras.html", compras=compras,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))  



   
    

