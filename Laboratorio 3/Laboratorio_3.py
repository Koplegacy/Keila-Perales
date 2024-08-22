
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

import datetime as now
now.datetime(year,month,day )

dia = int(input("Introduce el dia de nacimiento: "))
mes = int(input("Introduce el mes de nacimiento: "))
año = int(input("Introduce el año de nacimiento: "))  
fecha = datetime.date(año,mes,dia)
s = datetime.date(now)
resultado = fecha - now
print(f"Los días transcurridos son {resultado.days}")