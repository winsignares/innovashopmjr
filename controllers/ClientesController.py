from flask import Blueprint, Flask, jsonify,json, render_template, request,session
from config.db import app, bd, ma

from models.ClientesModels import Cliente, ClienteSchema 

Cliente_schema = ClienteSchema()
Cliente_schema = ClienteSchema(many=True)


ruta_Clientes = Blueprint("ruta_Clientes", __name__)


@ruta_Clientes.route('/clientes')
def VendedorCliente():
    empresa = session['empresa']
    clientes = Cliente.query.filter_by(empresa=empresa).all()
    return render_template("clientes.html",clientes=clientes)




@ruta_Clientes.route('/CrearCliente', methods=['POST'])
def CrearCliente():
    try:
        identifi = request.json['iden']
        nombre = request.json['nombre']
        telefono = request.json['telefono']
        empresa = request.json['empresa']


        # Crear el nuevo cliente
        nuevo_cliente = Cliente(identificacion=identifi, nombre=nombre, telefono=telefono,compras=0, empresa=empresa)
        bd.session.add(nuevo_cliente)
        bd.session.commit()

        return "Cliente creado correctamente", 200

    except Exception as e:
        return "Error al crear el cliente: " + str(e), 500







@ruta_Clientes.route('/EliminarCliente', methods=['POST'])
def EliminarVendedor():
    id = request.json['id']
    try:
        cliente = Cliente.query.get(id)
        if cliente:
            bd.session.delete(cliente)
            bd.session.commit()
            return "Producto eliminado correctamente."
        else:
            return "El producto no existe."
    except Exception as e:
        return "Error eliminando producto: " + str(e)
    
    