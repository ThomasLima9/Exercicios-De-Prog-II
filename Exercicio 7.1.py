m = 0  # Inicializa a variável 'm' com 0. 'm' armazenará o maior número inserido pelo usuário.

# Solicita ao usuário que insira um número
numero = int(input('Digite um numero: '))

# Enquanto o número inserido for maior ou igual a 0, o loop continuará
while numero >= 0:
    # Se o número inserido for maior que o valor armazenado em 'm', atualiza 'm' com o número
    if numero > m:
        m = numero  # 'm' recebe o novo maior valor
    
    # Solicita outro número ao usuário para continuar o loop
    numero = int(input('Digite um numero: '))

# Quando um número negativo for inserido, o loop termina e o maior número inserido é exibido
print(f"Maior numero é {m}")
