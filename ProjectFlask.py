from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def Inicio():
    return render_template("Inicio.html")

@app.route("/Pagina1")
def Pagina1():
    return render_template("Pagina1.html")

@app.route("/Gatos")
def Gatos():
    return render_template("Gatos.html")

@app.route("/Cachorros")
def Cachorros():
    return render_template("Cachorros.html")

@app.route("/<x>")
def Nome(x):
    return render_template("Nome.html", x=x)

if __name__ == "__main__":
    app.run(debug=True)
