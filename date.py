# um pequeno "programa" que lê uma data fornecida pelo usuário (no formato dd/mm/yyyy) e, caso essa data for válida, ele imprime "data válida" no terminal, caso não for, ele imprime "data inválida".


def validate(date):
   msg = 'data válida'

   if not date.replace('/', '').isdigit():
     while not date.isdigit():
       date = input('[data inválida] --- apenas coloque números. Coloque uma data no formato "dd/mm/yyyy" (exemplo: 15/7/2020).\nDigite uma data novamente: ')
       
       if date.replace('/', '').isdigit():
         break
       
   if not '/' in date:
     while not '/' in date:
      date = input('[data inválida] --- a data não contém uma barra (/)\nExemplo de uma data correta para o sistema: 1/2/2020\nDigite uma data novamente: ')
  
      if '/' in date:
        break
  
   day, month, year = map(int, date.split('/'))
   
   
   months_31 = [1, 3, 5, 7, 8, 10, 12]
   months_30 = [4, 6, 9, 11]
   
   leap_year = year % 4 == 0 and True or False
   
   if day == 0:
     msg = f'[data inválida] --- o número "{day}" não é um dia válido.'
   
   
   elif month > 12 or month <= 0:
     msg = f'[data inválida] --- o número "{month}" não é um mês válido.'
     
     
   elif year < 0000:
     msg = f'[data inválida] --- o número "{year}" não é um ano válido.'
     
     
   elif month == 2 and day >= 30:
     msg = f'[data inválida] --- o mês "2" tem apenas 28 dias (exceto em anos bissextos).'
   
   
   elif month in months_31 and day > 31:
     msg = f'[data inválida] --- o mês "{month}" contém apenas 31 dias. Você colocou um dia que não existe no mês.'
    
    
   elif month in months_30 and day > 30:
    msg = f'[data inválida] --- o mês "{month}" contém apenas 30 dias. Você colocou um dia que não existe no mês.'
    
    
   elif leap_year == True and month == 2 and day == 29:
     msg = 'data válida'
    
    
   elif leap_year == False and month == 2 and day == 29:
     msg = f'[data inválida] --- o ano não é bissexto, logo, você não pode colocar o dia 29 no mês 2.'
     

   return print(msg)


date = input('Digite uma data:\n')

validate(date)