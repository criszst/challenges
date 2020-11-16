generoReply = input('Qual o seu gênero? Responda com "masculino" para homens e "feminino" para mulheres\n')

while generoReply.lower() != 'masculino' and generoReply.lower() != 'm' and generoReply.lower() != 'feminino' and generoReply.lower() != 'f':
  generoReply = input('Digite um gênero correto. Opções disponiveis:\n Masculino - Homens\n M - Homens\n Feminino - Mulheres\n F - Mulheres\n Digite o gênero novamente: ')

if generoReply.lower() == 'masculino' or generoReply.lower() == 'm':
  reply = input('Digite a sua altura:\n')
  
  
  while not reply.isdigit():
   reply = input('apenas coloque números. Digite a sua altura novamente: ')
   
   if reply.isdigit():
     break
   
  float(reply)
  transform_string = str(reply)
    
  if transform_string[1] != '.':
   invalid = False
  
   while not invalid:
    reply = float(input('coloque a altura da maneira correta. Exemplo: 1.65\nDigite a sua altura: '))
    
    string_reply = str(reply)
    
    if string_reply[1] == '.':
      invalid = True
      break

  calc = (72.7 * reply) - 58

  print(f'O peso ideal para homens (baseado na sua altura) é {round(calc)}')

elif generoReply.lower() == 'feminino' or generoReply.lower() == 'f':
  alt = input('Digite a sua altura:\n')
  
  while not alt.isdigit():
   alt = input('apenas coloque números. Digite a sua altura novamente: ')
   
   if alt.isdigit():
     break
   
  float(alt)
  
  transform_str = str(alt)
  
  if transform_str[1] != '.':
  
   heigthInvalid = False
  
   while not heigthInvalid:
    alt = float(input('coloque a altura da maneira correta. Exemplo: 1.65\nDigite a altura novamente: '))
    
    str_alt = str(alt)
    
    if str_alt[1] == '.':
     invalid = True
     break

  calc = (62.1 * alt) - 44.7

  print(f'O peso ideal para mulheres (baseado na sua altura) é {round(calc)}')