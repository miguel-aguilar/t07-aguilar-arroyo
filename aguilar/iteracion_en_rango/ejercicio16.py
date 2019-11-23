import os
#declaracion de variables
x,y,z=0,0,0
#imprimir los numeros que se encuentran  en cierto rango en un solo intervalo
#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])

#ouput
print ("MOSTRAR EL RANGO QUE EMPIECE DESDE EL ", x ," Y TERMINE EN ", y)
print("PERO QUE SE SALTE DE ", z , " en ", z)
print("Rpta: ")

#iterador_rang
even_numbers = list(range(x,y,z))
print (even_numbers)

#fin_iterador_rang
