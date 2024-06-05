from config.db import bd, ma, app

class Stocks(bd.Model):
    __tablename__ = "stock"
    id = bd.Column(bd.Integer, primary_key=True)
    identificacion = bd.Column(bd.String(255))
    nombre = bd.Column(bd.String(255))
    cotizacion = bd.Column(bd.Integer)
    stock = bd.Column(bd.Integer)
    pdf = bd.Column(bd.String(255))
    empresa = bd.Column(bd.String(255))
    def __init__(self, identificacion, nombre, cotizacion, stock, pdf,empresa):
        self.nombre = nombre
        self.identificacion = identificacion
        self.cotizacion = cotizacion
        self.stock = stock
        self.pdf = pdf
        self.empresa = empresa

with app.app_context():
    bd.create_all()

class Stockchema(ma.Schema):
    class Meta:
        fields = ('id', 'identificacion', 'nombre', 'cotizacion', 'stock', 'pdf','empresa')
