#Mundo 2
valor = float(input('Informe o valor da casa: \033[32mR$\033[m').strip())
salario = float(input('Informe seu salário: \033[32mR$\033[m').strip())
anos = int(input('Quantos anos de financiamento?').strip())
mensal = valor / (anos * 12)
minímo = salario * 30 / 100
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos,\nA prestação será de {mensal:.2f}')
if mensal >=minímo:
    print('\033[32m✔ \033[mEMPRÉSTIMO aprovado.')
else:
    print('\033[31m🚫 \033[mEMPRÉSTIMO reprovadao.')
# 😭 No 36 Fiquei meio travado
