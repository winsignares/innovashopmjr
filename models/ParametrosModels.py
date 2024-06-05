from config.db import bd, ma, app

class Parametros(bd.Model):
    __tablename__ = "parametros"
    id = bd.Column(bd.Integer, primary_key=True)
    codigo = bd.Column(bd.String(255))
    producto = bd.Column(bd.String(255))
    precio = bd.Column(bd.Float)
    ganancia = bd.Column(bd.Float)
    iva = bd.Column(bd.Float)
    precio_final = bd.Column(bd.Float)
    empresa = bd.Column(bd.String(255))

    def __init__(self, nombre, cotizaciones, clientes, compras, informes, parametros, productos, stock, vendedores, empresa, estado,):
        self.nombre = nombre
        self.cotizaciones = cotizaciones
        self.clientes = clientes
        self.compras = compras
        self.informes = informes
        self.parametros = parametros
        self.productos = productos
        self.stock = stock
        self.vendedores = vendedores
        self.empresa = empresa
        self.estado = estado
    

with app.app_context():
    bd.create_all()

class ParametroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'cotizaciones', 'clientes', 'compras', 'informes', 'parametros', 'productos', 'stock', 'vendedores', 'empresa', 'estado')
