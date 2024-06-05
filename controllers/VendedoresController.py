from flask import Blueprint, Flask, render_template, request,session
from config.db import bd, ma, app
from models.VendedoresModels import Vendedor, VendedorSchema 
from models.UserController import User
Vendedor_schema = VendedorSchema()
Vendedor_schema = VendedorSchema(many=True)


ruta_Vendedores = Blueprint("ruta_Vendedores", __name__)

@ruta_Vendedores.route('/Vendedores')
def indexVendedores():
    vendedores = Vendedor.query.all()
    return render_template("Vendedores.html")




@ruta_Vendedores.route('/vendedores')
def EmpresasVendedores():
    empresa = session['empresa']
    vendedores = Vendedor.query.filter_by(empresa=empresa).all()
    return render_template("vendedores.html", vendedores=vendedores)




@ruta_Vendedores.route('/CrearVendedor', methods=['POST'])
def crearVendedor():

    identifi = request.json['iden']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    empresa = request.json['empresa']

    try:
       
        producto = Vendedor(identificacion=identifi,nombre=nombre,telefono=telefono,ventas=0,empresa=empresa)
        bd.session.add(producto)
        bd.session.commit()

        user = User(nombre=nombre,contrasena=identifi,rol='VENDEDOR',empresa=empresa)
        bd.session.add(user)
        bd.session.commit()
        return "Producto Creado. ID: {}".format(producto.id)

    except Exception as e:

        return "Error: " + str(e)
    


@ruta_Vendedores.route('/EliminarVendedor', methods=['POST'])
def EliminarVendedor():
    id = request.json['id']
    try:
        producto = Vendedor.query.get(id)
        if producto:
            bd.session.delete(producto)
            bd.session.commit()
            return "Producto eliminado correctamente."
        else:
            return "El producto no existe."
    except Exception as e:
        return "Error eliminando producto: " + str(e)