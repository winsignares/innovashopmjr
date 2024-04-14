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

