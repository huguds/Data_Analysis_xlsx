from lib.arquivo.___init___ import *
from lib.interface.___init___ import *
from lib.filtro.___init___ import *
from time import sleep

# endArquivo = 'alunos.xlsx'
# endArquivo = "C:/Users/vitin/OneDrive/Área de Trabalho/Estudos - Revisão - Programação/Exercicios - python/Projeto de Análise de Dados/alunos.xlsx"
endArquivo = 'Tabela_alunos.xlsx'
acessarArquivo(endArquivo)
sleep(2)
limparTela()

while True:
    resposta = menu([' Listar alunos(as)',' Filtrar alunos(as)', ' Sair do sistema'])
    if resposta == 1:
        limparTela()
        cabecalho('Listando alunos(as)....')
        sleep(2)
        listarElementos(endArquivo)
    elif resposta == 2:
        limparTela()
        cabecalho('Filtrar elementos')
        sleep(2)
        opc = submenu([' Nomes',' 1° Nota',' 2° Nota',' Média',' Crescente',' Decrescente',' Aprovados',' Reprovados',' Voltar'])
        if opc == 1: 
            limparTela()
            cabecalho('Buscando nomes...') # Filtrar somente os elementos
            sleep(2)
            filtraNomes(endArquivo)
        elif opc == 2:
            limparTela()
            cabecalho('1° Nota') # Exibe 1° nota
            sleep(2)
            filtraNota1(endArquivo)
        elif opc == 3:
            limparTela()
            cabecalho('2° Nota') # Exibe somente a 2° nota
            sleep(2)
            filtraNota2(endArquivo)
        elif opc == 4:
            limparTela()
            cabecalho('Buscando médias...') # Exibe somente as medias
            sleep(2)
            filtraMedia(endArquivo)
        elif opc == 5:
            limparTela()
            cabecalho('Ordernando de forma Crescente...') # Ordena de forma crescente através das médias
            sleep(2)
            ordenarMediaCrescente(endArquivo)
        elif opc == 6:
            limparTela()
            cabecalho('Ordenando de forma Decrescente...') # Ordena de forma Decrescente através das médias
            sleep(2)
            ordenarMediaDecrescente(endArquivo)
        elif opc == 7:
            limparTela()
            cabecalho('Buscando Aprovados...')
            sleep(2)
            aprovados(endArquivo)
        elif opc == 8:
            limparTela()
            cabecalho('Buscando Reprovados...')
            sleep(2)
            reprovados(endArquivo)
        elif opc == 9:
            limparTela()
            cabecalho('Voltando...') # Volta para o menu
            sleep(2)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        sleep(2)
        limparTela() # Comando para limpar o terminal
        break