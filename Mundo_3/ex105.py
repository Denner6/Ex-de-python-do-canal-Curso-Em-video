def notas(*nota, situacao=False):
    """
    -> Função para analizar notas e situação de vários alunos
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param situacao: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    informacoes = {'Total': len(nota), 'Maior': max(nota), 'Menor': min(nota), 'Média': sum(nota) / len(nota)}
    if situacao:
        if informacoes['Média'] <= 5:
            informacoes['Situação'] = 'Ruim'
        elif informacoes['Média'] >= 7:
            informacoes['Situação'] = 'Boa'
        elif 5 <= informacoes['Média'] < 7:
            informacoes['Situação'] = 'Razoável'
    return informacoes


# Main program
print(notas(3.5, 2, 6.5, 2, 7, 4, situacao=False))

