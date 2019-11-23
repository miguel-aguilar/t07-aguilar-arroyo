import os
#declaracion de variables
w,z=0,0
#imprimir los numeros que se encuentran  en cierto rango
#input
w=int(os.sys.argv[1])
z=int(os.sys.argv[2])

#ouput
print ("Despues de resolver la inecuacion")
print("Dar como respuesta los numeros que tomaria la variable")
print("Rpta: ")

#iterador_rang
for numeros in range(w,z):
    print (numeros)

#fin_iterador_rang
