import os
#declaracion de variables
x,y,=0,0
#imprimir los numeros que se encuentran  en cierto rango en un solo intervalo
#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

#ouput
print ("MOSTRAR EL RANGO QUE EMPIECE DESDE EL ", x ," Y TERMINE EN ", y)
print ("LUEGO A CADA UNO ELEVARLO AL CUADRADO")
print("Rpta: ")

#iterador_rang
cuadradas = []

for cuadrada in range(x,y):
    al_cuadrado=(cuadrada**2)
    cuadradas.append(al_cuadrado)

print (cuadradas)

#fin_iterador_rang
