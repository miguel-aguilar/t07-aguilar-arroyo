import os
#declaracion de variables
m,n=0,0
#imprimir los numeros que se encuentran  en cierto intervalo

#input
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])

#ouput
print ("Despues de resolver la inecuacion racional ")
print("Dar como respuesta los numeros que hacen que la solucion exista")
print("Rpta: ")

#iterador_rang
for numeros_enteros in range(m,n):
    print (numeros_enteros)

#fin_iterador_rang
