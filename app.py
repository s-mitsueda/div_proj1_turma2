from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("Produtos.csv", index_col="Código")

@app.route("/cadastro/")
def listar():
	return render_template("lista.html", df=df)