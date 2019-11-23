import  os
# Sumar los P primeros numeros pares
# Declaracion de variable
P=0.0

#input
P=int(os.sys.argv[1])
i=0
suma=0

#ouput
print("ejercicio 05")
print("suma de 6 en 6 de los numeros naturales positivos desde el 0 hasta el: ", P)

while(i<=P):
    suma += i
    i += 6

#fin_while
print("la suma de 6 en 6 de  los 20 primeros numeros naturales positivos", suma)
