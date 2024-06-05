from config.db import bd, ma, app

class Compra(bd.Model):
    __tablename__ = "compras"
    id = bd.Column(bd.Integer, primary_key=True)
    codigo = bd.Column(bd.String(255))
    nombre = bd.Column(bd.String(255))
    cotizacion = bd.Column(bd.Integer)
    stock = bd.Column(bd.Integer)
    detalles = bd.Column(bd.String(255))
    empresa = bd.Column(bd.String(255))
    def __init__(self, codigo, nombre, clientes, cotizacion, stock, detalles,empresa):
        self.codigo = codigo
        self.nombre = nombre
        self.clientes = clientes
        self.cotizacion = cotizacion
        self.stock = stock
        self.detalles = detalles
        self.empresa =empresa
        
      

with app.app_context():
    bd.create_all()

class CompraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'codigo', 'nombre', 'clientes', 'cotizacion', 'stock', 'detalles','empresa')
