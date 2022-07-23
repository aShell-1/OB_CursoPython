from math import sqrt

def esPrimo(num):
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            if (num % i == 0):
                return False
        return True

    else:
        return False

for i in range(60):
    if esPrimo(i) == True:
        print(str(i) + " es primo")