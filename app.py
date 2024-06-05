from flask import Flask, render_template, request, json, jsonify,session,redirect,url_for
from config.db import app


from controllers.ClientesController import ruta_Clientes
from controllers.CotizacionesController import ruta_cotizaciones
from controllers.ComprasController import ruta_Compras
from controllers.InformesController import ruta_Informes
from controllers.ParametrosController import ruta_Parametros
from controllers.ProductosController import ruta_Productos
from controllers.StockController import ruta_Stock
from controllers.VendedoresController import ruta_Vendedores
from controllers.EmpresasController import ruta_Empresas
from controllers.ModulosController import ruta_Modulos
from controllers.UserController import ruta_User

app.register_blueprint(ruta_Clientes, url_prefix="/controller")
app.register_blueprint(ruta_cotizaciones, url_prefix="/controller")
app.register_blueprint(ruta_Compras, url_prefix="/controller")
app.register_blueprint(ruta_Informes, url_prefix="/controller")
app.register_blueprint(ruta_Parametros, url_prefix="/controller")
app.register_blueprint(ruta_Productos, url_prefix="/controller")
app.register_blueprint(ruta_Stock, url_prefix="/controller")
app.register_blueprint(ruta_Vendedores, url_prefix="/controller")
app.register_blueprint(ruta_Empresas, url_prefix="/controller")
app.register_blueprint(ruta_Modulos, url_prefix="/controller")
app.register_blueprint(ruta_User, url_prefix="/controller")



@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        if session['rol'] in ['ADMIN', 'EMPRESA', 'VENDEDOR']:
            return render_template("layout.html")
    return render_template("login.html") 


@app.route('/panel', methods=['GET'])
def panel_admin():
    if 'username' in session and session['rol'] in ['ADMIN', 'EMPRESA', 'VENDEDOR']:
        return render_template("layout.html") 
    else:
        return redirect(url_for('index'))



@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('rol', None)
    return render_template("login.html") 




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    