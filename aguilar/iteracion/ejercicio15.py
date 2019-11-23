import os
#declaracion de variables
mensaje=""

#MENSAJE INCRIPTADO
#INPUT
mensaje=os.sys.argv[1].upper()

#DESIFRAR EL SIGUIENTE MENSAJE

#ouput
print("su nombre es...")
print("pero de cariño le digo:", mensaje)
print("y le hice un acrostico el cual es: ")
#bucle
for letra in mensaje:
    if(letra == "C"):
        print("Chica sencilla que ")
    if(letra == "O"):
        print("Opaca al")
    if(letra == "R"):
        print("Resto")
    if(letra == "A"):
        print("Animando mi dia por completo")

#fin_iterador

print("fin del bucle")
