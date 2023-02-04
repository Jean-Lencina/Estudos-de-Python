from datetime import date

sexo = str(input('Você é homem ou mulher? ')).lower()
if sexo == 'mulher':
    print('Você não precisa se alistar')
    continuar = int(input('Você quer se alistar mesmo assim(digite 1 para sim e 2 para não)? '))
    if continuar == 1:
        altura = float(input('Qual a sua altura(m)? '))
        if altura >= 1.60:
            print('Dirija-se ao Exército Brasileiro para mais informações!')
        else:
            print('Desculpe, mas você não pode se alistar!')
    elif continuar == 2:
        print('Obrigado!')
    else:
        print('Você digitou um número inválido! Tente novamente!')
elif sexo == 'homem':
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if sexo == 'homem' and idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif sexo == 'homem' and idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif sexo == 'homem' and idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Você deveria ter se alistado no ano de {}'.format(ano))
    elif nasc > atual:
        print('Você digitou um ano INVÁLIDO')
else:
    print('ERRO')
