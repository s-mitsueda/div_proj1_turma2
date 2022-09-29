import os
from datetime import datetime
from time import sleep

os.system("cls")

# liga / desliga os comandos while
programa_ligado = True
opcao_principal = 0    # 0 = nenhum menu, 1 = menu de cadastro,   2 = menu de vendas
opcao_cadastro  = 0    # 0 = nenhum menu, 1 = cadastrar produto,  2 = descadastrar produto
opcao_vendas    = 0    # 0 = nenhum menu, 1 = gerenciar carrinho, 2 = finalizar compra

# (Ettore) lista de produtos cadastrados
produtos = [    {"nome": "Jenipapo","preço": 25},
                {"nome": "Lichia","preço": 28},
                {"nome": "Pitaya","preço": 30},
                {"nome": "Kiwi","preço": 1},
                {"nome": "Goiaba","preço": 12},
                {"nome": "Pitanga","preço": 14},
                {"nome": "Café","preço": 20},]

carrinho = [    {"nome": "Kiwi","preço": 1,"quantidade": 3},
                {"nome": "Café","preço": 20,"quantidade": 10},
                {"nome": "Goiaba","preço": 12,"quantidade": 2},
                {"nome": "Pitanga","preço": 14,"quantidade": 1},]

# (Ettore) função para listar produtos cadastrados
def lista_produtos():
    
    print(F"{'••• LISTA DE PRODUTOS •••':^73}\n{'-'*34:^73}")
    print(F"{'Id':>21}   {'Nome':15}    {'Preço Unit':10}\n{'-'*34:^73}")

    if len(produtos)==0:
        print("Não há produtos cadastrados.")
    else:
        for produto in produtos:
            print(F"{produtos.index(produto):>21}   {produto['nome']:.<18} R$   {produto['preço']:5.2f}")
        print()

# (Ettore) função para sair do programa
def sair():
    super.programa_ligado = False
    super.opcao_principal = 0
    super.opcao_cadastro  = 0
    super.opcao_vendas    = 0

# Tela de abertura do prograna
title1="••• O R G Â N I C O ' S •••"
title2="C o o p e r a t i v a   d e   P r o d u t o r e s"
title3="\033[93m"+"Grupo 2: Beatriz, Câmara, Ettore & Raissa"+"\033[m"
linha=73

espaço1=(linha-len(title1))//2-3
espaço2=(linha-len(title2))//2-3
espaço3=(linha-len(title3))//2+1
linha_vazia="|"+" "*(linha-2)+"|"

print("-"*linha)
print(linha_vazia)
print("|"," "*espaço1, title1," "*espaço1,"|")
print(linha_vazia)
print("|"," "*espaço2, title2," "*espaço2,"|")
for i in range (6): print(linha_vazia)
print("|"," "*espaço3, title3," "*espaço3,"|")
print("-"*linha)
sleep(8)

