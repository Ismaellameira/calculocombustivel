# Programa que calcula o preço do combustivel com desconto.
# Programa pegunta qual combustivel deseja.

c = str(input('Qual combustível deseja?: '))
l = int(input('Quantos litros?: '))

# Preço dos combustiveis por litro

al = 2.5
gas = 1.9

if c =='Alcool' or c == 'alcool':
    if l <= 20:
        desc1 = l * al - (0.03 * l)
        print(f'O seu desconto foi de R$ {desc1}')
    if l > 20:
        desc2 = l * al - (0.2 * l)
        print(f'O seu desconto foi de {desc2}')

elif c == 'Gasolina' or c == 'gasolina':
    if l <= 20:
        desc3 = l * gas - (0.04 * l)
        print(f'O seu desconto foi de {desc3}')
    if l > 20:
        desc4 = l * gas - (0.06 * l)
        print(f'O seu desconto foi de {desc4}')

print('final do programa')