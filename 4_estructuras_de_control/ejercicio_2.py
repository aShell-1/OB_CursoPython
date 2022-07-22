num_inicio = 2
num_final = 8
lista_num = []

for i in range(num_inicio, num_final+1):
    if (i % 2) != 0:
        lista_num.append(i)

print(lista_num)