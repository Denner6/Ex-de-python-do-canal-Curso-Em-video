larg = float(input('\033[33mLargura da parede: '))
alt = float(input('\033[31mAltura da parede: '))
area = larg * alt
print(f'\033[30mSua parede tem \033[32m{larg} \033[30mx \033[33m{alt}\033[30m e sua área é de \033[33m{area:.2f}m².')
tinta = area / 2
print(f'\033[30mPara pintar essa parede, você precisará de \033[34m{tinta:.2f}L \033[30mde tinta.')