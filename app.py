from decimal import Decimal
from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import csv

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

df_dtypes = {
	"nome": "string",
	"disponivel": "boolean",
	"qtd_vendas": "int64"}
df_converters = {
	"valor": Decimal,
	"valor_vendas": Decimal}

produtos = pd.read_csv("produtos.csv", dtype=df_dtypes, converters=df_converters)

@app.route("/")
def menu_inicial():
	return redirect('/carrinho')

@app.route("/cadastro/")
def menu_cadastro():
	return render_template("_menu_cadastro.html", produtos=produtos)

@app.route("/cadastro/cadastrar")
def cadastrar():
	global produtos
	n = pd.Series({
		"nome": request.args.get("nome"),
		"valor": request.args.get("valor", type=Decimal).quantize(Decimal("0.00")),
		"disponivel": True,
		"qtd_vendas": 0,
		"valor_vendas": Decimal("0.00")})
	produtos = pd.concat([produtos, n.to_frame().T], ignore_index=True)
	produtos.to_csv("produtos.csv", index=False)

	return redirect(url_for("menu_cadastro"))

@app.route("/cadastro/descadastrar/", methods=["POST"])
def descadastrar():
	produtos.at[request.form.get("id_produto", type=int), "disponivel"] = False
	produtos.to_csv("produtos.csv", index=False)

	return redirect(url_for("menu_cadastro"))

@app.route("/vendas/")
def menu_vendas():
	return render_template("_menu_vendas.html")

@app.route("/vendas/comprar")
def comprar():
	serie = pd.read_csv("carrinho_raissa.csv")

	argumentos = request.args.to_dict()
	result = pd.concat([serie, pd.Series(argumentos).to_frame().T])
	result.to_csv("carrinho_raissa.csv", index=False)

	return redirect(url_for("menu_vendas"))

@app.route('/vendas/listar')
def listar():
	serie = pd.read_csv("carrinho_raissa.csv")

	return serie.to_dict()

@app.route("/carrinho", methods=['GET'])
def carrinho():
	def formatar_preco(preco, quantidade):
		total = preco * int(quantidade)

		preco = f'{preco:.02f}'.replace('.', ',')
		preco = f'R$ {preco}'

		return preco, total

	produtos = []

	with open('Carrinho.csv', 'r', encoding="utf8") as file:
		# LENDO COMO CSV
		carrinho = csv.reader(file, delimiter=',')
		
		# PULANDO HEADER
		next(carrinho, None)

		# PASSANDO POR CADA LINHA DO ARQUIVO
		for produto in carrinho:
			# DEFININDO COLUNAS
			codigo = produto[0]
			nome = produto[1]
			preco = float(produto[2])
			quantidade = produto[3]

			# FORMATANDO PREÇO
			preco, total_produto = formatar_preco(preco, quantidade)

			# ADICIONANDO À LISTA DE PRODUTOS
			produtos.append({
				"codigo": codigo,
				"nome": nome,
				"preco": preco,
				"quantidade": quantidade,
				"total": total_produto 
			})

	#RENDERIZANDO PÁGINA
	return render_template("carrinho.html", produtos=produtos, aguardando_pagamento=False)

@app.route("/carrinho", methods=['POST'])
def efetuar_compra():
	forma_de_pagamento = request.form.get('forma-de-pagamento')
	print(forma_de_pagamento)
	if forma_de_pagamento:
		# LIMPANDO CARRINHO
		with open('Carrinho.csv', 'w') as file:
			file.truncate()
	
		return render_template("carrinho.html", forma_de_pagamento=forma_de_pagamento)
	return redirect(url_for('carrinho'))

@app.route("/carrinho/delete/<int:id>", methods=['POST'])
def deletar_do_carrinho(id):
	# FILTRANDO ID INSERIDO
	df = pd.read_csv('Carrinho.csv')
	df = df[df["Código"] != id]

	# ESCREVENDO NOVA LISTA
	df.to_csv('Carrinho.csv', index=False)
	return redirect(url_for('carrinho'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')