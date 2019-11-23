import  os
# Sumar los x primeros numeros pares
# Declaracion de variable
x=0.0

# input
x=int(os.sys.argv[1])
i=1
suma=0

#ouput
print("ejercicio 01")
print("sumar los numeros pares naturales positivos desde el 0 hasta el ", x)

#La sumas de los 50 numeros paraes positivos
while(i<=x):
    suma += i
    i += 2

#fin_while
print("la suma de los 50 primeros numeros pares", suma)
