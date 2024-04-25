from config.db import bd, ma, app

class User(bd.Model):
    __tablename__ = "User"
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(255))
    contraseña = bd.Column(bd.String(255))
    rol = bd.Column(bd.String(255))

    def __init__(self, nombre, contraseña, rol):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol

def crear_datos_predeterminados():
    if not User.query.first():
        usuarios = [
            User(nombre='Andrade', contraseña='admin123', rol='ADMIN'),
            User(nombre='Olimpica', contraseña='olimpica123', rol='EMPRESA'),
            User(nombre='Andres', contraseña='carlos123', rol='VENDEDOR')
        ]
        bd.session.add_all(usuarios)
        bd.session.commit()

with app.app_context():
    bd.create_all()
    crear_datos_predeterminados()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'contraseña', 'rol')
