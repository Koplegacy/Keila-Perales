#Ejercicio 1
#Una función para definir el máximo entre dos numeros
x = float(input("Di un número:"))
y = float(input("Di otro número:"))
if y > x:
    print("El número mayor es ",y)
elif x > y:
    print("El número mayor es ",x)
else:
    print("Es el mismo número")

#Ejercicio 2
# #Una función para definir el máximo entre tres numeros

k = float(input("Dime un número:"))
m = float(input("Dime otro número:"))
r = float(input("Dime un número más:"))

if k>m and k>r:
    print("El número mayor es ",k)
elif m>k and m>r:
    print("El número mayor es ",m)
elif r>k and r>m:
    print("El número mayor es ",r)
else:
    print("Es el mismo número")
#Ejercicio 3
#Una función para contar el numero de elementos en una lista
def calcular_longitud(objeto):
    contador = 0
    for _ in objeto:
        contador += 1
    return contador

porcontar = [input("Introduce un texto:")]
print("La longitud del texto es:", calcular_longitud(porcontar))


#Ejercicio 4
#Tome un carácter y especifique si es vocal o consonante
z = input("Introduzca una letra:")
vocales = 'aeiou'
if z in vocales:
    print(True)
else:
    print(False)


#Ejercicio 5
#Escribir una función que sume y mmultiplique los elementos de una lista a la vez

#Ejercicio 6
#Definir una función inversa
palabra= input("Ingresa un texto: ")
palabra_invertida = palabra [::-1]
print(palabra_invertida)

#Ejercicio 7
#Identificar palabas que se escriben igual al derecho y al revés

palab = input("Ingresa una palabra: ")
palab_invertida = palab [::-1]
if palab == palab_invertida:
    print(True)
else:
    print(False)

#Ejercicio 8
#Verificar si dos listas tienen al menos un elemento en común


#Ejercicio 9
#Definir una funcion que genere caracteres, tome un entero n y devuelva el caracter multiplicado por n
#queremos que lo repita 10 veces

v = input("Introduzca una palabra o caracter: ")
print(v*10)

#Ejercicio 10
#Definir un procedimiento  que tome una lista e imprima el histograma de esta

def imprimir_histograma(lista):
    for valor in lista:
        print('*'*valor)

numeros = [5,7,8,3,4]
imprimir_histograma(numeros)


