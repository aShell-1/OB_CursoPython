from time import strftime

str_horas = strftime('%H')
str_minutos = strftime('%M')
hora_limite = 19 # 7pm

print(f'Son las {str_horas}:{str_minutos} h')
if int(str_horas) >= hora_limite:
    print('Lo hiciste bien. Hora de ir a casa.')
else:
    print(f'Faltan {hora_limite-1-int(str_horas)}:{60-int(str_minutos)} h para ser libres.')