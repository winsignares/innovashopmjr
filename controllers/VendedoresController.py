from flask import Blueprint, Flask, render_template, request,session,redirect,url_for
from config.db import bd, ma, app
from models.VendedoresModels import Vendedor, VendedorSchema 

Vendedor_schema = VendedorSchema()
Vendedor_schema = VendedorSchema(many=True)


ruta_Vendedores = Blueprint("ruta_Vendedores", __name__)

@ruta_Vendedores.route('/Vendedores')
def indexVendedores():

    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        vendedores = Vendedor.query.all()
        return render_template("Vendedores.html", vendedores=vendedores,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))



