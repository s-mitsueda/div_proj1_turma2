function calcular_total() {
    // PUXANDO PRODUTOS NO CARRINHO
    produtos = document.getElementsByClassName('produto')

    // CONVERTENDO PRODUTOS EM UMA LISTA
    valor_total = [...produtos]
                    // CALCULANDO VALOR TOTAL POR PRDOUTO
                    .map(produto => {
                        preco = parseFloat(obter_preco(produto))
                        quantidade = parseInt(obter_quantidade(produto))
                        
                        preco_total = preco * quantidade
                        atualizar_preco_total(produto, preco_total)

                        return preco_total
                    })
                    // SOMANDO VALOR TOTAL
                    .reduce((a, b) => a + b, 0)
        
    // REDEFININDO VALOR TOTAL
    document
        .getElementById('carrinho-valor-total')
        .innerText = `R$ ${valor_total.toFixed(2).replace('.', ',')}`
}

function incrementar(codigo) {
    valor_produto = document.querySelector(`.produto[produto_id="${codigo}"] span`)
    valor_atual = parseInt(valor_produto.innerText)

    if(valor_atual < 0) { return }

    valor_produto.innerText = `${valor_atual + 1}`
    calcular_total()
}

function decrementar(codigo) {
    valor_produto = document.querySelector(`.produto[produto_id="${codigo}"] span`)
    valor_atual = parseInt(valor_produto.innerText)

    if(valor_atual < 1) { return }

    valor_produto.innerText = `${valor_atual - 1}`
    calcular_total()
}

function obter_preco(produto) {
    return produto.children[3].innerText.replace('R$ ', '').replace(',', '.')
}

function obter_quantidade(produto) {
    return produto.querySelector('.quantidade span').innerText
}

function atualizar_preco_total(produto, preco_total) {
    produto.querySelector('.total').innerText = `R$ ${preco_total.toFixed(2).replace('.', ',')}`
}

calcular_total()
