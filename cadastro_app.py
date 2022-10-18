from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import csv

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

produtos = pd.read_csv("Produtos.csv", index_col="Nome")

@app.route("/")
def menu_inicial():
	"""(em construção) Renderiza a página inicial do programa na rota `/`.
	
	Talvez possa incluir o logo, uma mensagem de boas-vindas, e links para as outras páginas.
	"""
	return redirect('/carrinho')

@app.route("/cadastro/")
def menu_cadastro():
	"""Renderiza a página do menu de cadastro na rota `/cadastro/`.
	
	A página é criada a partir de templates do Flask, com o template base sendo `_menu_cadastro.html`. Ela possui um elemento `<table>` (template `table_produtos.html`), que lista os produtos cadastrados no banco de dados, e elementos `<form>` (template: `form_descadastro.html`), utilizados para adicionar e remover produtos do banco de dados.
	"""

	return render_template("_menu_cadastro.html", produtos=produtos)

@app.route("/cadastro/cadastrar/")
def cadastrar():
	def cadastrar():
	codigo = request.form.get("codigo")
	preço = request.form.get("preço")
	alimento = pd.Series([
        "nome": nome,
        "valor": preço
        "disponível": True,
        "qtd_vendas": 0,
        "valor_vendas": 0])
    n = (pd.concat([produtos,alimento.to_frame[]]))
	return redirect("/")
	

	return redirect(url_for("menu_cadastro"))

@app.route("/cadastro/descadastrar/", methods=["POST"])
def descadastrar():
	"""Remove um produto do banco de dados de produtos cadastrados.
	
	O formulário de descadastro na página `/cadastro/` envia uma request `POST` com o nome do produto a ser descadastrado. `DataFrame.drop()` é usado para remover as informações do produto do banco de dados, e `DataFrame.to_csv()` atualiza o arquivo do banco de dados. Finalmente, retorna para a página `/cadastro/`.
	"""

	produtos.drop(request.form.get("nome_produto"), inplace=True)
	# produtos.to_csv("Produtos.csv")

	return redirect(url_for("menu_cadastro"))

@app.route("/vendas/")
def menu_vendas():
	"""(em construção) Renderiza a página do menu de vendas na rota `/vendas/`.
	
	Talvez a página possa incluir uma lista de produtos atualmente no carrinho, outra de items cadastrados no sistema, e formulários para adicionar produtos ao carrinho, removê-los, mudar a quantidade, finalizar a compra, etc.

	Ainda não tenho certeza se todas estas funcionalidades estarão na mesma página, ou se algumas devem estar em páginas separadas.
	"""

	pass

@app.route("/carrinho", methods=['GET'])
def carrinho():
	def formatar_preco(preco, quantidade):
		total = preco * int(quantidade)

		preco = f'{preco:.02f}'.replace('.', ',')
		preco = f'R$ {preco}'

		return preco, total

	produtos = []

	with open('Carrinho.csv', 'r') as file:
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