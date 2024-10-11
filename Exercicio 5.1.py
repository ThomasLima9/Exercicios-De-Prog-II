lista = []

while True:
    n = int(input('Digite um numero: '))
    if n >= 0:
        n = int(n)
        lista.append(n)

    else:
        break

print(f'O maior valor é ', max(lista) )
