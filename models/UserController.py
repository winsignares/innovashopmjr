from config.db import bd, ma, app

class User(bd.Model):
    __tablename__ = "User"
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(255))
    contrasena = bd.Column(bd.String(255))
    rol = bd.Column(bd.String(255))
    empresa = bd.Column(bd.String(255))

    def __init__(self, nombre, contrasena, rol, empresa):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol
        self.empresa = empresa

with app.app_context():
    bd.create_all()
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'contrasena', 'rol','empresa')
