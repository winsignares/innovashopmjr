from config.db import bd, ma, app

class Empresa(bd.Model):
    __tablename__ = "empresas"  # Nombre de la tabla en la base de datos
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(255))
    cotizaciones = bd.Column(bd.Boolean)
    clientes = bd.Column(bd.Boolean)
    compras = bd.Column(bd.Boolean)
    informes = bd.Column(bd.Boolean)
    parametros = bd.Column(bd.Boolean)
    productos = bd.Column(bd.Boolean)
    stock = bd.Column(bd.Boolean)
    vendedores = bd.Column(bd.Boolean)
    empresas = bd.Column(bd.Boolean)
    estado = bd.Column(bd.String(50))
    periodo = bd.Column(bd.String(50))

    def __init__(self, nombre, cotizaciones, clientes, compras, informes, parametros, productos, stock, vendedores, empresas, estado,periodo):
        self.nombre = nombre
        self.cotizaciones = cotizaciones
        self.clientes = clientes
        self.compras = compras
        self.informes = informes
        self.parametros = parametros
        self.productos = productos
        self.stock = stock
        self.vendedores = vendedores
        self.empresas = empresas
        self.estado = estado
        self.periodo = periodo

with app.app_context():
    bd.create_all()
 
class EmpresaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'cotizaciones', 'clientes', 'compras', 'informes', 'parametros', 'productos', 'stock', 'vendedores', 'empresas', 'estado','periodo')


