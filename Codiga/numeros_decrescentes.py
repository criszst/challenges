# By @azure --> https://github.com/Liga-dos-Programadores/codiga/blob/master/desafios-antigos.md#009---numeros-decrescentes-by-azure

import heapq

numbers = str(input('Digite os números abaixos:\n'))

while not numbers.isdigit():
    numbers = str(input('digite apenas números. Digite alguns números:\n'))
    
    if numbers.isdigit():
        break

while len(numbers) <= 1:
    numbers = str(input('Digite mais de um número. Digite alguns números novamente:\n'))
    
    if len(numbers) > 1:
        break
    
lst = list(numbers)
# lst = list(set(numbers))

largest = heapq.nlargest(len(numbers), lst)

transform_str = ''.join(largest)

print(f'Ordem descrescente: {transform_str}')