from flask import Flask
from flask import url_for, redirect
from flask import request
import pandas as pd

app = Flask(__name__)

serie = pd.read_csv('raissa_carrinho.csv')
print(serie)

@app.route('/')
def carrinhoDeCompras():
    return redirect(url_for("static", filename="formulario.html"))

@app.route('/comprar')
def comprar():
    argumentos = request.args.to_dict()
    result = pd.concat([serie, pd.Series(argumentos).to_frame().T])
    result.to_csv('raissa_carrinho.csv', index=False)

    print(result)
    return redirect(url_for("carrinhoDeCompras"))

@app.route('/listar')
def listar():
    return serie.to_dict()
    #return carrinho

if __name__ == "__main__":
    app.run(debug=True)