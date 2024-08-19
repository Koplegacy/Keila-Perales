#función que nos imprima el numero mayor de una lista de n numeros
def mayor_que(lista):
    if not lista:
        return No
    
    maximo = lista[0]  
    
    for numero in lista:
        if numero > maximo:
            maximo = numero  
    
    return maximo
n = int(input("Ingrese la cantidad de números: "))
lista = [float(input(f"Ingrese el elemento {i + 1} para la lista: ")) for i in range(n)]
resultado = mayor_que(lista)
print("El numero mayor es: ", resultado)



#Funcion que tome una lista de palabras y devuelva la mas larga

def mas_larga(lista_palabras):
    palabra_larga = lista_palabras[0]  
    
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):
            palabra_mas_larga = palabra 
    return palabra_mas_larga

n = int(input("Ingrese el número de palabras: "))
lista_palabras = []
for i in range(n):
    palabra = input(f"Ingrese una palabra {i+1}: ")
    lista_palabras.append(palabra)

resultado = mas_larga(lista_palabras)
print("La palabra más larga es:", resultado)

#Ejercicio 3

def filtrar_palabras(lista_palabras, n):
    palabras_filtradas = [palabra for palabra in lista_palabras if len(palabra) > n]
    return palabras_filtradas

cadena_palabras = input("Ingrese las palabras separadas por comas: ")
lista_palabras = [palabra.strip() for palabra in cadena_palabras.split(',')]
n = int(input("Ingrese el número mínimo de caracteres: "))

resultado = filtrar_palabras(lista_palabras, n)
print(resultado)


#Ejercicio 4

def contador_mayusculas(cadena):
    contador = 0 
    for c in cadena:
        if c.isupper():
            contador += 1
    return contador

cadena = input("Escriba una frase: ")

resultado = contador_mayusculas(cadena)
print(f"La cadena tiene {resultado} cantidad de letras mayúsculas.")

#Ejercicio 5

def bin_a_int(binario):
    try:
        entero = int(binario, 2)
        return entero
    except ValueError:
        return "Error: Ingresa un número binario válido."
numbinario = input("Ingresa un número binario: ")
resultado = bin_a_int(numbinario)
print(resultado)


#Ejercicio 6

year = int(input("Ingrese el año: "))
personas = []
n = int(input("Ingresa el número de persona para saber su edad: "))
for i in range(n):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    year_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))

    edad = year - year_nacimiento
    personas.append((nombre, edad))

print("Info de las personas:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} años en el año {year}.")


#Ejercicio 7

edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

mayores_20 = sum(edad > 20 for edad in edades)
print(f"El número de personas mayores de 20 es de: {mayores_20}")


#Ejercicio 8




#Ejercicio 9

vocales = ["A", "E", "I", "O", "U", "Á", "É", "Í", "O", "Ú", "a", "e", "i", "o", "u", "á", "é", "í", "o", "ú"]

def contador_vocales(cadena):
    contador = 0 
    for c in cadena:
        if c in vocales:
            contador += 1
    return contador

cadena = input("Ingrese una frase: ")

resultado = contador_vocales(cadena)
print(f"La cadena tiene {resultado} vocales.")


#Ejercicio 10
year = int(input("Ingresa el año que deseas saber si es o no bisiesto: "))
if (year% 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("El año", year, "es bisiesto")
else:
    print("El año", year, "no es bisiesto")