import os
from src.utils.logger import Logger
from src.fields_mask import FieldMask
from src.familiar_arrangements import Family

def menus(n: int) -> None:
    match n:
        case 1:
            lines = f"{20*'*'}MENU DE PROBLEMAS{20*'*'}"
            print(lines)
            print("\t[1] - Problema da máscara de campos\n"+
            "\t[2] - Problema dos arranjos familiares\n"+
            "\t[0] - Sair"
            )
            print(len(lines)*"*")
        case 2:
            lines = f"{20*'*'}MENU DE MÁSCARAS{20*'*'}"
            print(lines)
            print("\t[1] - Nome, nome do meio e sobrenome\n"+
            "\t[2] - E-mail\n"+
            "\t[3] - Senha\n"+
            "\t[4] - CPF\n"+
            "\t[5] - Telefone\n"+
            "\t[6] - Data e hora\n"+
            "\t[7] - Número\n\n"+
            "\t[8] - Voltar\n"+
            "\t[0] - Sair"
            )
            print(len(lines)*"*")
        case 3:
            lines = f"{20*'*'}MENU DE ARRANJOS FAMILIARES{20*'*'}"
            print(lines)
            print("\t[1] - Problema A\n"+
            "\t[2] - Problema B\n"+
            "\t[3] - Problema C\n"+
            "\t[4] - Problema D\n"+
            "\t[5] - Problema E\n"+
            "\t[6] - Problema F\n"+
            "\t[7] - Problema G\n\n"+
            "\t[8] - Voltar\n"+
            "\t[0] - Sair"
            )
            print(len(lines)*"*")

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def cli_app():
    # Limpar terminal, deixando somente aplicação
    clear()
    # Menu principal
    menus(1)
    # Opção selecionanda 
    option = input("Digite a operação desejada: ").strip()

    # Verifica se a variável existe e foi atribuido um valor a ela
    if 'option' in locals() and option is not None:
        clear() # limpa terminal para o próximo menu (se houver)

    match option:
        case "1":
            methods = {"1": "first_mid_last_name", "2": "email", "3": "passwd",
                         "4": "cpf", "5": "telephone", "6":"date_time", "7": "real_number"}
            # Menu problema das máscaras
            menus(2)
            option = input("Digite a operação desejada: ").strip()

            # Verifica se a variável existe e foi atribuido um valor a ela
            if 'option' in locals() and option is not None:
                clear() # limpa terminal para o próximo menu
                # Menu voltar para o início
                if option == "8":
                    cli_app()
                # Menu de saída
                elif option == "0":
                    exit()
                # Verifica se a opção digita corresponde a um método/operação da Classe FieldMask
                elif option in methods.keys() and hasattr(FieldMask(), methods[option]):
                    # obtém o método para utilização
                    validator = getattr(FieldMask(), methods[option])
                    # Imprime mensagem ao usuário
                    lines = f"{20*'*'}Máscara de {methods[option].upper()}{20*'*'}"
                    print(lines)
                    while True:
                        print("Digite:\n- Uma entrada para ser validada ou;\n- 'VOLTAR' para ir para o início ou;\n- 'SAIR' para sair do programa. ")
                        inpt = input("----> ")
                        if inpt == "SAIR":
                            clear()
                            exit()
                        if inpt == "VOLTAR":
                            cli_app()
                        result = validator(inpt)
                        if result == True:
                            log.success(f"Entrada \"{inpt}\" válida :)")
                        else:
                            log.warning(f"Entrada \"{inpt}\" inválida! :(")                    
                else:
                    print("Operação inválida!")
            
        case "2":
            methods = {"1": "a", "2": "b", "3": "c",
                         "4": "d", "5": "e", "6":"f", "7": "g"}
            # Menu problema das máscaras
            menus(3)
            option = input("Digite a operação desejada: ").strip()

            # Verifica se a variável existe e foi atribuido um valor a ela
            if 'option' in locals() and option is not None:
                clear() # limpa terminal para o próximo menu
                # Menu voltar para o início
                if option == "8":
                    cli_app()
                # Menu de saída
                elif option == "0":
                    exit()
                # Verifica se a opção digita corresponde a um método/operação da Classe FieldMask
                elif option in methods.keys() and hasattr(Family(), methods[option]):
                    # obtém o método para utilização
                    validator = getattr(Family(), methods[option])
                    # Imprime mensagem ao usuário
                    lines = f"{20*'*'}Arranjo Familiar {methods[option].upper()}{20*'*'}"
                    print(lines)
                    while True:
                        print("Digite:\n- Uma entrada para ser validada ou;\n- 'VOLTAR' para ir para o início ou;\n- 'SAIR' para sair do programa. ")
                        inpt = input("----> ")
                        if inpt == "SAIR":
                            clear() # limpa terminal com a aplicação
                            exit() # finaliza a aplicação
                        if inpt == "VOLTAR":
                            cli_app() # Volta para o menu inicial da aplicação
                        result = validator(inpt) # recebe resultado da validação da entrada
                        if result == True:
                            log.success(f"Entrada \"{inpt}\" válida :)")
                        else:
                            log.warning(f"Entrada \"{inpt}\" inválida! :(")                    
                else:
                    print("Operação inválida!")
        case "0":
            exit()
        case _:
            print("Digite uma opção válida!") 


if __name__ == "__main__":
    log = Logger()
    cli_app()
    