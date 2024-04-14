from config.db import bd, ma, app

class Productos(bd.Model):
    __tablename__ = "productos"
    id = bd.Column(bd.Integer, primary_key=True)
    codigo = bd.Column(bd.String(255))
    imagen = bd.Column(bd.String(255))
    stock = bd.Column(bd.Integer)
    producto = bd.Column(bd.String(255))
    descuento_tiempo = bd.Column(bd.String(255))
    precio = bd.Column(bd.Float)

    def __init__(self, codigo, imagen, stock, producto, informes, descuento_tiempo, precio):
        self.nombre = codigo
        self.imagen = imagen
        self.stock = stock
        self.producto = producto
        self.informes = informes
        self.descuento_tiempo = descuento_tiempo
        self.precio = precio

with app.app_context():
    bd.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'codigo', 'imagen', 'stock', 'producto', 'informes', 'descuento_tiempo', 'precio')
