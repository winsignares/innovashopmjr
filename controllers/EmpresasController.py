from flask import Blueprint, Flask, jsonify,json, render_template, request, jsonify
from config.db import app, bd, ma

from models.EmpresasModels import Empresa, EmpresaSchema
from models.UserController import User

Empresa_schema = EmpresaSchema()
Empresa_schema = EmpresaSchema(many=True)



ruta_Empresas = Blueprint('ruta_Empresas', __name__)

@ruta_Empresas.route('/empresa')
def AdminEmpresa():
    empresa = Empresa.query.all()
    return render_template("empresas.html",empresa=empresa)



@ruta_Empresas.route('/CrearEmpresa', methods=['POST'])
def crearEmpresa():

    nombre = request.json['nombre']
    periodo = request.json['periodo']
    estado = request.json['estado']
    try:    
        empresa = Empresa(nombre=nombre,cotizaciones=1,clientes=1,compras=1,informes=1,parametros=1,productos=1,stock=1,vendedores=1,empresas=1,estado=estado,periodo=periodo)
        bd.session.add(empresa)
        bd.session.commit()

        user = User(nombre=nombre,contrasena='admin',rol='EMPRESA',empresa=nombre)
        bd.session.add(user)
        bd.session.commit()

        return "Empresa Creada. ID: {}".format(empresa.id)

    except Exception as e:

        return "Error: " + str(e)
    


    

@ruta_Empresas.route('/EditarEmpresa', methods=['POST'])
def EditarEmpresa():
    id = request.json['id']
    nombre = request.json['nombre']
    periodo = request.json['periodo']
    estado = request.json['estado']

    try:
        empresa = Empresa.query.get(id)
        if empresa:
            empresa.nombre = nombre
            empresa.periodo = periodo
            empresa.estado = estado

            bd.session.commit()
            return jsonify({'success': True, 'message': 'Empresa actualizado correctamente.'})
        else:
            return jsonify({'success': False, 'message': 'El Empresa no existe.'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Error actualizando Empresa: ' + str(e)})
    

    

@ruta_Empresas.route('/EliminarEmpresa', methods=['POST'])
def EliminarEmpresa():
    id = request.json['id']
    try:
        empresa = Empresa.query.get(id)
        user = User.query.get(id)
        if empresa:
            bd.session.delete(user)
            bd.session.delete(empresa)
            bd.session.commit()
            return "Empresa eliminado correctamente."
        else:
            return "El Empresa no existe."
    except Exception as e:
        return "Error eliminando Empresa: " + str(e)