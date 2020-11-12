from flask import Flask
from flask import render_template
from flask import request
from flask import url_for 
from flask import redirect 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://usuario:senha@localhost/ufc'
db = SQLAlchemy(app)

class ufc(db.model): 
    __table__="cliente"
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String)
    email = db.Column(db.String(120))
    valor_aposta = db.Column(db.Integer)
    def __init__(self, nome, telefone, email, valor_aposta):
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.valor_aposta = valor_aposta

    __table="lutadores"
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    def __init__(self,nome):
    self.nome = nome

db.create_all()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/fnurmagomedov")
def fnurmagomedov():
    return render_template("fnurmagomedov.html")

@app.route("/adesanya")
def adesanya():
    return render_template("adesanya.html")

@app.route("/usman")
def usman():
    return render_template("usman.html")

@app.route("/jones")
def jones():
    return render_template("jones.html")

@app.route("/miocic")
def miocic():
    return render_template("miocic.html")

@app.route("/volknovski")
def volknovski():
    return render_template("volknovski.html") 

@app.route("/atleta")
def atleta():
    return render_template("index.html") 

@app.route("/redes-sociais")
def redes():
    return render_template("index.html") 

@app.route("/sobre")
def sobre():
    return render_template("sobre.html") 

@app.route("/aposta")
def aposta():
    return render_template("aposta.html") 

app.run(debug=True)