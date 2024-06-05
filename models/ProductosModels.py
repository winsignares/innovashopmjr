from config.db import bd, ma, app

class Productos(bd.Model):
    __tablename__ = "productos"
    id = bd.Column(bd.Integer, primary_key=True)
    codigo = bd.Column(bd.String(255))
    stock = bd.Column(bd.Integer)
    producto = bd.Column(bd.String(255))
    descuento_tiempo = bd.Column(bd.String(255))
    precio = bd.Column(bd.Float)
    empresa = bd.Column(bd.String(255))
    ganancia = bd.Column(bd.Integer)
    iva = bd.Column(bd.Integer)
    precioFinal =  bd.Column(bd.Float)
    categoria =  bd.Column(bd.String(255))


    def __init__(self, codigo,  stock, producto,descuento_tiempo, precio, empresa,ganancia,iva,precioFinal,categoria):
        self.nombre = codigo
        self.stock = stock
        self.producto = producto
        self.descuento_tiempo = descuento_tiempo
        self.precio = precio
        self.ganancia = ganancia
        self.iva = iva
        self.empresa = empresa
        self.precioFinal = precioFinal
        self.categoria = categoria
    
with app.app_context():
    bd.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'codigo', 'stock', 'producto',  'descuento_tiempo', 'precio','empresa','ganancia','iva','precioFinal','categoria')
