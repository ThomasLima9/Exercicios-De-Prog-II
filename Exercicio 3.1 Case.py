codigo = int(input('Digite o código do item (1/2/3/4): '))


while codigo < 1 or codigo > 4:
    print('Digite um número entre (1/2/3/4)')
    codigo = int(input('Digite o código do item (1/2/3/4): '))

def verifi_cod(codigo):
    match codigo:
        case 1:
            return 'R$ 2,50'
        
        case 2:
            return 'R$ 5,00'
        
        case 3:
            return 'R$ 7,50'
        
        case 4:
            return 'R$ 9,00'

print(verifi_cod(codigo))