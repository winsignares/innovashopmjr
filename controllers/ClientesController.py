from flask import Blueprint, Flask, jsonify,json, render_template, request
from config.db import app, bd, ma

from models.ClientesModels import Cliente, ClienteSchema 

Cliente_schema = ClienteSchema()
Cliente_schema = ClienteSchema(many=True)


ruta_Clientes = Blueprint("ruta_Clientes", __name__)

@ruta_Clientes.route('/Clientes')
def indexClientes():
    clientes = Cliente.query.all()
    return render_template("Clientes.html", clientes=clientes)

