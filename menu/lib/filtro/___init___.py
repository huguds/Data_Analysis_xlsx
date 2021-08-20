import pandas as pd
import numpy as np

def filtraNomes(endereco):
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print ('Arquivo não encontrado')
        return False
    else:
        #print(excel[["Nomes"]].head()) # Retorna os dados da tabela de acordo com o nome passado no colchetes
        print(excel.filter(items=['Nomes'])) # Retorna a tabela de nomes através do método filter()
        return True

def filtraNota1(endereco):
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print ('Arquivo não encontrado')
        return False
    else:
        print(excel[["Nomes","Nota1"]].head())
        return True

def filtraNota2(endereco):
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print ('Arquivo não encontrado')
        return False
    else:
        print(excel[["Nomes","Nota2"]].head())
        return True

def filtraMedia(endereco):
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print ('Arquivo não encontrado')
        return False
    else:
        print(excel[["Nomes","Media"]].head())
        return True

def ordenarMediaCrescente(endereco):
    try:
        excel = pd.read_excel(endereco) # Lê o arquivo excel
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        print(excel.sort_values(["Media"], ascending=[False]))
        return True

def ordenarMediaDecrescente(endereco):
    try:
        excel = pd.read_excel(endereco) # Lê o arquivo excel
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        print(excel.sort_values(["Media"], ascending=[True]))
        return True

def aprovados(endereco): # Função cria uma nova tabela onde os alunos com notas maiores ou igual 7 recebem como resultado = 'Aprovados'
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return False    
    else:
        conditionList = [(excel['Media'] >= 7),(excel['Media'] < 7)]
        choiceList = ['Aprovado','Reprovado']
        excel["Resultado"] = np.select(conditionList, choiceList, default='Not specified')
        print(excel[excel.Resultado == 'Aprovado'])
        return True
        
def reprovados(endereco): # Função cria uma nova tabela onde os alunos com notas menores que 7 recebem como resultado = 'Reprovados'
    try:
        excel = pd.read_excel(endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return False    
    else:
        conditionList = [(excel['Media'] >= 7),(excel['Media'] < 7)]
        choiceList = ['Aprovado','Reprovado']
        excel["Resultado"] = np.select(conditionList, choiceList, default='Not specified')
        print(excel[excel.Resultado == 'Reprovado'])
        return True

# def aprovados(endereco):
#     try:
#         excel = pd.read_excel(endereco)
#     except FileNotFoundError:
#         print('Arquivo não encontrado')
#         return False
#     else:
#         print(excel[excel.Resultado == "Aprovado"])
#         return True

# def reprovados(endereco):
#     try:
#         excel = pd.read_excel(endereco)
#     except FileNotFoundError:
#         print('Arquivo não encontrado')
#         return False
#     else:
#         print(excel[excel.Resultado == "Reprovado"])
#         return True