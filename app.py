import mysql.connector
from flask import jsonify
from flask import Flask, render_template

app = Flask(__name__, template_folder='config/templates', static_folder='config/static')

# Configurar la conexión a la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'innovashop'

# Crear una instancia de conexión a la base de datos
try:
    mysql = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    print("Conexión exitosa a la base de datos MySQL")
except mysql.connector.Error as err:
    print("Error al conectar a la base de datos MySQL:", err)
    mysql = None

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/compras')
def compras():
    return render_template('Pages/compras.html')



@app.route('/productos')
def productos():
    cursor = mysql.cursor(dictionary=True)  # Establece el cursor para que devuelva los resultados como diccionarios
    cursor.execute("SELECT * FROM producto")  # Consulta para seleccionar todos los productos
    productos = cursor.fetchall()  # Recupera todos los productos
    cursor.close()  # Cierra el cursor
    return render_template('Pages/productos.html', productos=productos)  # Renderiza la plantilla con los productos recuperados


@app.route('/clientes')
def clientes():
    return render_template('Pages/clientes.html')

@app.route('/cotizaciones')
def cotizaciones():
    return render_template('Pages/cotizaciones.html')

@app.route('/informes')
def informes():
    cursor = mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informe")
    informes = cursor.fetchall()
    cursor.close()
    return render_template('Pages/informes.html', informes=informes)


@app.route('/vendedores')
def vendedores():
    return render_template('Pages/vendedores.html')

@app.route('/stock')
def stock():
    cursor = mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM stock")
    stock = cursor.fetchall()
    cursor.close()
    return render_template('Pages/stock.html', stock=stock)

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
