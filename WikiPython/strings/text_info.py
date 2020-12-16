# um programa para mostrar algumas informações de um texto (mostrando a quantidade de espaços que tem nele, a quantidade de vogais e a quantidade de caracteres.)

txt = input('Digite uma frase:\n')
vogais = ['a', 'e', 'i', 'o', 'u']

length = len(str(txt))


spaces = txt.find(' ') > 0 and txt.find(' ') or 0

count = 0

for i in vogais:
    count += txt.lower().count(i)
        

print(f'\n{length} caracter/caracteres\n{spaces} espaço(s)\n{count} vogal/vogais')