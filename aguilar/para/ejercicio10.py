import os
#declaracion de variables
x=0

#input
x=int(os.sys.argv[1])
i=0
sumar=0

#ouput
print("ejercicio 01")
print("sumar los numeros desde el 0 hasta el: ", x)
print("rpta:")

#sumar los x primeros numeros


while(i<=x):
    sumar += i
    i += 1


#fin_while

print("la suma de los ", x ," primeros numeros es: ", sumar)
