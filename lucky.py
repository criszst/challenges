# programa com o sistema de "loop" para verificar se o usuário acertou o número sorteado. Caso não tenha sorteado, um loop de "número errado. Digite novamente: " será iniciado. Se ele acertar na pergunta desse loop ou fora, o loop acaba/não irá existir.

import random

question = int(input('Escolha dentre as opções abaixo: \nDigite 1 para jogar contra a máquina\nDigite 2 para deixar a máquina jogar sozinha.\n'))

if question == 1:
 rdn = random.randrange(0, 11)

 print('número sorteado. O número está entre 0 e 10.')

 choice = int(input('Tente adivinhar o número que foi sorteado. Digite o seu palpite: '))

 if choice == rdn:
    print(f'Você acertou o número {rdn}!')
    
 while choice != int(rdn):
    again = int(input('número errado. Digite novamente: '))
    
    if again == int(rdn):
        print(f'Você aceitou o número {rdn}!')
        break


# para fazer a maquina jogar sozinha:
elif question == 2:
 rdn = random.randrange(0, 11)

 print('número sorteado. O número está entre 0 e 10.')

 choice = random.randrange(0, 11)

 if choice == rdn:
    print(f'Eu acertei o número {rdn}!')
    
 while choice != int(rdn):
    again = random.randrange(0, 11)
    
    if again == int(rdn):
        print(f'Eu aceitei o número {rdn}! - while')
        break
