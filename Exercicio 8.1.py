numero = int(input('Digite um numero: '))

primo = None

i = 2

while numero > i:
    if numero % i == 0:
        primo = False
        break
    i = i + 1

else:
    primo = True

if primo == True:
    print(numero,'é primo')

elif primo == False:
    print(numero,'não é primo')
