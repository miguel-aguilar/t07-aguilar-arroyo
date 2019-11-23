import os
#declaracion de variables
MSG=""

#MENSAJE INCRIPTADO
#INPUT
MSG=os.sys.argv[1].upper()

#DESIFRAR EL SIGUIENTE MENSAJE

#ouput
print("COMUNICADO")
print("LA OFICINA GENERAL LE DEJA EL SIGUIENTE MENSAJE:")

#bucle
for letra in MSG:
    if(letra == "A"):
        print("Buenas tardes")
    if(letra == "E"):
        print("Mucho gusto")
    if(letra == "I"):
        print("Espero tenga un")
    if(letra == "O"):
        print("Buen dia")
    if(letra == "U"):
        print("Mal dia")
#fin_iterador

print("fin del bucle")
