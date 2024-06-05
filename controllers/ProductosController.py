from flask import Blueprint, Flask, render_template, request, jsonify,session
from config.db import bd, ma, app
from models.ProductosModels import Productos, ProductoSchema 

Producto_schema = ProductoSchema()
Producto_schema = ProductoSchema(many=True)


ruta_Productos = Blueprint("ruta_Productos", __name__)

@ruta_Productos.route('/productos')
def indexProductos():
    productos = Productos.query.all()
    return render_template("productos.html", productos=productos)



@ruta_Productos.route('/CrearProducto', methods=['POST'])
def crear():
    productov = request.json['producto']
    stockv = request.json['stock']
    preciov = request.json['precio']
    empresav = request.json['empresa']
    categoriav = request.json['categoria']
    try:
       
        producto = Productos(codigo='123',stock=stockv,producto=productov,descuento_tiempo=0 ,precio=preciov,empresa=empresav,ganancia=0,iva=0,precioFinal=preciov,categoria=categoriav)

        bd.session.add(producto)
        bd.session.commit()

        return "Producto Creado. ID: {}".format(producto.id)

    except Exception as e:

        return "Error: " + str(e)
    


@ruta_Productos.route('/EliminarProducto', methods=['POST'])
def eliminar():
    id = request.json['id']
    try:
        producto = Productos.query.get(id)
        if producto:
            bd.session.delete(producto)
            bd.session.commit()
            return "Producto eliminado correctamente."
        else:
            return "El producto no existe."
    except Exception as e:
        return "Error eliminando producto: " + str(e)


@ruta_Productos.route('/EditarProducto', methods=['POST'])
def Editar():
    id = request.json['id']
    nombre = request.json['nombre']
    stock = request.json['stock']
    precio = request.json['precio']
    imagen = request.json['imagen']

    try:
        producto = Productos.query.get(id)
        if producto:
            producto.producto = nombre
            producto.stock = stock
            producto.precio = precio
            producto.imagen = imagen

            bd.session.commit()
            return jsonify({'success': True, 'message': 'Producto actualizado correctamente.'})
        else:
            return jsonify({'success': False, 'message': 'El producto no existe.'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Error actualizando producto: ' + str(e)})





@ruta_Productos.route('/EmpresaProductos')
def EmpresaProductos():
    if 'empresa' in session:  # Verifica si la sesión tiene la empresa asociada
        empresa = session['empresa']
        productos = Productos.query.filter_by(empresa=empresa).all()
        return render_template("Empresas/productosEmpresas.html", productos=productos)
    else:
        return "Error: No se ha establecido la empresa en la sesión."




@ruta_Productos.route('/VendedorProductos')
def VendedorProductos():
    empresa = session['empresa']
    productos = Productos.query.filter_by(empresa=empresa).all()
    return render_template("Vendedor/productosVendedor.html",productos=productos)