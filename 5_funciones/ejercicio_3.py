def esBisiesto(year):
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)) :
        return True
    else:
        return False

for i in range(1900, 2000+1):
    if esBisiesto(i) == True:
        print(str(i)+" es bisiesto")