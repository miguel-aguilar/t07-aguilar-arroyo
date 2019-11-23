import os
#declaracion de variables
x,y,z=0,0,0
#imprimir los numeros que se encuentran  en cierto intervalo

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
respuesta_de_la_operacion = []

for suma in range(x,y,z):
    resultado=(suma + 5)
    respuesta_de_la_operacion.append(resultado)

print (respuesta_de_la_operacion)

#fin_iterador_rang
