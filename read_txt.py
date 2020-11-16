import os.path

if not os.path.isfile('file.txt'):    
    writeTxt = input('eu não encontrei o arquivo. Sendo assim, qual calculo você deseja no arquivo?\n')
    
    f = open('file.txt', 'a')    
    f.write(writeTxt)
    print('arquivo criado com o cálculo %s' % writeTxt)

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
    
print(f'Resultado: {operator}')