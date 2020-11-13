from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:master4721@localhost/ufc'
db = SQLAlchemy(app)

class ufc(db.Model): 
    __tablename__ = 'apostas'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    valor_aposta = db.Column(db.Float)
    lutador = db.Column(db.String(60))
    def __init__(self, nome, telefone, email, valor_aposta,lutador):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.valor_aposta = valor_aposta
        self.lutador = lutador

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

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        telefone = (request.form.get("telefone"))
        email = (request.form.get("email"))
        valor_aposta = (request.form.get("valor_aposta"))
        lutador = (request.form.get("lutador"))
        if nome:
            f = ufc(nome,telefone,email,valor_aposta,lutador)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("listar"))

@app.route("/listar")
def listar():
    listas = ufc.query.all()
    return render_template("listaaposta.html", ufc=listas)

if __name__ == "__main__":
    app.run(debug=True)

teste = ufc.query.all()