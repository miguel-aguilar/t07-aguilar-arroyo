import os
#declaracion de variables
x,y,z=0,0,0
#imprimir los numeros que se encuentran  en cierto rango en un solo intervalo
#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])

#ouput
print ("Mostrar el intervalo que va desde", x , " hasta ", y )
print ("pero que salte de ", z , " en ", z)
print ("luego a cada uno multiplicarlo por 2")
print("Rpta: ")

#iterador_rang
cuadradas = []

for cuadrada in range(x,y,z):
    multiplicacion=(cuadrada*2)
    cuadradas.append(multiplicacion)

print (cuadradas)

#fin_iterador_rang
