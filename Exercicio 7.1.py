lista = []

while True:
    n = input('Digite um numero: ')
    if n != '':
        n = int(n)
        lista.append(n)

    else:
        break

print(f'O maior valor é ', max(lista) )
