from config.db import bd, ma, app

class Vendedor(bd.Model):
    __tablename__ = "vendedores"
    id = bd.Column(bd.Integer, primary_key=True)
    identificacion = bd.Column(bd.String(255))
    nombre = bd.Column(bd.String(255))
    telefono = bd.Column(bd.String(255))
    ventas = bd.Column(bd.Integer)

    def __init__(self, identificacion, nombre, telefono, ventas):
        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono
        self.ventas = ventas
       

with app.app_context():
    bd.create_all()

class VendedorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'identificacion', 'nombre', 'telefono', 'ventas')
