#En este gestor de tareas, imaginamos que ya existe una cantidad determinada de tareas por asignación
#para este ciclo escolar, en este caso, son 5 tareas por cada asignación.

import pandas as pd

df = pd.read_excel("C:\Users\keila\OneDrive\Documents\Repositorio Github\Keila-Perales-2\Gestor_de_tareas\Lista_de_tareas.xlsx")
print(df)

from datetime import datetime

fechas = pd.read_excel("C:\Users\keila\OneDrive\Documents\Repositorio Github\Keila-Perales-2\Gestor_de_tareas\s_fechas.xlsx", sheet_name= 'Hoja1')
print(fechas)

tabla_fechas = fechas.iloc[3:, 2:]
tabla_fechas = tabla_fechas.apply(pd.to_datetime, errors='coerce')

fecha_actual = datetime.now()   

print("¡Bienvenido a tu gestor de tareas!")


def menu():
    print("Menú de operaciones")
    print("A: Consulta las materias disponibles")
    print("B: Visualizar tarea")
    print("C: Conteo de tareas disponibles") #Aquí ya estoy descartando las vencidas con la fn de fechass
    print("D: Ayuda")
    print("E: Salir")

    x = input("Ingrese la letra correspondiente a lo deseado:").upper()

    if x == "A":
        A = ["Química", "Matemáticas","Inglés","Física","Artes","Deportes"]
        print("Las materias disponibles son:",A)
    elif x == "B":
        def visualizar_tareas(df,fila,columna):
            try:
                valor = df.at[fila, columna]
                if valor in [True]:
                    return "Esta tarea ya está completa"
                else:
                    def tarea():
                            archivo = f"C:\Users\keila\OneDrive\Documents\Repositorio Github\Keila-Perales-2\Gestor de tareas\{materia}\{asignacion}.txt"  
                            with open(archivo, "r") as doc:
                                contenido = doc.read()
                                print(contenido)
                    tarea()    
            except KeyError:
                return "Tarea no encontrada"
            except IndexError:
                return "Materia no encontrada"
            materia = input("Ingrese el nombre de la materia para visualizar:")
            asignacion = int(input("Ingrese el numero de asignación que desea ver(recordar que estas van del 1-5):"))
            print(f"Esta es la tarea {asignacion} de la materia {materia}")
            resultado = visualizar_tareas(df,materia,asignacion)
            print(resultado)
        visualizar_tareas()
    elif x == "C":
        def vencimiento():
            fechas_vigentes = tabla_fechas[tabla_fechas >= fecha_actual]
            cantidad_vigentes = fechas_vigentes.count().sum()
            print(f"La cantidad de tareas vigentes es : {cantidad_vigentes}")
        vencimiento()
    elif x == "D":
        print("Contacte a nuestro soporte técnico a través de:\n\tsoporte.tecnico1@hotmail.com\n\to\n\tTel.81XXXXXXXX")
    elif x == "E":
        print("Nos vemos luego")
    else:
        print("Opción inválida")
menu()


