from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.InformesModels import Informes, InformeSchema 

Informes_schema = InformeSchema()
Informes_schema = InformeSchema(many=True)

ruta_Informes = Blueprint("ruta_Informes", __name__)

@ruta_Informes.route('/Informes')
def indexInformes():
    informes = Informes.query.all()
    return render_template("Informes.html", informes = informes)

