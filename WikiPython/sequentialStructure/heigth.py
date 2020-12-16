# programa para saber o peso ideal da pessoa baseado na sua altura em centimetros

generoReply = input('Qual o seu gênero? Responda com "masculino" para homens e "feminino" para mulheres\n')

while generoReply.lower() != 'masculino' and generoReply.lower() != 'm' and generoReply.lower() != 'feminino' and generoReply.lower() != 'f':
  generoReply = input('Digite um gênero correto. Opções disponiveis:\n Masculino - Homens\n M - Homens\n Feminino - Mulheres\n F - Mulheres\n Digite o gênero novamente: ')

def calc_function(reply):
  try:
   reply = float(input('Digite a sua altura:\n'))
  except ValueError:
    # gambiarra logo abaixo...
    try:
     reply = float(input('não coloque frases. Apenas coloque números\nDigite a sua altura novamente: '))
    except ValueError:
      reply = float(input('não coloque frases. Apenas coloque números\nDigite a sua altura novamente: '))
     

    
  if str(reply)[1] != '.':
    
    while not str(reply).isdigit():
      if str(reply).replace('.', '').isdigit():
       break
    
      reply = input('apenas coloque números. Digite a sua altura novamente: ')
   

  if str(reply)[1] != '.':
    
   invalid = False
  
   while not invalid:
    reply = float(input('coloque a altura da maneira correta. Exemplo: 1.65\nDigite a sua altura: '))
    
    if str(reply)[1] == '.':
      invalid = True
      break
    

  return reply

if generoReply.lower() == 'masculino' or generoReply.lower() == 'm':
  reply = ''
  
  alt = calc_function(reply)
  
  calc = (72.7 * alt) - 58

  print(f'O peso ideal para homens (baseado na sua altura) é {round(calc, 2)} KG')

elif generoReply.lower() == 'feminino' or generoReply.lower() == 'f':
  reply = ''
  
  alt = calc_function(reply)
  
  calc = (62.1 * alt) - 44.7

  print(f'O peso ideal para mulheres (baseado na sua altura) é {round(calc, 2)} KG')
  
  # Outra forma de fazer o ".toFixed(2)" do Javascript (além do round(<var>, 2)):
  # ---> float('{:.2f}'.format(calc))