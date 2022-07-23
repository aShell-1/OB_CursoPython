# CLASES
## Crear clase en Python

```python
class nombre_clase:  
    propiedad1 = 'valor1'

    def metodo1():
        pass
```
## Ejemplo
```python
class Linterna:
    _encendido = True

    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False
    def isEncendido(self):
        return self._encendido

# Instanciar para usar
d = Linterna()
d.encendido = False

print(d.encendido)
# Imprime False
```
*Python por defecto y no defecto usa propiedades públicas*

*Una convención en Python es que si una propiedad inicia con _ no deberíamos manipularla fuera de la clase*

*Anteponer self indica que nos referimos a una propiedad de la clase. Sino se estaría creando una variable local.*

## Destructor
Se invoca en el momento que no hay más referencias a la clase asociada.

# OBJETO
Representación de algo real en programación.

## Instanciar para usar
