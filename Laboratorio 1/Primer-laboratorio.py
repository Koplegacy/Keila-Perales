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


#Ejercicio 4
#Tome un carácter y especifique si es vocal o consonante
z = input("Introduzca una letra:")
vocales = 'aeiou'
if z in vocales:
    print(True)
else:
    print(False)
