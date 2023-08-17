# cuidado com loop infiniito
#estrutura de controle para criar loop 
numero_sorteado = 15

numero_escolhido = int(input('Informe un número entre 1 e 20:' ))

if numero_sorteado == numero_escolhido:
    print('Você acertou!')
else:
    print('você errou!')


while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('parabens! voce acertou!')

# Exemplo 02: Estrutura com contador

contador=0

while contador < 5:
    print(contador)

contador  = contador + 1