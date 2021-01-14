# programa para ler os números de um arquivo.txt e calcular os mesmos de lá. Por exemplo, caso um arquivo.txt contenha o calculo "10 / 2", ele irá calcular o mesmo e irá imprimir o resultado no terminal.

import os.path
import sys

if not os.path.isfile('file.txt'):    
    writeTxt = input('eu não encontrei o arquivo. Sendo assim, qual cálculo você deseja no arquivo?\n')
    
    if not writeTxt.isdigit():
        isNotDigit = True
        
        while isNotDigit == True:
         if writeTxt[0].isdigit():
             isNotDigit = False
             break
          
         writeTxt = str(input('apenas escreva números, sem letras...:\n'))
         
    
    f = open('file.txt', 'a')    
    f.write(writeTxt)
    print('arquivo criado com o cálculo %s' % writeTxt)


f = open('file.txt', 'r')

read = f.read()
      
calc = read.split(' ')

if len(calc) == 1:
  print(f'não há cálculos para ser calculado. Texto no arquivo: {read}')
  
else:
  
  operator = ''


  if calc[1] == '+':
   operator = int(calc[0]) + int(calc[2])
    
  elif calc[1] == '-':
   operator = int(calc[0]) - int(calc[2])
    
  elif calc[1] == '*':
    operator = int(calc[0]) * int(calc[2])

  elif calc[1] == '/':
    operator = int(calc[0]) / int(calc[2])
    
    
  if operator == '':
    print(f'Sem resultado aparente. Texto no arquivo:\n{read}')

  else:
   print(f'Resultado: {operator}')
