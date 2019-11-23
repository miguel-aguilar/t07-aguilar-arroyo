import  os
# Sumar los x primeros numeros pares
# Declaracion de variable
x=0.0

#input
x=int(os.sys.argv[1])
i=0
suma=0

#ouput
print("ejercicio 03")
print("suma de 3 en 3 de los numeros naturales positivos  desde el 0 hasta el: ", x)

while(i<=x):
    suma += i
    i += 3

#fin_while
print("la suma de 3 en 3 de  los 100 primeros numeros naturales positivos", suma)
