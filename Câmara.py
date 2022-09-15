import os
import csv
from re import S
from datetime import datetime
from time import sleep

os.system("cls")

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


os.system("cls")

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

            print("\033[;7m"+"\t\tA ►  Cadastramento de Produtos"+"\033[m")
            print("\t\tC ►  Deleção de Produtos")
            
            print()
            print("********** Beatriz: copiar seu código aqui ********** ")
            print()
                       
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

            print("\t\tA ►  Cadastramento de Produtos")
            print("\033[;7m"+"\t\tC ►  Deleção de Produtos"+"\033[0;0m")
            
            print()
            print("********** Ettore: copiar seu código aqui ********** ")
            print()
                       
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

                print("\033[;7m"+"\t\tA ►  Adição de produtos ao carrinho" +"\033[0;0m")
                print("\t\tC ►  Finalização da venda do carrinho")
                
                print()
                print("********** Raissa: copiar seu código aqui ********** ")
                print()

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

                itens_carrinho=[
                    {"Código":1, "Nome": "Açaí", "Preço": 25.0,"Quantidade": 1},
                    {"Código":2, "Nome": "Lichia", "Preço": 28.0,"Quantidade": 2},
                    {"Código":3, "Nome": "Pitaya", "Preço": 30.0,"Quantidade": 1},
                    {"Código":4, "Nome": "Kiwi", "Preço": 24.0,"Quantidade": 2},
                    {"Código":5, "Nome": "Goiaba", "Preço": 12.0,"Quantidade": 1},
                    {"Código":6, "Nome": "Pitanga", "Preço": 14.0,"Quantidade": 1},
                    {"Código":7, "Nome": "Café", "Preço": 20.0,"Quantidade": 10},]   
                print()
                print("\t\tCARRINHO DE COMPRAS")
                print("\t\t------------------------------------")
                print("\t\tCódigo\tProduto\t\tPreço\tQuantidade")


                total = 0
                for produto in itens_carrinho:
                    codigo = produto['Código']
                    nome = produto['Nome']
                    preco = produto['Preço']
                    quantidade = produto['Quantidade']
                    total += (preco*quantidade)
                    print(f'\t\t{codigo}\t{nome}\t\t{preco}\t{quantidade}')
                
                print(f'Total:\t\t\t\t\t\t{total}')

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


print("\nP R O G R A M A   E N C E R R A D O\n")
