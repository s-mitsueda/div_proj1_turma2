from datetime import datetime
import os
from re import S
os.system("cls")

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
    title1="••• M E N U   D E   N A V E G A Ç Ã O •••\n"
    title2=" "*73
    title=title1+title2
    print("-"*len(title2))    
    print(title)
    print("-"*len(title2))
    qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
    qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
    qtd_caracter_espaço=len(title2)-(qtd_caracter_data+qtd_caracter_hora)
    print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
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
        title1="\t\t••• M Ó D U L O   D E   C A D A S T R O •••\n"
        title2=""
        title=title1+title2
        print("-"*73)    
        print(title)
        print("-"*73)
        qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
        qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
        qtd_caracter_espaço=73-(qtd_caracter_data+qtd_caracter_hora)
        print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
     
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
            title1="\t\t••• M Ó D U L O   D E   C A D A S T R O •••\n"
            title2="••• C A D A S T R A M E N T O   D E   P R O D U T O S •••"
            title=title1+title2
            print("-"*73)
            print(title)
            print("-"*73)
       
            qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
            qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
            qtd_caracter_espaço=73-(qtd_caracter_data+qtd_caracter_hora)
        
            print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
        
            print("\033[;7m"+"\t\tA ►  Cadastramento de Produtos"+"\033[0;0m")
            print("\t\tC ►  Delação de Produtos")
            
            print()
            cadastrar_alimento = "s"
            alimento = {
            "Nome": "",
            "Código": "",
            "Valor": ""

            }

            alimento ["Nome"] = str(input("Qual alimento gostaria de cadastrar? "))
            alimento ["Código"] = int(input("Qual o código do alimento? "))
            alimento ["Valor"] = float(input("Qual o valor do produto? "))

            while cadastrar_alimento == "s":
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
            title1="\t\t••• M Ó D U L O   D E   C A D A S T R O •••\n"
            title2="••• D E L E Ç Ã O   D E   P R O D U T O S •••"
            title=title1+title2
            print("-"*73)
            print(title)
            print("-"*73)
       
            qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
            qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
            qtd_caracter_espaço=73-(qtd_caracter_data+qtd_caracter_hora)
        
            print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
        
            print("\t\tA ►  Cadastramento de Produtos")
            print("\033[;7m"+"\t\tC ►  Delação de Produtos"+"\033[0;0m")
            
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
            title1="\t\t••• M Ó D U L O   D E   V E N D A S •••\n"
            title2=" "*73
            title=title1+title2
            print("-"*len(title2))    
            print(title)
            print("-"*len(title2))
            qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
            qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
            qtd_caracter_espaço=len(title2)-(qtd_caracter_data+qtd_caracter_hora)
            print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
     
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
                title1="\t\t••• M Ó D U L O   D E   V E N D A S •••\n"
                title2="••• A D I Ç Ã O   D E   P R O D U T O S   A O   C A R R I N H O •••"
                title=title1+title2
                print("-"*len(title2))
                print(title)
                print("-"*len(title2))
       
                qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
                qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
                qtd_caracter_espaço=len(title2)-(qtd_caracter_data+qtd_caracter_hora)
        
                print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
        
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
                title1="\t\t••• M Ó D U L O   D E   V E N D A S •••\n"
                title2="••• F I N A L I Z A Ç Ã O   D E   V E N D A S   D O   C A R R I N H O •••"
                title=title1+title2
                print("-"*len(title2))
                print(title)
                print("-"*len(title2))
       
                qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
                qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
                qtd_caracter_espaço=len(title2)-(qtd_caracter_data+qtd_caracter_hora)
        
                print(data_hora.strftime("%d/%m/%Y")+" "*qtd_caracter_espaço+data_hora.strftime("%H:%M"),"\n")
        
                print("\t\tA ►  Adição de produtos ao carrinho")
                print("\033[;7m"+"\t\tC ►  Finalização da venda do carrinho"+"\033[0;0m")

                print()
                print("********** Câmara: copiar seu código aqui ********** ")
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
print("\nP R O G R A M A   E N C E R R A D O\n")
