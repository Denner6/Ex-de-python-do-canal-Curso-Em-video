nota1 = float(input('Informe a primeira nota: ').strip())
nota2 = float(input('Informe a segunda nota: ').strip())
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f} o aluno teve média {média:.1f}')
if média < 5.0:
    print('Aluno \033[31mREPROVADO\033[m')
elif 7 > média >=5:
    print('Aluno em \033[33mRECUPERAÇÃO\033[m')
elif média >=7:
    print('Aluno \033[32mAPROVADO')