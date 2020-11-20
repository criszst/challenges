# programa para checar o quanto tempo demora a velocidade de download de um arquivo baseado na velocidade da internet e no tamanho do mesmo
tamanho_arquivo = str(input('Qual é o tamanho do arquivo? (em MB)\n').replace(',', ''))

velocidade_internet = str(input('Qual é a velocidade da sua internet? (em Mb/s)\n').replace(',', ''))

calc = int(tamanho_arquivo[0]) / (int(velocidade_internet[0]) / 8)
minuto = round(calc) / 60
horas = round(minuto) / 60


int(calc)

if round(calc) >= 60 and round(calc) < 3600:
    print(f'Irá demorar {round(minuto, 2)} minuto(s) para o download do arquivo ser concluído.')
    
elif round(calc) >= 3600:
    print(f'Irá demorar {round(horas, 2)} hora(s) para o download do arquivo ser concluído.')

else:
   print(f'Irá demorar {round(calc, 2)} segundo(s) para o download do arquivo ser concluído.')