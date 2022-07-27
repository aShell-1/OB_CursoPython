"""
Crea un script que le pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la listade países
ordenados alfabéticamente y separados por comas.
"""

paises = input('Escribe nombres de países, sepáralos usando \",\":\nIn : ')

paises_list = paises.split(',')
for i in range(len(paises_list)):
    paises_list[i] = paises_list[i].strip().lower().capitalize()

paises_list = sorted(set(paises_list))

print('Out: '+', '.join(paises_list))