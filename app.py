from flask import Flask, render_template

app = Flask(__name__, template_folder='config/templates', static_folder='config/static')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/compras')
def compras():
    return render_template('Pages/compras.html')

@app.route('/productos')
def productos():
    return render_template('Pages/productos.html')


@app.route('/clientes')
def clientes():
    return render_template('Pages/clientes.html')


@app.route('/cotizaciones')
def cotizaciones():
    return render_template('Pages/cotizaciones.html')

@app.route('/informes')
def informes():
    return render_template('Pages/informes.html')

@app.route('/vendedores')
def vendedores():
    return render_template('Pages/vendedores.html')

@app.route('/stock')
def stock():
    return render_template('Pages/stock.html')

@app.route('/parametros')
def parametros():
    return render_template('Pages/parametros.html')

@app.route('/salir')
def salir():
    return render_template('login.html')

@app.route('/main')
def mainE():
    return render_template('Pages/main.html')


if __name__ == '__main__':
    app.run(debug=True)
