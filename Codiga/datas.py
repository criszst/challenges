# --> https://github.com/Liga-dos-Programadores/codiga/blob/master/desafios-antigos.md#desafio-extra-6-meses

def extensive(date):
     day, month, year = map(int, date.split('/'))
   
     months = { 
          1: 'Janeiro',
          2: 'Fevereiro',
          3: 'Março',
          4: 'Abril',
          5: 'Maio',
          6: 'Junho', 
          7: 'Julho',
          8: 'Agosto',
          9: 'Setembro',
          10: 'Outubro',
          11: 'Novembro',
          12: 'Dezembro'
     }
      
     months_31 = [1, 3, 5, 7, 8, 10, 12]
     months_30 = [4, 6, 9, 11]
      
     leap_year = year % 4 == 0 and True or False
   
     if day == 0:
       msg = f'[data inválida] --- o número "{day}" não é um dia válido.'
   
   
     elif month > 12 or month <= 0:
       msg = f'[data inválida] --- o número "{month}" não é um mês válido.'
     
     
     elif year < 0000:
       msg = None
     
     
     elif month == 2 and day >= 30:
       msg = None
   
   
     elif month in months_31 and day > 31:
       msg = None
    
    
     elif month in months_30 and day > 30:
       msg = None
    
    
     elif leap_year == True and month == 2 and day == 29:
       msg = 'data válida'
    
    
     elif leap_year == False and month == 2 and day == 29:
       msg = None
       
       return print(f'{msg}\nData por extenso: {day} de {months[int(date)]} de {year}')

data = input('Digite uma data:\n')

extensive(data)