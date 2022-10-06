from flask import Flask, render_template, redirect, request, url_for
import pandas as pd

app = Flask(__name__)

produtos = pd.read_csv("Produtos.csv", index_col="Nome")

@app.route("/")
def menu_inicial():
	"""(em construção) Renderiza a página inicial do programa na rota `/`.
	
	Talvez possa incluir o logo, uma mensagem de boas-vindas, e links para as outras páginas.
	"""

	pass

@app.route("/cadastro/")
def menu_cadastro():
	"""Renderiza a página do menu de cadastro na rota `/cadastro/`.
	
	A página é criada a partir de templates do Flask, com o template base sendo `_menu_cadastro.html`. Ela possui um elemento `<table>` (template `table_produtos.html`), que lista os produtos cadastrados no banco de dados, e elementos `<form>` (template: `form_descadastro.html`), utilizados para adicionar e remover produtos do banco de dados.
	"""

	return render_template("_menu_cadastro.html", produtos=produtos)

@app.route("/cadastro/cadastrar/")
def cadastrar():
	"""(em construção) Adiciona um novo produto ao banco de dados de produtos cadastrados.
	
	Lê os valores enviados pelo formulário de cadastro na página `/cadastro/`, os adiciona ao banco de dados, e retorna para a página `/cadastro/`.
	"""

	# inserir código de novo cadastramento aqui

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