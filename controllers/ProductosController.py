from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.ProductosModels import Productos, ProductoSchema 

Producto_schema = ProductoSchema()
Producto_schema = ProductoSchema(many=True)


ruta_Productos = Blueprint("ruta_Productos", __name__)

@ruta_Productos.route('/Productos')
def indexProductos():
    productos = Productos.query.all()
    return render_template("Productos.html", productos = productos)

