import os
from datetime import datetime
from time import sleep

os.system("cls")

# (Ettore) lista de produtos cadastrados
produtos = [
    {
        "nome": "Jenipapo",
        "preço": 25
    },
    {
        "nome": "Lichia",
        "preço": 28
    },
    {
        "nome": "Pitaya",
        "preço": 30
    },
    {
        "nome": "Kiwi",
        "preço": 24
    },
    {
        "nome": "Goiaba",
        "preço": 12
    },
    {
        "nome": "Pitanga",
        "preço": 14
    },
    {
        "nome": "Café",
        "preço": 20
    },
]
carrinho = []

# (Ettore) função para listar produtos cadastrados
def lista_produtos():
    print(f"{' Produtos ':=^45}")
    print("")
    if len(produtos) == 0:
        print("Não há produtos cadastrados.")
    else:
        print(f"{'ID':>6} | {'Nome':20} | {'Preço':13}")
        print(f"{'-' * 45}")
        for produto in produtos:
            print(f"{produtos.index(produto):>6} | {produto['nome']:20} | R$ {produto['preço']:<10.2f}")
    print("")

# Tela de abertura do prograna
title1="••• O R G Â N I C O ' S •••"
title2="C o o p e r a t i v a   d e   P r o d u t o r e s"
title3="\033[93m"+"Grupo 2: Beatriz, Câmara, Ettore & Raissa"+"\033[m"
tamanho_linha=73

espaço1=(tamanho_linha-len(title1))//2-3
espaço2=(tamanho_linha-len(title2))//2-3
espaço3=(tamanho_linha-len(title3))//2+1
linha_vazia="|"+" "*(tamanho_linha-2)+"|"

print("-"*tamanho_linha)
print(linha_vazia)
print("|"," "*espaço1, title1," "*espaço1,"|")
print(linha_vazia)
print("|"," "*espaço2, title2," "*espaço2,"|")
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print("|"," "*espaço3, title3," "*espaço3,"|")
print("-"*tamanho_linha)
sleep(8)

# liga / desliga os comandos while 
flag_menu_navegação=True  
flag_menu_cadastro=False     
flag_item_3A=False          
flag_item_3C=False          
flag_menu_vendas=False       
flag_item_4A=False          
flag_item_4C=False          

