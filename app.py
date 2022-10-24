from decimal import Decimal
from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import csv

from secretstorage import Item

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

#Funções
def formatar_preco(preco, quantidade):
		total = preco * int(quantidade)

		preco = f'{preco:.02f}'.replace('.', ',')
		preco = f'R$ {preco}'

		return preco, total


def lerCarrinho(caminho):
	produtos = []
	with open(caminho, 'r', encoding="utf8") as file:
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
			#preco, total_produto = formatar_preco(preco, quantidade)
			total_produto = preco * int(quantidade)

			# ADICIONANDO À LISTA DE PRODUTOS
			produtos.append({
				"codigo": codigo,
				"nome": nome,
				"preco": preco,
				"quantidade": quantidade,
				"total": total_produto 
			})
	return produtos




#Rotas

@app.route("/")
def menu_inicial():
	return redirect('/carrinho')

@app.route("/cadastro/")
def menu_cadastro():
	return render_template("_menu_cadastro.html", produtos=produtos)

@app.route("/cadastro/cadastrar/", methods=["POST"])
def cadastrar():
	global produtos
	n = pd.Series({
		"nome": request.form.get("nome"),
		"valor": request.form.get("valor", type=Decimal).quantize(Decimal("0.00")),
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
	return render_template("_menu_vendas.html", produtos=produtos[produtos["disponivel"] == True])

@app.route("/vendas/comprar")
def comprar():
	produtos = pd.read_csv("produtos.csv").set_index('nome')
	carrinho = lerCarrinho(caminho = 'Carrinho.csv')
	argumentos = request.args.to_dict() #Ler formulario (depois de apertar o botão enviar)
	print(argumentos)

	nome = argumentos['nome'] #pega a chave nome do formulario
	item = {
		'codigo': str(len(carrinho)+1),
		'nome': nome, 
		'preco': str(produtos.loc[nome, 'valor']), 
		'quantidade': argumentos['qtd'], 
		}
	print(item)
	carrinho.append(item)
	#criar um dataframe utilizando o carrinho, lista de dicionarios
	#.drop -> remover coluna total
	#to_csv -> transformar o dataframe para um csv chamado Carrinho.csv
	#index = False -> escrever o csv sem o index
	pd.DataFrame(carrinho)\
	  .drop(columns='total')\
	  .to_csv('Carrinho.csv',index=False)

	return redirect(url_for("menu_vendas"))

@app.route('/vendas/listar')
def listar():
	carrinho = lerCarrinho(caminho = 'Carrinho.csv')

	return carrinho

@app.route("/carrinho", methods=['GET'])
def carrinho():
	carrinho = lerCarrinho(caminho = 'Carrinho.csv')
	print(carrinho)

	#RENDERIZANDO PÁGINA
	return render_template("carrinho.html", produtos=carrinho, aguardando_pagamento=False)

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