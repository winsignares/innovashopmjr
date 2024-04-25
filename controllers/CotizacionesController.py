
from flask import Blueprint, Flask, render_template, request, session,redirect,url_for
from config.db import bd, ma, app
from models.ProductosModels import Productos, ProductoSchema 

Producto_schema = ProductoSchema()
Producto_schema = ProductoSchema(many=True)


ruta_cotizaciones = Blueprint("ruta_cotizaciones", __name__)

@ruta_cotizaciones.route('/Cotizaciones')
def indexCotizaciones():
    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        productos = Productos.query.all()
        return render_template("cotizaciones.html", productos=productos,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))  



    
  

