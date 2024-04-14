from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/foroul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.secret_key = "41E5653FC7AEB894026D6BB7B2DB7F65902B454945FA8FD65A6327047B5277FB"

bd = SQLAlchemy(app)
ma = Marshmallow(app)
