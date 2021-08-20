import os

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c}-{item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

def submenu(lista):
    print('Filtrar elementos')
    i = 1
    for item in lista:
        print(f'{i}-{item}')
        i += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

def limparTela():
    return os.system('cls' if os.name == 'nt' else 'clear')