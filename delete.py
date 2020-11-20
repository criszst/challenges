import os

arquivo = str(input('Qual é o nome do arquivo?\n'))

while not os.path.isfile(arquivo):    
   arquivo = str(input('o arquivo desejado não existe. Insira um novo arquivo:\n'))
   

if os.path.isfile(arquivo): 
  os.remove(arquivo)
  print('arquivo removido com sucesso!')