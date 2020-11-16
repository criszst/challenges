generoReply = input('Qual o seu gênero? Responda com "masculino" para homens e "feminino" para mulheres\n')

while generoReply.lower() != 'masculino' and generoReply.lower() != 'm' and generoReply.lower() != 'feminino' and generoReply.lower() != 'f':
  generoReply = input('Digite um gênero correto. Opções disponiveis:\n Masculino - Homens\n M - Homens\n Feminino - Mulheres\n F - Mulheres\n Digite o gênero novamente: ')

if generoReply.lower() == 'masculino' or generoReply.lower() == 'm':
  try:
   reply = float(input('Digite a sua altura:\n'))
  except ValueError:
    reply = float(input('não coloque frases. Apenas coloque números\nDigite a sua altura novamente: '))
    
  if str(reply)[1] != '.':
    while not str(reply).isdigit():
      if str(reply).replace('.', '').isdigit():
       break
    
      reply = input('apenas coloque números. Digite a sua altura novamente: ')
   
  float(reply)

  if str(reply)[1] != '.':
   invalid = False
  
   while not invalid:
    reply = float(input('coloque a altura da maneira correta. Exemplo: 1.65\nDigite a sua altura: '))
    
    if str(reply)[1] == '.':
      invalid = True
      break

  
  calc = (72.7 * reply) - 58

  print(f'O peso ideal para homens (baseado na sua altura) é {calc} KG')

elif generoReply.lower() == 'feminino' or generoReply.lower() == 'f':
  try:
   alt = float(input('Digite a sua altura:\n'))
  except ValueError:
    alt = float(input('não coloque frases. Apenas coloque números\nDigite a sua altura novamente: '))
  
  
  
  if str(alt)[1] != '.':
    while not str(alt).isdigit():
      if str(alt).replace('.', '').isdigit():
       break
    
      alt = input('apenas coloque números. Digite a sua altura novamente: ')
   
   
  float(alt)
  
    
  if str(alt)[1] != '.':
   invalid = False
  
   while not invalid:
    alt = float(input('coloque a altura da maneira correta. Exemplo: 1.65\nDigite a sua altura: '))
    
    string_reply = str(alt)
    
    if string_reply[1] == '.':
      invalid = True
      break

  
  calc = (62.1 * alt) - 44.7

  print(f'O peso ideal para mulheres (baseado na sua altura) é {calc} KG')