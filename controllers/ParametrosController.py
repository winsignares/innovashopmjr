from flask import Blueprint, Flask, render_template, request,jsonify,session
from config.db import bd, ma, app
from models.ParametrosModels import Parametros, ParametroSchema 
from models.ProductosModels import Productos

Parametros_schema = ParametroSchema()
Parametros_schema = ParametroSchema(many=True)


ruta_Parametros = Blueprint("ruta_Parametros", __name__)


@ruta_Parametros.route('/parametros')
def EmpresaParametros():
    empresa = session['empresa']
    productos = Productos.query.filter_by(empresa=empresa).all()
    return render_template("parametros.html",productos=productos)


@ruta_Parametros.route('/EditarParametros', methods=['POST'])
def EditarParametros():
    id = request.json['id']
    producto = request.json['producto']
    precio = request.json['precio']
    ganancia = request.json['ganancia']
    iva = request.json['iva']
    PrecioFinal = request.json['PrecioFinal']
    
    try:
        producto = Productos.query.get(id)
        if producto:
            producto.ganancia = ganancia
            producto.iva = iva
            producto.precioFinal = PrecioFinal
            bd.session.commit()

            return jsonify({'success': True, 'message': 'producto actualizado correctamente.'})
        else:
            return jsonify({'success': False, 'message': 'El Empresa no existe.'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Error actualizando Empresa: ' + str(e)})