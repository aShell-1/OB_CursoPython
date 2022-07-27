"""
En este segundo ejercicio, tenéis que crear una aplicación que
obtendrá los elementos impares de una lista pasada por parámetro
con filter y realizará una suma de todos estos elementos 
obtenidos mediante reduce.
"""

from functools import reduce

full_list = [12, 32, 25, 1345, 65, 34, 77, 1]
impar_list = list(filter(lambda i: i%2 != 0, full_list))

print(
    f'Lista: {impar_list}\n'
    f'Usando sum() => {sum(impar_list)}\n'
    f'Usando reduce() => {reduce((lambda x,y: x+y), impar_list)}'
    )