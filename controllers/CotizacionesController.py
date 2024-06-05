
from flask import Blueprint, Flask, render_template, request,session,jsonify
from config.db import bd, ma, app
from models.ProductosModels import Productos, ProductoSchema 
from models.ClientesModels import Cliente
from models.VendedoresModels import Vendedor
from models.InformesModels import Informes
import random
from sqlalchemy import desc
ruta_cotizaciones = Blueprint("ruta_cotizaciones", __name__)




@ruta_cotizaciones.route('/cotizaciones')
def EmpresaCotizaciones():
    empresa = session['empresa']
    productos = Productos.query.filter_by(empresa=empresa).all()
    clientes = Cliente.query.filter_by(empresa=empresa).all()
    vendedores = Vendedor.query.filter_by(empresa=empresa).all()

    ultimo_numero_factura = None
    informes = Informes.query.all()
    if informes:
        ultimo_numero_factura = Informes.query.with_entities(Informes.factura).order_by(desc(Informes.id)).first()[0]

    return render_template("cotizaciones.html", productos=productos, clientes=clientes, vendedores=vendedores, ultimo_numero_factura=ultimo_numero_factura)




@ruta_cotizaciones.route('/hacercotizacion', methods=['POST'])
def hacer_cotizacion():
    clienteID = request.json['clienteId']
    vendedorID = request.json['vendedorId']
    carrito = request.json['carrito']
    empresa = request.json['empresa']
    NFactura = float(request.json['Nfactura']) + 1

    try:

        # Actualizar compras del cliente
        cliente = Cliente.query.get(clienteID)
        if cliente:
            cliente.compras += 1
            bd.session.commit()
        else:
            return jsonify({'success': False, 'message': 'El cliente no existe.'})

        # Actualizar ventas del vendedor
        vendedor = Vendedor.query.get(vendedorID)
        if vendedor:
            vendedor.ventas += 1
            bd.session.commit()
        else:
            return jsonify({'success': False, 'message': 'El vendedor no existe.'})
        

        # Actualizar ventas del vendedor
  
        for producto in carrito:
            informe = Informes(
                cliente_id=clienteID,
                vendedor_id=vendedorID,
                producto_id=producto['id'],  # Aquí debes usar el id del producto en el carrito
                cantidad=producto['cantidad'],
                factura=NFactura  ,  # Puedes establecer esto según tus necesidades
                estado='GENERADA',  # Puedes establecer esto según tus necesidades
                empresa=empresa,  # Aquí debes usar el valor correcto
            )
            bd.session.add(informe)
        
        bd.session.commit()

        return jsonify({'success': True, 'message': 'Operaciones realizadas correctamente.'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Error: ' + str(e)})