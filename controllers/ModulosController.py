from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app


ruta_Modulos = Blueprint("ruta_Modulos", __name__)

@ruta_Modulos.route('/Modulos')
def indexModulos():
    return render_template("Modulos.html")


@ruta_Modulos.route('/AdminModulos')
def AdminModulos():
    return render_template("Admin/modulosAdmin.html")

