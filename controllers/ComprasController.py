from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.ComprasModels import Compra, CompraSchema 

Compras_schema = CompraSchema()
Compras_schema = CompraSchema(many=True)


ruta_Compras = Blueprint("ruta_Compras", __name__)

@ruta_Compras.route('/Compras')
def indexCompras():
    compras = Compra.query.all()
    return render_template("Compras.html")

@ruta_Compras.route('/EmpresaCompras')
def EmpresaCompras():
    
    return render_template("Empresas/comprasEmpresas.html")


@ruta_Compras.route('/VendedorCompras')
def VendedorCompras():
    
    return render_template("Vendedor/comprasVendedor.html")