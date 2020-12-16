# programa para converter metros em centimetros
question = str(input('Especifique a conversão.\n Digite 1 para converter metros em centimetros\n Digite 2 para converter centimetros em metros:\n'))

if question == '1':
 m = int(input('Digite a quantidade de metros:\n'))

 calc = m * 100

 print(f'Conversão: {calc}cm')

elif question == '2':
  cm = int(input('Digite a quantidade de centimetros:\n'))
  
  transform = cm / 100
    
  print(f'Conversão: {transform} metro(s)')