def funcao(x):
    return (x**2 + 4) / 5

x = float(input("Digite um número para encontrar o ponto fixo: "))

for t in range(10):
    novo_x = funcao(x)
    print(f'iteração {t+1}: {novo_x}')

    if novo_x == x:
        print(f'{novo_x} é um ponto fixo')
        break
    
    x = novo_x

else:
    print('Não tem ponto fixo')
