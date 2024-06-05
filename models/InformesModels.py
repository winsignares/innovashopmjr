from config.db import bd, ma, app

class Informes(bd.Model):
    __tablename__ = "informes"
    id = bd.Column(bd.Integer, primary_key=True)
    cliente_id = bd.Column(bd.Integer, nullable=False)
    vendedor_id = bd.Column(bd.Integer, nullable=False)
    producto_id = bd.Column(bd.Integer, nullable=False)
    cantidad = bd.Column(bd.Integer, nullable=False)
    factura = bd.Column(bd.Integer)
    estado = bd.Column(bd.String(255))
    empresa = bd.Column(bd.String(255))

    def __init__(self, cliente_id, vendedor_id, producto_id, cantidad, factura=None, estado=None, empresa=None):
        self.cliente_id = cliente_id
        self.vendedor_id = vendedor_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.factura = factura
        self.estado = estado
        self.empresa = empresa

class InformeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cliente_id', 'vendedor_id', 'producto_id', 'cantidad', 'factura', 'estado', 'empresa')

with app.app_context():
    bd.create_all()
