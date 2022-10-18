from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import csv

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

produtos = pd.read_csv("Produtos.csv")

@app.route("/cadastrar", methods=["POST","GET"])
def cadastrar():
    codigo = request.form.get("codigo")
    preço = request.form.get("preço")
    alimento = pd.Series([
        "nome": nome,
        "valor": preço
        "disponível": True,
        "qtd_vendas": 0,
        "valor_vendas": 0])
    pd.concat([produtos,alimento])
    return redirect("/")
