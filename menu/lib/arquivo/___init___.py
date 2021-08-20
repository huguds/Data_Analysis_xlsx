import pandas as pd # Importa o Pandas = biblioteca para manipulação e análise de dados
from openpyxl import Workbook # Biblioteca para ler e escrever em arquivo Excel

def acessarArquivo(endereco):
    try:
        excel = pd.read_excel(endereco) # Lê o arquivo excel
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        print('Arquivo encontrado com sucesso')
        return True

def retornarCabecalho(endereco):
    try:
        cab = pd.read_excel(endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        for columns in cab:
            print(columns)
      
def listarElementos(endereco):
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    else:
        print(excel)

# def cadastrar(endereco, nome='desconhecido'):
#     try:
#         excel = pd.read_excel(endereco)
#     except FileNotFoundError:
#         print('Arquivo não encontrado')
#         return False
#     else:
#         # ultimaLinhaNomes = len(excel.Nomes)
#         # print(ultimaLinhaNomes)
#         # excel.Nomes(len) = nome
#         excel.loc[len(excel.Nomes)] = nome
#         print(excel)