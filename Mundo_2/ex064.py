from time import sleep

print('-'*30)
print('Informe 999 para parar')
print('-'*30)

n = 0
count = 0
numbers_typed = 0

while n != 999:
    n = int(input('Informe um número: '))
    numbers_typed += 1
    count += n

print('OS RESULTADOS A SEGUIR NÃO CONTAM COM O NÚMERO 999')
sleep(2)
print(f'Você digitou {numbers_typed-1} números')
print(f'E a soma entre eles  é {count-999}')
