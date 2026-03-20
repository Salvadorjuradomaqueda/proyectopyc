import sqlite3
conexion = sqlite3.connect('moto-gp.db')
cursor = conexion.cursor()


cursor.execute('''INSERT INTO moto (id_moto,nombre,precio,marca,id_piloto) VALUES(?, ?, ?, ?, ?)''', (1, 'Marc Marquez', 26, 170, 93, 1))
