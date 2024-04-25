from flask import Blueprint, Flask, jsonify,json, render_template, request, session, redirect,url_for
from config.db import app, bd, ma

from models.ClientesModels import Cliente, ClienteSchema 

Cliente_schema = ClienteSchema()
Cliente_schema = ClienteSchema(many=True)


ruta_Clientes = Blueprint("ruta_Clientes", __name__)

@ruta_Clientes.route('/Clientes')
def indexClientes():
    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        clientes = Cliente.query.all()
        return render_template("Clientes.html", username=username, rol = rol,clientes=clientes)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))  
    


    