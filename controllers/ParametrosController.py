from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.ParametrosModels import Parametros, ParametroSchema 

Parametros_schema = ParametroSchema()
Parametros_schema = ParametroSchema(many=True)


ruta_Parametros = Blueprint("ruta_Parametros", __name__)

@ruta_Parametros.route('/Parametros')
def indexParametros():
    parametros = Parametros.query.all()
    return render_template("Parametros.html", parametros = parametros)

