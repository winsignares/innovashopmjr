
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app



ruta_cotizaciones = Blueprint("ruta_cotizaciones", __name__)

@ruta_cotizaciones.route('/Cotizaciones')
def indexCotizaciones():
    return render_template("cotizaciones.html")

