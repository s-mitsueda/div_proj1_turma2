from flask import Flask, render_template, redirect, request, url_for
import pandas as pd

app = Flask(__name__)

produtos = pd.read_csv("Produtos.csv", index_col="Nome")

@app.route("/cadastro/")
def menu_cadastro():
	return render_template("_menu_cadastro.html", produtos=produtos)

@app.route("/cadastro/descadastrar/", methods=["POST"])
def descadastrar():
	produtos.drop(request.form.get("nome_produto"), inplace=True)
	# produtos.to_csv("Produtos.csv")

	return redirect(url_for("menu_cadastro"))