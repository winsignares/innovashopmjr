from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.VendedoresModels import Vendedor, VendedorSchema 

Vendedor_schema = VendedorSchema()
Vendedor_schema = VendedorSchema(many=True)


ruta_Vendedores = Blueprint("ruta_Vendedores", __name__)

@ruta_Vendedores.route('/Vendedores')
def indexVendedores():
    vendedores = Vendedor.query.all()
    return render_template("Vendedores.html", vendedores=vendedores)

