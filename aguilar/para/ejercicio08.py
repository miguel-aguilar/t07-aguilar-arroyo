import os
#declaracion de variables
x=0

#input
x=int(os.sys.argv[1])
i=0
sumar=0

#ouput
print("ejercicio 03")
print("si es que sumas desde el 0 hasta el ", x)
print ("pero teniendo en cuenta de que vaya de 3 en 3")
print ("el resultado es:")

#sumar los x primeros numeros de 3 en 3


while(i<=x):
    sumar += i
    i += 3


#fin_while

print("la suma de los ", x ," primeros numeros teniendo en cuenta de que va 3 en 3 es: ", sumar)
