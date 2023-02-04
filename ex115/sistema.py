from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
        while True:
            try:
                resp1 = str(input('Deseja realizar um novo cadastro? [S/N] '))
            except:
                print('Você digitou um valor inválido')
            if resp1 in 'Ss':
                cabeçalho('NOVO CADASTRO')
                nome = str(input('Nome: '))
                idade = leiaint('Idade: ')
                cadastrar(arq, nome, idade)
            elif resp1 in 'Nn':
                break
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1)
