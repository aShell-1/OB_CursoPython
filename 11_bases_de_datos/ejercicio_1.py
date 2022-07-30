"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""
import sqlite3

def main():
    cnx = sqlite3.connect('ejercicio.db')
    cur = cnx.cursor()
    crear_tabla(cur)
    insertar_alumnos(cnx, cur)
    mostrar_alumnos(cur)
    cur.close()
    cnx.close()

def crear_tabla(cur):
    cur.execute(''' create table if not exists alumnos(id integer primary key, nombre text not null, clave not null)''')

def insertar_alumnos(cnx, cur):
    try:
        for i in range(10):
            query = 'insert into alumnos (id, nombre, clave) values(?,?,?)'
            cur.execute(query, (i+1,f'alumno{i+1}',f'clave{i+1}'))
    except sqlite3.IntegrityError:
        print('\nNo se pudo insertar la data\n')

    cnx.commit()

def mostrar_alumnos(cur):
    headers = []
    for field in cur.execute("select name from pragma_table_info('alumnos')"):
        headers.append(field[0])

    print(f'{headers[0] : <5} {headers[1] : <10} {headers[2] : <8}')
    print('-'*5 +' '+'-'*10 +' '+'-'*8)

    for row in cur.execute('select * from alumnos where nombre="alumno1" or nombre="alumno2"'):
        print(f'{row[0] : <5} {row[1] : <10} {row[2] : <8}')


if __name__ == '__main__':
    main()