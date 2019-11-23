import  os
# Sumar los -y- primeros numeros
# Declaracion de variable
y=0.0

#input
y=int(os.sys.argv[1])
i=0
suma=0

#ouput
print("ejercicio 02")
print("suma los numeros desde el 0 hasta el: ", y)

while(i<=y):
    suma += i
    i += 1

#fin_while
print("la suma de los 200 primeros numeros", suma)
