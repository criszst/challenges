# um pequeno "programa" que lê uma data fornecia pelo usuário (no formato dd/mm/yyyy) e, caso essa data for válida, ele imprime "data válida" no terminal, caso não for, ele imprime "data inválida".

def validate(date):
    str(date)
    err = ''
    
    if len(date) < 8 or len(date) > 10:
        while len(date) < 8 and len(date) > 10:
         err = input('[data inválida] --- a data tem menos que 8 caracteres ou tem mais que 10 caracteres, se tornando, assim, uma data inválida. Exemplo de uma data correta para o sistema: 10/12/2020\n Insira uma data novamente: ')
         
         if len(err) == 8 or len(err) == 9 or len(err) == 10:
             date = err
             break
           
    if not '/' in date:
      while not '/' in date:
        err = input('[date inválida] --- a data nao contém nenhuma barra (/).\nExemplo de uma data correta para o sistema: 1/2/2020.\nDigite uma data novamente:\n')
        
        if '/' in err:
          date = err
          break
         
         
    if len(date) == 8:
        
      if not date.replace('/', '').isdigit():
         while not date.replace('/', '').isdigit():
          err = input(f'[data inválida] --- apenas coloque números na data.\nExemplo de uma data correta para o sistema: 1/1/2020\nInsira uma data novamente: ')
         
          if str(date).replace('/', '').isdigit():
             date = err
             break
         
         
      if len(date[0]) == 1:
          
        if date[1] != '/':
          while date[1] != '/':
            err = input('[data inválida] --- a data não contém uma barra (/) nas posições corretas.\nExemplo de uma data correta para o sistema: 1/2/2020\nInsira uma data novamente: ')
            
            if str(err[1]) == '/':
               date = err
               break
           
         
      elif len(date[0]) == 2:
          
        if date[2] != '/':
         while date[2] != '/':
           err = input('[data inválida] --- a data não contém uma barra (/) nas posições corretas.\nExemplo de uma data correta para o sistema: 10/1/2020\nInsira uma data novamente: ')
            
           if str(err[2]) == '/':
              date = err
              break
          
          
    elif len(date) == 9:
        
     if not date.replace('/', '').isdigit():
         while not date.replace('/', '').isdigit():
          err = input(f'[data inválida] --- apenas coloque números na data.\nExemplo de uma data correta para o sistema: 10/12/2020\nInsira uma data novamente: ')
         
          if str(err).replace('/', '').isdigit():
              date = err
              break
         
         
     if len(date[0]) == 2:
         
       if date[2] != '/':
          while date[2] != '/':
            err = input('[data inválida] --- a data não contém uma barra (/) nas posições corretas.\nExemplo de uma data correta para o sistema: 1/2/2020\nInsira uma data novamente: ')
            
            if str(err[2]) == '/':
               date = err
               break
           
           
     elif len(date[0]) == 1:
         
       if date[2] != '/':
          while date[2] != '/':
            err = input('[data inválida] --- a data não contém uma barra (/) nas posições corretas.\nExemplo de uma data correta para o sistema: 10/2/2020\nInsira uma data novamente: ')
            
            if str(err[2]) == '/':
               date = err
               break
             
         
    elif len(date) == 10:
        
     if not date.replace('/', '').isdigit():
         while not date.replace('/', '').isdigit():
          err = input(f'[data inválida] --- apenas coloque números na data.\nExemplo de uma data correta para o sistema: 10/12/2020\nInsira uma data novamente: ')
         
          if str(err).replace('/', '').isdigit():
              date = err
              break
          
     if len(date[0]) == 1:
          
        if date[1] != '/':
          while date[1] != '/':
            err = input('[data inválida] --- a data não contém uma barra (/) nas posições corretas.\nExemplo de uma data correta para o sistema: 1/2/2020\nInsira uma data novamente: ')
            
            if str(err[1]) == '/':
               date = err
               break
           
         
     elif len(date[0]) == 2:
          
        if date[2] != '/':
         while date[2] != '/':
           err = input('[data inválida] --- a data não contém uma barra (/) nas posições corretas.\nExemplo de uma data correta para o sistema: 10/1/2020\nInsira uma data novamente: ')
            
           if str(err[2]) == '/':
              date = err
              break
         
        
    return True

date = input('Digite uma data:\n')

correct_or_no = validate(date)

if correct_or_no == True:
    print('data válida')