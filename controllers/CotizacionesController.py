
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.ProductosModels import Productos, ProductoSchema 

Producto_schema = ProductoSchema()
Producto_schema = ProductoSchema(many=True)


ruta_cotizaciones = Blueprint("ruta_cotizaciones", __name__)

@ruta_cotizaciones.route('/Cotizaciones')
def indexCotizaciones():
    productos = Productos.query.all()
    return render_template("cotizaciones.html" , productos = productos)

