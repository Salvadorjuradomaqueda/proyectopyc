import sqlite3
conexion = sqlite3.connect('moto-gp.db')
cursor = conexion.cursor()



def menu():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Crear registro")
        print("2. Leer registros")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_registro()
            conexion.commit()
            cursor.close
        elif opcion == "2":
            leer_registros()
        elif opcion == "3":
            actualizar_registro()
        elif opcion == "4":
            eliminar_registro()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

def crear_registro():
    tabla = input("¿En que tabla? (equipo/piloto/moto): ")
    if tabla == "equipo":
        id_e = int(input("ID: "))
        nombre = input("Nombre: ")
        puntos = int(input("Puntos: "))
        cursor.execute("INSERT INTO equipo VALUES (?, ?, ?)", (id_e, nombre, puntos),)
        
    elif tabla == "piloto":
        id_p = int(input("ID: "))
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        altura = float(input("Altura: "))
        dorsal = int(input("Dorsal: "))
        id_equipo = int(input("ID Equipo: "))
        cursor.execute("INSERT INTO piloto VALUES (?, ?, ?, ?, ?, ?)", (id_p, nombre, edad, altura, dorsal, id_equipo),)
        
    elif tabla == "moto":
        id_m = int(input("ID: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        marca = input("Marca: ")
        id_piloto = int(input("ID Piloto: "))
        cursor.execute("INSERT INTO moto VALUES (?, ?, ?, ?, ?)", (id_m, nombre, precio, marca, id_piloto),)
       

def leer_registros():
    tabla = input("¿Qué tabla? (equipo/piloto/moto): ")
    cursor.execute(f"SELECT *FROM {tabla}")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

def actualizar_registro():
    tabla = input("¿Qué tabla? (equipo/piloto/moto): ")
    id_registro = input("ID del registro a actualizar: ")
    columna = input("¿Qué columna actualizar?: ")
    valor = input("Nuevo valor: ")
    cursor.execute(f"UPDATE {tabla} SET {columna} = ? WHERE id_{tabla} = ?", (valor, id_registro))
    

def eliminar_registro():
    tabla = input("¿Qué tabla? (equipo/piloto/moto): ")
    id_registro = input("ID del registro a eliminar: ")
    cursor.execute(f"DELETE FROM {tabla} WHERE id_{tabla} = ?", (id_registro,))
    

menu()







conexion.commit()
conexion.close()


