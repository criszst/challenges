# programa para coletar o maior número de uma lista

numbers = str(input('Quais são os números? Digite abaixo:\n'))

transformList = list(numbers.replace(' ', ''))

big = max(transformList)

""" str_list = str(transformList)
a = ''.join(str_list)

find = a.find(big) """

print(f'Maior número: {big}')
# print(f'Maior número: {big} | na posição {find}')