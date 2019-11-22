import os
#declaracion de variables
x=0

#input
x=int(os.sys.argv[1])
i=0
sumar=0

#ouput
print("ejercicio 05")
print("si es que sumas desde el 0 hasta el ", x)
print ("pero teniendo en cuenta de que vaya de 4 en 4")
print ("luego dividirlo entre 2")
print ("el resultado es:")

#sumar los x primeros numeros de 3 en 3


while(i<=x):
    sumar += i
    i += 4


#fin_while

#procesing
total=(sumar/2)

print("la suma de los ", x ," primeros numeros teniendo en cuenta de que va 4 en 4 y luego dividirlo entre 2 es igual a: ", total)
