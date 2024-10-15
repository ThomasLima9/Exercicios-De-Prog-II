from math import sin, pi  # Importando o valor de pi para referência

def PI(x):
    return x + sin(x)

# Iniciando com um valor próximo de pi
x = float(input('Digite um numero para a aproximação: '))
print(f'Valor inicial: {x}')
for t in range(10):
    x = PI(x)
    print(f'Iteração {t+1}: x = {x}')

    if x == pi:
        print(f'A iteração {t+1} se aproxima de pi')
        break
else:
    print(f'A iteração {t+1} Não se aproxima de pi')
