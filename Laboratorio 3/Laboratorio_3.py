
#Pedir nombre y apellido de usuario y dar bienvenida

a = print("Bienvenido/a "+input("Ingrese su nombre: ")+" "+input("Ingrese su apellido: "))

#Crear un programa que pida dos numeros enteros y muestre su suma, resta, multiplicación y división

x = int(input("Ingrese un número entero: "))
y = int(input("Ingrese otro numero entero: "))
suma = x + y
resta1 = x - y
resta2 = y - x
mult = x * y
division1 = x/y
division2 = y/x
print(f"La suma de {x} y {y} es {suma}, mientras que la resta de {x}-{y} es {resta1} y la de {y}-{x} es {resta2} \nla multiplicación de estos dos números es {mult} y la división  de {x} entre {y} es {division1:.2f} y la división contraria es {division2:.2f}")


# Que al introducir una oración la devuelva en mayúsculas, minúsculas y con las primeras letras en mayúsculas


z = input("Intruduzca una oración: ")
mayus = z.upper()
minusculas = z.lower()
primera = z.title()

print(f"La oración '{z}' en diversos formatos es:\n{mayus} - completamente en mayúsculas,\n{minusculas} - completamente en minúsculas,\n{primera} - solo la primer letra de cada palabra en mayúscula")

#Pedir fecha de nacimiento e imprimir cuántos días han transcurrido hasta la fecha

from datetime import datetime

nacimiento = input("Introduce tu fecha de nacimiento (formato: DD/MM/AAAA): ")
nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y")
fecha_actual = datetime.now()
resultado = (fecha_actual - nacimiento).days

print(f"Los días transcurridos hasta hoy son {resultado}")

#Recibir un numero flotante y lo muestre redondeado a dos decimales 

num = float(input("Introduce una cantidad con decimales: "))
print(f"Tu numero redondeado a dos decimales es {num:.2f}")


#Escribir un programa qque pida un archivo de texto y nos muestre dicho archivo en la pantalla
#Ojo: funciona solo para archivos que se encuentren en la misma carpeta que este documento de python

leer = input("Ingresa el nombre del archivo que desea abrir con .txt al final: ")
with open(leer, "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#Desarrollar un programa que lea una lista de numeros separados por comas y luego imprima la suma de estos 


lista = input("Ingresa una lista de número sepaarados por comas: ")
numero_lista =[float(lista) for lista in lista.split(",")]
suma = sum(numero_lista)
print(f"La suma de los numeros en tu lista es {suma}")

#Solicitar dos cadenas de texto y que se impriman concatenadas

oracion1 = input("Ingrese una cadena de texto: ")
oracion2 = input("Ingrese otra cadena de texto que quiera añadir al final de la primera: ")
union = oracion1 +" "+ oracion2
print(f"Esta es tu oración completa:\n{union}")

#Solicitar su nombre y que luego imprimirlo invertido

name = input(" Ingresa tu nombre: ")
invertido = name[::-1]
print(f"Este es tu nombre invertido: {invertido}")

#Solicitar una serie de calificaciones y luego imprima el promedio

n = int(input("Ingrese la cantidad de calificaciones a promediar: "))
calif_list = []
for calif in range(n):
    calificacion = float(input(f"Ingrese la calificación {calif + 1}: "))
    calif_list.append(calificacion)
prom = sum(calif_list)/len(calif_list)

print(f"El promedio es {prom:.2f}")


#  Solicitar peso y altura y calcular su IMC

Name1 = input("Ingresa tu nombre: ")
peso = float(input("Ingresa tu peso (kg): "))
altura = (float(input("Ingresa tu altura (cm): ")))/100
calculo = peso / (altura)**2
print(f"Hola {Name1}, tu IMC es de {calculo:.2f}")
      
#Programa que genere un numero aleatorrio entre 1 y 100  y pida al usuario adivinarlo, dando pisatas de si es mayor o menor

import random

def juego():
    mistery = random.randint(1, 100)
    intento = None
    j = input("Introduce tu nombre: ")

    print(f"Bienvenido al juego {j}")
    print("Adivina el número en el que pienso (se encuentra entre 1 y 100)")

    while intento != mistery:
        intento = int(input("Introduce tu número: "))
        
        if intento < mistery:
            print("El número es mayor")
        elif intento > mistery:
            print("El número es menor")

    print(f"¡Felicidades! el número es {mistery}.")

juego()

#Hacer un programa que pida una lista de nombres y los ordene alfabeticamente
def ordenar_nombres():
    nombres = []
    print("Introduce los nombres que deseas ordenar iniciando con mayúscula, escribe 'fin' para terminar.")

    while True:
        nombre = input("Introduce un nombre: ")
        if nombre.lower() == 'fin':
            break
        nombres.append(nombre)

    nombres.sort()

    print("\nNombres ordenados alfabéticamente:")
    for nombre in nombres:
        print(nombre)

ordenar_nombres()

#Escribir un programa que muestre la tabla de multiplicar de un numero introducido

def tabla_multiplicar():
    numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

    print(f"\nTabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabla_multiplicar()

#Programa que pida al usuario introducir una oración e imprimir la cantidad de palabras que tiene

def contar():
    oracion = input("Introduce una oración: ")
    palabras = oracion.split()
    cantidad_palabras = len(palabras)

    print(f"La oración tiene {cantidad_palabras} palabras.")

contar()

