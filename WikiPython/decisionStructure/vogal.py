# programa para saber se a letra fornecida pelo usuário é uma vogal ou não.
word = str(input('Qual é a letra?\n').lower())
check = ''

if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
    check = 'é uma vogal'
else:
    check = 'não é uma vogal'
    
print(check)
