from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app
from models.StockModels import Stocks, Stockchema 

Stocks_schema = Stockchema()
Stocks_schema = Stockchema(many=True)

ruta_Stock = Blueprint("ruta_Stock", __name__)

@ruta_Stock.route('/Stock')
def indexStock():
    stock = Stocks.query.all()
    return render_template("Stock.html")

@ruta_Stock.route('/EmpresaStock')
def EmpresaStock():
    
    return render_template("Empresas/stockEmpresas.html")