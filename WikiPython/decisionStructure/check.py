# programa que verifica se um número é negativo ou se é positivo.
try:
 number = int(input('Qual é o número para verificar se ele é negativo ou positivo?\n'))
except ValueError:
 number = int(input('formato inválido. Digite um número novamente:\n'))

print('positivo' if number >= 0 else 'negativo')
