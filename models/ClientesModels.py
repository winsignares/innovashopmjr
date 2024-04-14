from config.db import bd, ma, app

class Cliente(bd.Model):
    __tablename__ = "clientes"
    id = bd.Column(bd.Integer, primary_key=True)
    identificacion = bd.Column(bd.String(255))
    nombre = bd.Column(bd.String(255))
    telefono = bd.Column(bd.String(255))
    compras = bd.Column(bd.Integer)

    def __init__(self, identificacion, nombre, telefono, compras):
        self.identificacion = identificacion
        self.cotizaciones = nombre
        self.clientes = telefono
        self.compras = compras
        

with app.app_context():
    bd.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'identificacion', 'nombre', 'telefono', 'compras')
