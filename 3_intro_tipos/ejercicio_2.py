peso_kg = float(input('Peso (kg): '))
estatura_m = float(input('Estatura (m): '))

imc = peso_kg/(estatura_m)**2

print('Tu índice de masa corporal es ' + str(round(imc, 2)) + ' kg.m^(-2)')