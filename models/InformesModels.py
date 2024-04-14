from config.db import bd, ma, app

class Informes(bd.Model):
    __tablename__ = "informes"
    id = bd.Column(bd.Integer, primary_key=True)
    identificacion = bd.Column(bd.String(255))
    nombre = bd.Column(bd.String(255))
    factura = bd.Column(bd.Integer)
    estado = bd.Column(bd.String(255))
    pdf = bd.Column(bd.String(255))

    def __init__(self, identificacion, nombre, factura, pdf):
        self.identificacion = identificacion
        self.nombre = nombre
        self.factura = factura
        self.pdf = pdf
    

with app.app_context():
    bd.create_all()

class InformeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'identificacion', 'nombre', 'factura', 'pdf') 
