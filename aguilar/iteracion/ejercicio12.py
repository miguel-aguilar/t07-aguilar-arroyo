import os
#declaracion de variables
mensaje=""

#MENSAJE INCRIPTADO
#INPUT
mensaje=os.sys.argv[1].upper()

#DESIFRAR EL SIGUIENTE MENSAJE

#ouput
print("al subrayar la palabra clave")
print("nos dimos cuenta que habia un mensaje oculto:")
print("el cual era:")
#bucle
for letra in mensaje:
    if(letra == "A"):
        print("tienes")
    if(letra == "M"):
        print("una excelente")
    if(letra == "O"):
        print("comprension")
    if(letra == "R"):
        print("de textos")

#fin_iterador

print("fin del bucle")
