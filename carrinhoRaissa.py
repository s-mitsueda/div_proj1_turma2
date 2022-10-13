import os
produtos = (
    {'id': 1, 'nome': 'Jenipapo', 'preco': 25.0},
    {'id': 2, 'nome': 'Lichia', 'preco': 28.0},
    {'id': 3, 'nome': 'Pitaya', 'preco': 30.0},
    {'id': 4, 'nome': 'Kiwi', 'preco': 24.0},
    {'id': 5, 'nome': 'Goiaba', 'preco': 12.0},
    {'id': 6, 'nome': 'Pitanga', 'preco': 14.0},
    {'id': 7, 'nome': 'Café', 'preco': 20.0}
)

carrinho = []


def exibirOpcoes():
    print('\n\n')
    print('1 - Adicionar Item')
    print('2 - Exibir itens e o valor total')
    print('3 - Limpar Carrinho de compras')
    


def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'], p['nome'], p['preco']))


opcao = '1'

os.system('clear')
print('Carrinho de Compras \n')


def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome']


while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')

    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o identificador do produto: '))
        quantidade = int(input('Digite quantidade: '))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                        (produto['preco'] * item['quantidade'])
                    break

            print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))

    if opcao == '3':
        carrinho = []