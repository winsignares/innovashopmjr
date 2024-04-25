from flask import Blueprint, Flask, jsonify,json, render_template, request,session,redirect,url_for
from config.db import app, bd, ma

from models.EmpresasModels import Empresa, EmpresaSchema 

Empresa_schema = EmpresaSchema()
Empresa_schema = EmpresaSchema(many=True)



ruta_Empresas = Blueprint('ruta_Empresas', __name__)

@ruta_Empresas.route('/Empresas')
def inderEmpresa():
    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        empresas = Empresa.query.all()
        return render_template("empresas.html", empresas=empresas,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))  




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
  
        return "Error: " + str(e)



@ruta_Empresas.route('/crear_empresa', methods=['POST'])
def crear_empresa():
    try:
       
        nueva_empresa = Empresa(nombre='OLIMPICA', cotizaciones=1,clientes=1,compras=1,informes=1,parametros=1,productos=1,stock=1,vendedores=1,empresas=1,estado='ACTIVO')

        bd.session.add(nueva_empresa)
        bd.session.commit()

        return "Empresa creada correctamente. ID: {}".format(nueva_empresa.id)

    except Exception as e:

        return "Error: " + str(e)
