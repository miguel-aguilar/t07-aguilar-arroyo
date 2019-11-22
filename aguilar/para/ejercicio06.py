import os
#declaracion de variables
x=0

#input
x=int(os.sys.argv[1])
i=0
sumar=0

#ouput
print("ejercicio 04")
print("sumar los numeros pares desde el 0 hasta el ", x)
print("luego elevarlo al cuadrado")
print("rpta:")

#sumar los x primeros numeros

while(i<=x):
    sumar += i
    i += 1

#fin_while

#procesing
total=(sumar**2)
print("la suma de los primeros numeros desde el 0 hasta ", x ," y luego elevarlo al cuadrado es: ", total)