while programa_ligado:
    os.system("cls")
    data_hora=datetime.now() # Recebe a data e a hora atual

    title1="••• M E N U   D E   N A V E G A Ç Ã O •••"
    title2=""
    linha=73

    print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha}}\n{'-'*linha}")
    print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
    print("\t\tA ►  CADASTRO","\n\t\tB ►  VENDAS","\n\t\tS ►  S A I R   D O   S I S T E M A")
    opção=input("\n\t\tOpção desejada: ").lower().strip()

    if opção=="a":
        opcao_principal = 1
    elif opção=="b": 
        opcao_principal = 2
    elif opção=="s":
        sair()

    while opcao_principal == 1:
        os.system("cls")
        data_hora=datetime.now() # Recebe a data e a hora atual

        title1="••• M Ó D U L O   D E   C A D A S T R O •••"
        title2=""
        linha=73

        print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha}}\n{'-'*linha}")
        print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
        
        print("\t\tA ►  Cadastramento de Produtos","\n\t\tC ►  Deleção de Produtos")
        
        print("\n\t\tN ►  Voltar ao Menu de Navegação","\n\t\tS ►  S A I R   D O   S I S T E M A")
        opção=input("\n\t\tOpção desejada: ").lower().strip()

        if opção=="a":
            opcao_cadastro = 1
        elif opção=="c": 
            opcao_cadastro = 2
        elif opção=="n":
            opcao_cadastro = 0
            opcao_principal = 0
        elif opção=="s":
            sair()


        while opcao_cadastro == 1:
            os.system("cls")
            data_hora=datetime.now() # Recebe a data e a hora atual
            
            title1="••• M Ó D U L O   D E   C A D A S T R O •••"
            title2="\033[;7m••• C A D A S T R A M E N T O   D E   P R O D U T O S •••\033[m"
            linha=73
            
            print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha+8}}\n{'-'*linha}")
            print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
            
            lista_produtos()

            cadastrar_alimento = "s"
            while cadastrar_alimento == "s":
                alimento = {
                    "nome": input("Qual alimento gostaria de cadastrar? "),
                    "preço": float(input("Qual o valor do produto? "))
                }
                produtos.append(alimento)
                cadastrar_alimento = input("Deseja cadastrar mais um alimento? / (s ou n) ")

            print("\n\t\tV ►  Voltar ao menu de Cadastro","\n\t\tS ►  S A I R   D O   S I S T E M A")
            opção=input("\n\t\tOpção desejada: ").lower().strip()

            if opção=="v": 
                opcao_cadastro = 0
            elif opção=="s":
                sair()


        while opcao_cadastro == 2:
            os.system("cls")
            data_hora=datetime.now() # Recebe a data e a hora atual

            title1="••• M Ó D U L O   D E   C A D A S T R O •••"
            title2="\033[;7m••• D E L E Ç Ã O   D E   P R O D U T O S •••\033[m"
            linha=73
            
            print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha+8}}\n{'-'*linha}")
            print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
            
            lista_produtos()

            # (Ettore) funcionalidade de deleção/descadastramento de produtos
            id = int(input("Código do produto a ser deletado: "))
            try:
                produtos[id]
            except:
                print("")
                input("Produto com este código não encontrado.")
                opcao_cadastro = 0
            else:
                print("")
                print(f"{'Nome:':6} {produtos[id]['nome']}")
                print(f"{'Preço:':6} R$ {produtos[id]['preço']:<10.2f}")
                print("")
                confirma = input("Confirma a deleção do produto acima? (s/N) ")
                match confirma.upper():
                    case "S":
                        produtos.pop(id)
                        input("Deleção concluída.")
                    case _:
                        input("Deleção cancelada.")
                opcao_cadastro = 0


    while opcao_principal == 2:
            os.system("cls")
            data_hora=datetime.now() # Recebe a data e a hora atual

            title1="••• M Ó D U L O   D E   V E N D A S •••"
            title2=""
            linha=73

            print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha}}\n{'-'*linha}")
            print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
            
            print("\t\tA ►  Adição de produtos ao carrinho","\n\t\tC ►  Finalização da venda do carrinho")
            print("\n\t\tN ►  Voltar ao menu de Navegação")
            print("\t\tS ►  S A I R   D O   S I S T E M A")

            opção=input("\n\t\tOpção desejada: ").lower().strip()

            if opção=="a":
                opcao_vendas = 1
            elif opção=="c": 
                opcao_vendas = 2
            elif opção=="n":
                opcao_vendas = 0
                opcao_principal = 0
            elif opção=="s":
                sair()

            while opcao_vendas == 1:
                os.system("cls")
                data_hora=datetime.now() # Recebe a data e a hora atual

                title1="••• M Ó D U L O   D E   V E N D A S •••"
                title2="\033[;7m••• A D I Ç Ã O   D E   P R O D U T O S   A O   C A R R I N H O •••\033[0;0m"
                linha=73

                print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha+8}}\n{'-'*linha}")
                print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
                
                lista_produtos()

                #RAISSA
                opcao = 0

                print('===Carrinho de Compras=== \n')
                print('1 - Adicionar Item')
                print('2 - Remover Item')
                print('3 - Ver itens do carrinho')
                opcao = int(input('Digite a opção: '))

                if opcao == 1:
                    produto = produtos[int(input("Digite o ID do produto: "))].copy()
                    produto["quantidade"] = int(input("Digite quantidade: "))
                    carrinho.append(produto)
                    opcao_vendas = 0
                    menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
                    if menu == 'S':
                        opcao_vendas = 1

                if opcao == 2:
                    for produto in carrinho:
                        print(carrinho.index(produto))
                        print(produto)
                    id = int(input('Digite o ID do produto: '))
                    carrinho.pop(id)
                    opcao_vendas = 0
                    menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
                    if menu == 'S':
                        opcao_vendas = 1

                if opcao == 3:
                    for produto in carrinho:
                        print(carrinho.index(produto))
                        print(produto)
                    opcao_vendas = 0
                    menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
                    if menu == 'S':
                        opcao_vendas = 1
                # FIM RAISSA #

                print("\n\t\tV ►  Voltar ao menu de Vendas")
                print("\t\tS ►  S A I R   D O   S I S T E M A")

                opção=input("\n\t\tOpção desejada: ").lower().strip()

                if opção=="v": 
                    opcao_vendas = 0
                elif opção=="s":
                    sair()


            while opcao_vendas == 2:
                os.system("cls")
                data_hora=datetime.now() # Recebe a data e a hora atual

                title1="••• M Ó D U L O   D E   V E N D A S •••"
                title2="\033[;7m••• F I N A L I Z A Ç Ã O   D A   V E N D A   D O   C A R R I N H O •••\033[0;0m"
                linha=73

                print(F"{'-'*linha}\n{title1:^{linha}}\n{title2:^{linha+11}}\n{'-'*linha}")
                print(F"{data_hora.strftime('%d/%m/%Y'):<}{data_hora.strftime('%H:%M'):>{linha-10}}") # 10 > tamanho da data
                
                print(F"{'••• CARRINHO DE COMPRAS •••':^73}\n{'-'*51:^73}")
                print(F"{'Id':>13}   {'Produto':14}   {'Qtd':>3}   {'Preço Unit'}   {'Preço  Tot'}") 
                                               
                total=0
                total_carrinho=0
                for produto in carrinho:
                    id=carrinho.index(produto)
                    nome=produto["nome"]
                    preco=produto["preço"]
                    quantidade=produto["quantidade"]
                    
                    total=(preco*quantidade)
                    total_carrinho +=total
                    print(F"{id:13}   {nome:.<16} {quantidade:>3}   R$ {preco:>7.02f}   R$ {total:>7.02f}")

                print(F"{'-'*51:^73}")
                if len(carrinho)==0:
                    print(F"{'*** Carinho de Compras Vazio ***':^73}\n")
                else:
                    print(F"{'TOTAL DO CARRINHO:':>49}   R$ {total_carrinho:>7.02f}")                
                    print("\n\033[93m \t\tF ►  Finalizar compras do carrinho\033[m")
                
                print("\t\tV ►  Voltar ao menu de Vendas")
                print("\t\tS ►  S A I R   D O   S I S T E M A")

                opção=input("\n\t\tOpção desejada: ").lower().strip()

                if opção=="f":
                    carrinho=[]

                    msg1="C O M P R A S   R E A L I Z A D A S   C O M  S U C E S S O"
                    msg2="V O C Ê   C O M P R O U :  R$ "
                    msg3="O   C A R I N H O   D E   C O M P R A S   S E R Á   E S V A Z I A D O"
                    

                    espaço1=(linha-len(msg1))//2-1
                    espaço2=(linha-len(msg2)-len(str(total)))//2-1
                    espaço3=(linha-len(msg3))//2-1
                    
                    sleep(0.5)
                    print("\n","-"*linha)
                    sleep(0.5)
                    print(" "*espaço1, "\033[93m", msg1,"\033[m","\n")
                    sleep(0.5)
                    espaço2=" "*espaço2
                    print(F"{espaço2} \033[93m {msg2} {total:.2f} \033[m \n")
                    sleep(0.5)
                    print(" "*espaço3, msg3)
                    sleep(0.5)
                    print("-"*linha)
                    sleep(5)

                    opcao_vendas = 0

                if opção=="v": 
                    opcao_vendas = 0
                elif opção=="s":
                    sair()

input("\nP R O G R A M A   E N C E R R A D O")