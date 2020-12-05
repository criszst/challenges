try:
 number = int(input('Qual é o número para verificar se ele é negativo ou positivo?\n'))
except ValueError:
 number = int(input('formato inválido. Digite um número novamente:\n'))

reply = ''

if number >= 0:
    reply = 'número positivo'
else:
    reply = 'número negativo'
    
print(reply)