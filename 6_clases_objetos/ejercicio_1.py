class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

    def __str__(self):
        return 'Color : {}\nRuedas: {}\nPuertas: {}'.format(self._color, self._ruedas, self._puertas)

class Coche (Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrado):
        super().__init__(color, ruedas, puertas)
        self._velocidad = velocidad
        self._cilindrado = cilindrado

    def __str__(self):
        return super().__str__() + '\nVelocidad: {}\nCilindrado: {}'.format(self._velocidad, self._cilindrado )

print('-> VEHÍCULO')
vehiculo1 = Vehiculo('Rojo', 2, 0)
print(vehiculo1)
print('\n-> COCHE' )
coche1 = Coche('Negro', 4, 4, 60, 2.83)
print(coche1)