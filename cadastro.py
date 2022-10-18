from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import csv

request.form.get(produtos)

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

produtos = pd.read_csv("Produtos.csv", index_col="Nome")

@app.route("/cadastrar", methods=["POST","GET"])
def cadastrar():
    codigo= request.form["codigo"]
    preço = request.form["preço"]
    alimento = Alimentos(codigo,alimento,preço)
    return redirect("/")
