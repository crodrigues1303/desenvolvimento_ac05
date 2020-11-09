from flask import Flask
from flask import render_template


app = Flask(__name__)

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