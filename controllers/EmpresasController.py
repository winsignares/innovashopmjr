from flask import Blueprint, Flask, jsonify,json, render_template, request
from config.db import app, bd, ma

from models.EmpresasModels import Empresa, EmpresaSchema 

Empresa_schema = EmpresaSchema()
Empresa_schema = EmpresaSchema(many=True)



ruta_Empresas = Blueprint('ruta_Empresas', __name__)

@ruta_Empresas.route('/Empresas')
def inderEmpresa():

    empresas = Empresa.query.all()
    return render_template("empresas.html", empresas=empresas)





@ruta_Empresas.route('/actualizar_empresa', methods=['POST'])
def actualizar_empresa():
    try:
        data = request.json
        
        # Obtener los datos de la solicitud
        empresa_id = data.get('ID')
        modulo = data.get('modulo')
        estado_str = data.get('boolean')  # Obtener el estado como una cadena
        
        if estado_str.lower() == 'true':
                ChngEstado = 0
        else:
                ChngEstado = 1

        empresa = Empresa.query.get(empresa_id)
        
        if empresa:
            nombre_empresa = empresa.nombre
            
            setattr(empresa, modulo, ChngEstado)
            bd.session.commit()

            return "Empresa '{}' actualizada correctamente. ID: {}, MODULO: {}, ESTADO: {}".format(nombre_empresa, empresa_id, modulo, ChngEstado)
        else:
            return "Empresa no encontrada"

    except Exception as e:
        # Manejar otras excepciones no esperadas
        return "Error: " + str(e)



@ruta_Empresas.route('/crear_empresa', methods=['POST'])
def crear_empresa():
    try:
        # Crear una nueva instancia de la clase Empresa con valores predeterminados o nulos
        nueva_empresa = Empresa(nombre='OLIMPICA', cotizaciones=1,clientes=1,compras=1,informes=1,parametros=1,productos=1,stock=1,vendedores=1,empresas=1,estado='ACTIVO')

        # Agregar la nueva empresa a la sesión y confirmar la transacción en la base de datos
        bd.session.add(nueva_empresa)
        bd.session.commit()

        return "Empresa creada correctamente. ID: {}".format(nueva_empresa.id)

    except Exception as e:
        # Manejar otras excepciones no esperadas
        return "Error: " + str(e)
