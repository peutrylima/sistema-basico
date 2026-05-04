from biblioteca import *
from arquivo import *

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
