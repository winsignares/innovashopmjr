from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app


ruta_Login = Blueprint("ruta_Login", __name__)

@ruta_Login.route('/Login')
def indexLogin():
 
    return render_template("login.html")

