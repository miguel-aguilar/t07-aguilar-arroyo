import  os
# Sumar los -W- primeros numeros
# Declaracion de variable
W=0.0

#input
W=int(os.sys.argv[1])
i=0
suma=0

#ouput
print("ejercicio 04")
print("suma de 5 en 5 de los numeros naturales positivos desde el 0 hasta el: ", W)

while(i<=W):
    suma += i
    i += 5

#fin_while
print("la suma de 5 en 5 de los 20 primeros numeros naturales positivos", suma)
