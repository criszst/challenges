# programa para coletar o maior número de uma lista

numbers = str(input('Quais são os números? Digite abaixo:\n'))

if not numbers.replace(' ', '').isdigit():
    while not numbers.replace(' ', '').isdigit():
        numbers = str(input('não coloque letras, apenas números. Digite os números novamente:\n').replace(' ', ''))
        
        if numbers.isdigit():
            break

transformList = list(numbers.replace(' ', ''))

big = max(transformList)

print(f'Maior número: {big}')