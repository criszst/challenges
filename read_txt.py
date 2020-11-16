import os.path

if not os.path.isfile('file.txt'):
    print('Criando arquivo...')
    f = open('file.txt', 'a')
    f.write('2 + 2')

f = open('file.txt', 'r')

calc = f.read().split(' ')
operator = ''

if calc[1] == '+':
   operator = int(calc[0]) + int(calc[2])
    
elif calc[1] == '-':
   operator = int(calc[0]) - int(calc[2])
    
elif calc[1] == '*':
    operator = int(calc[0]) * int(calc[2])

elif calc[1] == '/':
    operator = int(calc[0]) / int(calc[2])
    
print(operator)