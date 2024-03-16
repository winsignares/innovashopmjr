from flask import Flask, render_template

app = Flask(__name__, template_folder='config/templates', static_folder='config/static')

@app.route('/')
def login():
    return render_template('login.html')

# Rutas relacionadas con las compras
@app.route('/compras')
def compras():
    return render_template('rolEmpresa/compras.html')

@app.route('/comprasVendedor')
def comprasVendedor():
    return render_template('rolVendedor/compras.html')
# --------------------------------------------------

@app.route('/productosVendedor')
def productosVendedor():
    return render_template('rolVendedor/productos.html')


@app.route('/productos')
def productos():
    return render_template('rolEmpresa/productos.html')



@app.route('/clientesVendedor')
def clientesVendedor():
    return render_template('rolVendedor/clientes.html')


@app.route('/clientes')
def clientes():
    return render_template('rolEmpresa/clientes.html')




@app.route('/cotizaciones')
def cotizaciones():
    return render_template('rolEmpresa/cotizaciones.html')



@app.route('/informes')
def informes():
    return render_template('rolEmpresa/informes.html')



@app.route('/vendedores')
def vendedores():
    return render_template('rolEmpresa/vendedores.html')

@app.route('/stock')
def stock():
    return render_template('rolEmpresa/stock.html')

@app.route('/parametros')
def parametros():
    return render_template('rolEmpresa/parametros.html')

@app.route('/salir')
def salir():
    return render_template('login.html')

@app.route('/mainE')
def mainE():
    return render_template('rolEmpresa/main.html')

@app.route('/mainV')
def mainV():
    return render_template('rolVendedor/main.html')

if __name__ == '__main__':
    app.run(debug=True)
