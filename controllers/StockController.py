from flask import Blueprint, Flask, render_template, request,session,redirect,url_for
from config.db import bd, ma, app
from models.StockModels import Stocks, Stockchema 

Stocks_schema = Stockchema()
Stocks_schema = Stockchema(many=True)

ruta_Stock = Blueprint("ruta_Stock", __name__)

@ruta_Stock.route('/Stock')
def indexStock():


    if 'username' in session:
        # Si hay una sesión activa, renderizar la página de diseño con el nombre de usuario
        username = session['username']
        rol = session['rol']
        stock = Stocks.query.all()
        return render_template("Stock.html", stock=stock,username=username, rol = rol)
    else:
        # Si no hay una sesión activa, redirigir al usuario al inicio de sesión
        return redirect(url_for('ruta_Login.indexLogin'))  
    



