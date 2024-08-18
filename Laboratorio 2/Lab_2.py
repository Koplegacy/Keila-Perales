#función que nos imprima el numero mayor de una lista de n numeros

def numero_mayor():
    n = int(input("Cantidad de datos a ingresar: "))
    if n<=0:
        print("Ingrese una cantidad válida: ")
        return
    numeros=[]
    for a in range(n):
        numero = float(input("Dime un número {a+1} : "))
        numeros.append(numero)
    mayor= max(numero_mayor)
    print("El mayor de los numeros es {mayor}") 