from pickle import dump, load

class Vehiculo:
    def __init__(self, tipo, marca, modelo, color):
        self._tipo = tipo
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def __str__(self):
        return f'{self._tipo} {self._marca} {self._modelo} {self._color}'

vehiculo1 = Vehiculo('Auto', 'BMW', 'Sedán', 'Bernina Grey')
print('-> Objeto desde ejercicio_2.py')
print(vehiculo1)

with open("pickled_obj", "wb") as txtfile:
    dump(vehiculo1, txtfile)

with open("pickled_obj", "rb") as txtfile:
    unpickled_obj = load(txtfile)

print(f'\n-> Objeto desde {txtfile.name}')
print(unpickled_obj)