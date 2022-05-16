from datetime import date
nascimento = int(input('Me informe o ano em que nasceu: '))
ano = date.today().year
idade = ano - nascimento
print(f'Você tem agora {idade} anos. Sua classificação é ')
if idade <=9:
    print('\033[34mMIRIM\033[m')
elif  idade <=14:
    print('\033[36mINFANTIL\033[m')
elif  idade <=19:
    print('\033[32mJÚNIOR\033[m')
elif  idade <=25:
    print('\033[33mSÊNIOR\033[m')
elif  idade:
    print('\033[31mMASTER')