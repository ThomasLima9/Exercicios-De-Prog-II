codigo = int(input('Digite o código do item (1/2/3/4): '))

while codigo < 1 or codigo > 4:
    print('Codigo invalido, digite entre (1/2/3/4)')
    codigo = int(input('Digite o código do item (1/2/3/4): '))

if codigo == 1:
    print('Valor de R$ 2,50 ')

elif codigo == 2:
    print('Valor de R$ 5,00')

elif codigo == 3:
    print('Valor de R$ 7,50')

elif codigo == 4:
    print('Valor de R$ 9,00')

#else:
   # print('Codigo invalido, digite entre (1/2/3/4)')
