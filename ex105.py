def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vário alunos.
    :param *n: uma ou mais notas de alunos(aceita várias)
    :param sit: valor adicional indicando se deve ou não adicionar a situação.
    :return: um dicionário com vária informaçoes sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >=5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(2.5, 8, 3, 9.5, sit=True)
print(resp)