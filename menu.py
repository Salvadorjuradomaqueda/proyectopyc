import sqlite3
conexion = sqlite3.connect('moto-gp.db')
cursor = conexion.cursor()

def mostrar_menu():
    print("*****MENÚ PRINCIPAL******")
    print("1.Crear datos")
    print("2.Borrar datos")
    print("3.Actualizar datos")
    print("4. Salir")
    print("*************************")

def menu():
    while True:
        mostrar_menu()
        elige = input("Selecciona una opción (1-4): ")
        
        if elige == "1":
            print("Creación de datos seleccionada")
        elif elige == "2":
            print("Borrado de datos seleccionado")
        elif elige == "3":
            print("Actualización de datos seleccionada")
        elif elige == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            
                     
menu()

