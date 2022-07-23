class Alumno:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    def imprimirDatos(self):
        print('Nombre: {}\nNota: {}'.format(self._nombre, self._nota))

    def isAprobado(self):
        print('Estado: '+ ('Aprobado' if self._nota > 13  else 'Reprobado'))

alumno1 = Alumno('Daikon', 17)
alumno1.imprimirDatos()
alumno1.isAprobado()
print()
alumno2 = Alumno('Zanahoria', 11)
alumno2.imprimirDatos()
alumno2.isAprobado()