while flag_menu_navegação:
    os.system("cls")
    data_hora=datetime.now() # Recebe a data e a hora atual

    title1="••• M E N U   D E   N A V E G A Ç Ã O •••"
    title2=""
    tamanho_linha=73 

    qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
    qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

    # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
    espaço1=(tamanho_linha-len(title1))//2-1
    espaço2=(tamanho_linha-len(title2))//2-1
    espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

    print("-"*tamanho_linha)   
    print(" "*espaço1, title1)
    print(" "*espaço2,title2)
    print("-"*tamanho_linha)

    print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

    print("\t\tA ►  CADASTRO")
    print("\t\tB ►  VENDAS")
    print("\n\t\tS ►  S A I R   D O   S I S T E M A")

    opção=input("\n\t\tOpção desejada: ").lower().strip()

    if opção=="a":
        flag_menu_cadastro=True
        flag_menu_vendas=False
    elif opção=="b": 
        flag_menu_cadastro=False
        flag_menu_vendas=True
    elif opção=="s":
        flag_menu_cadastro=False
        flag_menu_vendas=False
        flag_menu_navegação=False

    while flag_menu_cadastro:
        os.system("cls")
        data_hora=datetime.now() # Recebe a data e a hora atual

        title1="••• M Ó D U L O   D E   C A D A S T R O •••"
        title2=""
        tamanho_linha =73 

        qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
        qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

        # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
        espaço1=(tamanho_linha-len(title1))//2-1
        espaço2=(tamanho_linha-len(title2))//2-1
        espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

        print("-"*tamanho_linha)   
        print(" "*espaço1, title1)
        print(" "*espaço2,title2)
        print("-"*tamanho_linha)

        print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

        lista_produtos()

        print("\t\tA ►  Cadastramento de Produtos")
        print("\t\tC ►  Delação de Produtos")
        print("\n\t\tN ►  Voltar ao Menu de Navegação")
        print("\t\tS ►  S A I R   D O   S I S T E M A")

        opção=input("\n\t\tOpção desejada: ").lower().strip()

        if opção=="a":
            flag_item_3A=True
            flag_item_3C=False
            flag_item_4A=False
            flag_item_4C=False
        elif opção=="c": 
            flag_item_3A=False
            flag_item_3C=True
            flag_item_4A=False
            flag_item_4C=False
        elif opção=="n":
            flag_item_3A=False
            flag_item_3C=False
            flag_item_4A=False
            flag_item_4C=False
            flag_menu_cadastro=False
        elif opção=="s":
            flag_item_3A=False
            flag_item_3C=False
            flag_item_4A=False
            flag_item_4C=False
            flag_menu_cadastro=False
            flag_menu_vendas=False
            flag_menu_navegação=False


        while flag_item_3A:
            os.system("cls")
            data_hora=datetime.now() # Recebe a data e a hora atual
            
            title1="••• M Ó D U L O   D E   C A D A S T R O •••"
            title2="••• C A D A S T R A M E N T O   D E   P R O D U T O S •••"
            tamanho_linha =73 

            qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
            qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

            # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
            espaço1=(tamanho_linha-len(title1))//2-1
            espaço2=(tamanho_linha-len(title2))//2-1
            espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

            print("-"*tamanho_linha)   
            print(" "*espaço1, title1)
            print(" "*espaço2,title2)
            print("-"*tamanho_linha)

            print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

            lista_produtos()

            print("\033[;7m"+"\t\tA ►  Cadastramento de Produtos"+"\033[m")
            print("\t\tC ►  Deleção de Produtos")
            
            print()
            cadastrar_alimento = "s"
            while cadastrar_alimento == "s":
                alimento = {
                    "nome": input("Qual alimento gostaria de cadastrar? "),
                    "preço": float(input("Qual o valor do produto? "))
                }
                produtos.append(alimento)
                cadastrar_alimento = input("Deseja cadastrar mais um alimento? / (s ou n) ")

            print("\n\t\tV ►  Voltar ao menu de Cadastro")
            print("\t\tS ►  S A I R   D O   S I S T E M A")

            opção=input("\n\t\tOpção desejada: ").lower().strip()

            if opção=="v": 
                flag_item_3A=False
                flag_item_3C=False
                flag_item_4A=False
                flag_item_4C=False
            elif opção=="s":
                flag_item_3A=False
                flag_item_3C=False
                flag_item_4A=False
                flag_item_4C=False
                flag_menu_cadastro=False
                flag_menu_vendas=False
                flag_menu_navegação=False


        while flag_item_3C:
            os.system("cls")
            data_hora=datetime.now() # Recebe a data e a hora atual

            title1="••• M Ó D U L O   D E   C A D A S T R O •••"
            title2="••• D E L E Ç Ã O   D E   P R O D U T O S •••"
            tamanho_linha =73 

            qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
            qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

            # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
            espaço1=(tamanho_linha-len(title1))//2-1
            espaço2=(tamanho_linha-len(title2))//2-1
            espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

            print("-"*tamanho_linha)   
            print(" "*espaço1, title1)
            print(" "*espaço2,title2)
            print("-"*tamanho_linha)

            print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

            lista_produtos()

            print("\t\tA ►  Cadastramento de Produtos")
            print("\033[;7m"+"\t\tC ►  Deleção de Produtos"+"\033[0;0m")
            print()

            # (Ettore) funcionalidade de deleção/descadastramento de produtos
            id = int(input("Código do produto a ser deletado: "))
            try:
                produtos[id]
            except:
                print("")
                input("Produto com este código não encontrado.")
                flag_item_3C = False
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
                        flag_item_3C = False
                    case _:
                        input("Deleção cancelada.")
                        flag_item_3C = False

            # print("\n\t\tV ►  Voltar ao menu de Cadastro")
            # print("\t\tS ►  S A I R   D O   S I S T E M A")

            # opção=input("\n\t\tOpção desejada: ").lower().strip()

            # if opção=="v": 
            #     flag_item_3A=False
            #     flag_item_3C=False
            #     flag_item_4A=False
            #     flag_item_4C=False                
            # elif opção=="s":
            #     flag_item_3A=False
            #     flag_item_3C=False
            #     flag_item_4A=False
            #     flag_item_4C=False                
            #     flag_menu_cadastro=False
            #     flag_menu_vendas=False
            #     flag_menu_navegação=False


    while flag_menu_vendas:
            os.system("cls")
            data_hora=datetime.now() # Recebe a data e a hora atual

            title1="••• M Ó D U L O   D E   V E N D A S •••"
            title2=""
            tamanho_linha =73 

            qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
            qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

            # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
            espaço1=(tamanho_linha-len(title1))//2-1
            espaço2=(tamanho_linha-len(title2))//2-1
            espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

            print("-"*tamanho_linha)   
            print(" "*espaço1, title1)
            print(" "*espaço2,title2)
            print("-"*tamanho_linha)

            print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

            print("\t\tA ►  Adição de produtos ao carrinho")
            print("\t\tC ►  Finalização da venda do carrinho")
            print("\n\t\tN ►  Voltar ao menu de Navegação")
            print("\t\tS ►  S A I R   D O   S I S T E M A")

            opção=input("\n\t\tOpção desejada: ").lower().strip()

            if opção=="a":
                flag_item_4A=True
                flag_item_4C=False
                flag_item_3A=False
                flag_item_3C=False
            elif opção=="c": 
                flag_item_4A=False
                flag_item_4C=True 
                flag_item_3A=False
                flag_item_3C=False
            elif opção=="n":
                flag_item_4A=False
                flag_item_4C=False
                flag_item_3A=False
                flag_item_3C=False
                flag_menu_vendas=False
            elif opção=="s":
                flag_item_4A=False
                flag_item_4C=False
                flag_item_3A=False
                flag_item_3C=False
                flag_menu_cadastro=False
                flag_menu_vendas=False
                flag_menu_navegação=False

            while flag_item_4A:
                os.system("cls")
                data_hora=datetime.now() # Recebe a data e a hora atual

                title1="••• M Ó D U L O   D E   V E N D A S •••"
                title2="••• A D I Ç Ã O   D E   P R O D U T O S   A O   C A R R I N H O •••"
                tamanho_linha =73 

                qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
                qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

                # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
                espaço1=(tamanho_linha-len(title1))//2-1
                espaço2=(tamanho_linha-len(title2))//2-1
                espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

                print("-"*tamanho_linha)   
                print(" "*espaço1, title1)
                print(" "*espaço2,title2)
                print("-"*tamanho_linha)

                print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

                lista_produtos()

                print("\033[;7m"+"\t\tA ►  Adição de produtos ao carrinho" +"\033[0;0m")
                print("\t\tC ►  Finalização da venda do carrinho")

                #RAISSA
                opcao = 0
                flag_item_4A = True

                while flag_item_4A == True:
                    print('===Carrinho de Compras=== \n')
                    print('1 - Adicionar Item')
                    print('2 - Remover Item')
                    print('3 - Ver itens do carrinho')
                    opcao = int(input('Digite a opção: '))

                    if opcao == 1:
                        produto = produtos[int(input("Digite o ID do produto: "))].copy()
                        produto["quantidade"] = int(input("Digite quantidade: "))
                        carrinho.append(produto)
                        flag_item_4A = False
                        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
                        if menu == 'S':
                            flag_item_4A = True

                    if opcao == 2:
                        for produto in carrinho:
                            print(carrinho.index(produto))
                            print(produto)
                        id = int(input('Digite o ID do produto: '))
                        carrinho.pop(id)
                        flag_item_4A = False
                        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
                        if menu == 'S':
                            flag_item_4A = True

                    if opcao == 3:
                        for produto in carrinho:
                            print(carrinho.index(produto))
                            print(produto)
                        flag_item_4A = False
                        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
                        if menu == 'S':
                            flag_item_4A = True
                # FIM RAISSA #

                print("\n\t\tV ►  Voltar ao menu de Vendas")
                print("\t\tS ►  S A I R   D O   S I S T E M A")

                opção=input("\n\t\tOpção desejada: ").lower().strip()

                if opção=="v": 
                    flag_item_4A=False
                    flag_item_4C=False
                    flag_item_3A=False
                    flag_item_3C=False
                elif opção=="s":
                    flag_item_4A=False
                    flag_item_4C=False
                    flag_item_3A=False
                    flag_item_3C=False
                    flag_menu_cadastro=False
                    flag_menu_vendas=False
                    flag_menu_navegação=False


            while flag_item_4C:
                os.system("cls")
                data_hora=datetime.now() # Recebe a data e a hora atual

                title1="••• M Ó D U L O   D E   V E N D A S •••"
                title2="••• F I N A L I Z A Ç Ã O   D A   V E N D A   D O   C A R R I N H O •••"
                tamanho_linha =73 

                qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
                qtd_caracter_hora=len(data_hora.strftime("%H:%M"))

                # Qtd de aracteres para calcular o posicionamento dos títulos, data e hora
                espaço1=(tamanho_linha-len(title1))//2-1
                espaço2=(tamanho_linha-len(title2))//2-1
                espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

                print("-"*tamanho_linha)   
                print(" "*espaço1, title1)
                print(" "*espaço2,title2)
                print("-"*tamanho_linha)

                print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")

                print("\t\tA ►  Adição de produtos ao carrinho")
                print("\033[;7m"+"\t\tC ►  Finalização da venda do carrinho"+"\033[0;0m")

                print()
                print("\t\t\t"+"••• CARRINHO DE COMPRAS •••")
                print("\t\t"+"-"*42)
                print("\t\tCódigo\tProduto\t  Qtd Comprada\tPreço Unit")

                itens_carrinho=[
                    {"Código":1, "Nome": "Açaí", "Preço": 25.0,"Quantidade": 1},
                    {"Código":2, "Nome": "Lichia", "Preço": 28.0,"Quantidade": 2},
                    {"Código":3, "Nome": "Pitaya", "Preço": 30.0,"Quantidade": 1},
                    {"Código":4, "Nome": "Kiwi", "Preço": 24.0,"Quantidade": 2},
                    {"Código":5, "Nome": "Goiaba", "Preço": 12.0,"Quantidade": 1},
                    {"Código":6, "Nome": "Pitanga", "Preço": 14.0,"Quantidade": 1},
                    {"Código":7, "Nome": "Café", "Preço": 20.0,"Quantidade": 9},]   

                total=0
                for produto in itens_carrinho:
                    codigo = produto["Código"]
                    nome = produto["Nome"]
                    preco = produto["Preço"]
                    quantidade = produto["Quantidade"]
                    total += (preco*quantidade)
                    print(F"\t\t  {codigo}\t{nome}\t       {quantidade}\tR$  {preco:.02f}")

                print("\t\t"+"-"*42)
                print(F"\t\tTotal do carrinho:\t\tR$ {total:.02f}")
                print()

                print("\033[93m \t\tF ►  Finalizar compras do carrinho\033[m")

                print("\t\tV ►  Voltar ao menu de Vendas")
                print("\t\tS ►  S A I R   D O   S I S T E M A")

                opção=input("\n\t\tOpção desejada: ").lower().strip()

                if opção=="f":
                    itens_carrinho=[]

                    msg1="C O M P R A S   R E A L I Z A D A S   C O M  S U C E S S O"
                    msg2="V O C Ê   C O M P R O U :  R$ "
                    msg3="O   C A R I N H O   D E   C O M P R A S   S E R Á   E S V A Z I A D O"
                    msg4="R E T O R N A N D O   A O   M Ó D U L O   D E  V E N D A S"
                    tamanho_linha=73

                    espaço1=(tamanho_linha-len(msg1))//2-1
                    espaço2=(tamanho_linha-len(msg2)-len(str(total)))//2-1
                    espaço3=(tamanho_linha-len(msg3))//2-1
                    espaço4=(tamanho_linha-len(msg4))//2-1

                    sleep(0.5)
                    print("\n","-"*tamanho_linha)
                    sleep(0.5)
                    print(" "*espaço1, "\033[93m", msg1,"\033[m","\n")
                    sleep(0.5)
                    espaço2=" "*espaço2
                    print(F"{espaço2} \033[93m {msg2} {total:.2f} \033[m \n")
                    sleep(0.5)
                    print(" "*espaço3, msg3)
                    sleep(0.5)
                    print(" "*espaço4, msg4)
                    sleep(0.5)
                    print("-"*tamanho_linha)
                    sleep(3.5)

                    flag_item_4A=False
                    flag_item_4C=False
                    flag_item_3A=False
                    flag_item_3C=False

                if opção=="v": 
                    flag_item_4A=False
                    flag_item_4C=False
                    flag_item_3A=False
                    flag_item_3C=False
                elif opção=="s":
                    flag_item_4A=False
                    flag_item_4C=False
                    flag_item_3A=False
                    flag_item_3C=False
                    flag_menu_cadastro=False
                    flag_menu_vendas=False
                    flag_menu_navegação=False

input("\nP R O G R A M A   E N C E R R A D O")
