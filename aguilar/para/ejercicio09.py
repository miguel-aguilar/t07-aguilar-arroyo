import os
#declaracion de variables
x=0

#input
x=int(os.sys.argv[1])
i=0
sumar=0

#ouput
print("ejercicio 02")
print("sumar los numeros pares desde el 0 hasta el ", x)
print("luego multiplicarlo por dos")
print("rpta:")

#sumar los x primeros numeros pares

while(i<=x):
    sumar += i
    i += 2

#fin_while

#procesing
total=(2*sumar)
print("la suma de todos los numeros pares desde el 0 hasta ", x ," y luego multiplicarlo por 2 es: ", total)
