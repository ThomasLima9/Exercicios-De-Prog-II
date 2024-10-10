numero = int(input('Digite um número para calcular o fatorial: '))
i = 1
fatorial = 1 

while i <= numero:
    fatorial *= i
 #   i += 1 ou i = 1 + i
    i = 1 + i

print(f'O fatorial de {numero} é {fatorial}')