num_a = int(input('Digite um número a: '))
num_b = int(input('Digite um número b: '))

# ao inves de usar:
#if num_a % num_b == 0:
#    print('Sao multiplos')

#elif num_b % num_a == 0:
#    print('Sao multiplos')
# Posso utilizar:

if num_a % num_b == 0 or num_b % num_a == 0:
    print('São múltiplos')

    
else:
    print('Não sao Multiplos')