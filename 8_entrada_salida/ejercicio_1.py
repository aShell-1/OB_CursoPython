with open('miarchivo.txt', 'w') as waak:
    waak.write('El pollito pio 1\n')
    waak.write('El pollito pio 2\n')
    waak.write('El pollito pio 3')

with open('miarchivo.txt','r+') as waak:
    print(waak.read())
    print()
    waak.write('\nEn la radio hay un pollito')
    
    waak.seek(0)
    print(waak.read())