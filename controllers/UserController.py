from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from config.db import bd
from models.UserController import User
from models.EmpresasModels import Empresa
from models.ClientesModels import Cliente
from models.VendedoresModels import Vendedor
from models.InformesModels import Informes
from models.ProductosModels import Productos

ruta_User = Blueprint("ruta_User", __name__)

@ruta_User.route('/Login')
def loginUser():
    return render_template("login.html")

@ruta_User.route('/consultar')
def Consultar():
    return render_template("consultar.html")


@ruta_User.route('/validarUser', methods=['POST'])
def validate_user():
    username = request.json['user']
    password = request.json['password']
    user = User.query.filter_by(nombre=username).first()

    if user:
        if user.contrasena == password:
            # Almacenar información del usuario y de la empresa en la sesión
            session['username'] = username
            session['rol'] = user.rol
            session['empresa'] = user.empresa
            return jsonify({'success': True, 'message': 'Inicio de sesión exitoso.', 'rol': user.rol, 'empresa': user.empresa})
        else:
            return jsonify({'success': False, 'message': 'Contraseña incorrecta.'})
    else:
        return jsonify({'success': False, 'message': 'Usuario no encontrado.'})

@ruta_User.route('/logout')
def logout():
    # Eliminar información del usuario de la sesión
    session.pop('username', None)
    session.pop('rol', None)
    return redirect(url_for('ruta_User.loginUser'))



@ruta_User.route('/CrearAdmin',methods=['POST'])
def CrearAdmin():
    try:
        # Verificar si el usuario "admin" ya existe
        admin_existente = User.query.filter_by(nombre='admin').first()

        # Si el usuario "admin" ya existe, retornar un mensaje indicando que ya está creado
        if admin_existente:
            return "El usuario 'admin' ya está creado."

        # Si el usuario "admin" no existe, crearlo
        admin = User(nombre='admin', contrasena='admin', rol='ADMIN', empresa='')
        bd.session.add(admin)
        bd.session.commit()

        empresa = Empresa(nombre="",cotizaciones=1,clientes=1,compras=1,informes=1,parametros=1,productos=1,stock=1,vendedores=1,empresas=1,estado="",periodo="")
        bd.session.add(empresa)
        bd.session.commit()

        return "Usuario 'admin' creado exitosamente."

    
    except Exception as e:
        return "Error: " + str(e)



@ruta_User.route('/ConsultarCotizacion', methods=['POST'])
def ConsultarCotizacion():
    try:
        # Obtener el número de identificación del cliente desde la solicitud POST
        cliente_id = request.json['cliente_id']

        # Verificar si el usuario existe
        cliente = Cliente.query.filter_by(identificacion=cliente_id).first()

        if cliente:
            # Obtener la información del cliente
            nombre_cliente = cliente.nombre
            identificacion_cliente = cliente.identificacion

            # Obtener la información de la cotización del cliente
            informes = Informes.query.filter_by(cliente_id=cliente.id).all()

            if informes:
                # Inicializar la lista de productos cotizados
                productos_cotizados = []
                
                # Iterar sobre todos los informes del cliente
                for informe in informes:
                    # Obtener el nombre del vendedor que cotizó con el cliente
                    vendedor = Vendedor.query.get(informe.vendedor_id)
                    nombre_vendedor = vendedor.nombre

                    # Obtener los productos cotizados en este informe
                    producto_cotizado = Productos.query.get(informe.producto_id)
                    productos_cotizados.append({
                        'producto': producto_cotizado.producto,
                        'precio': producto_cotizado.precio
                    })

                # Devolver la información como JSON
                return jsonify({
                    'numeroFactura': informe.factura,
                    'nombre_cliente': nombre_cliente,
                    'identificacion_cliente': identificacion_cliente,
                    'nombre_vendedor': nombre_vendedor,
                    'productos_cotizados': productos_cotizados
                })

            else:
                return jsonify({'error': 'No se encontró ninguna cotización para este cliente.'})
        else:
            return jsonify({'error': 'El cliente no existe.'})

    except Exception as e:
        # Devolver un mensaje de error si ocurre alguna excepción
        return jsonify({'error': str(e)})

