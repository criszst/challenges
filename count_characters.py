# programa para contar os caracteres de uma frase e verificar se é menor que tal número ou maior que tal número, assim, mudando a resposta que é enviada ao terminal.

frase = input('Digite uma frase: ')
nmr = input('Digite um número: ')

def length(str):
  count = len(str)
  return count

if length(frase) >= 10:
    print(f'a frase tem mais que 10 ou é igual a 10 caracteres. Ela tem {length(frase)} caractere(s)')
else:
    print(f'a frase tem menos de 10 caracteres. Ela tem {length(frase)} caractere(s)')

while not nmr.isdigit():
   nmr = input('Não coloque frases, apenas coloque números. Digite um número novamente: ')

transformInt = int(nmr)
     
if transformInt >= 10:
      print(f'o número é maior ou igual a 10. Número digitado: {transformInt}')
      
else:
         print(f'o número é menor que 10. Número digitado: {transformInt}')