number = int(input('Qual é o número para verificar se ele é negativo ou positivo?\n'))

choice = ''

if number >= 0:
    choice = 'número positivo'
else:
    choice = 'número negativo'
    
print(choice)