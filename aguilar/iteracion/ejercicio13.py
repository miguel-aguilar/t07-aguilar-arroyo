import os
#declaracion de variables
MSG=""

#MENSAJE INCRIPTADO
#INPUT
MSG=os.sys.argv[1].upper()

#ouput
print("MATEMATICA BASICA")
print("SEGUN LAS VARIABLES QUE QUEDEN SE DECIFRARA EL SEGUIENTE MENSAJE:")

#DESIFRAR EL SIGUIENTE MENSAJE

#bucle
for letra in MSG:
    if(letra == "V"):
        print("FELICIDADES")
    if(letra == "W"):
        print("MAL HECHO")
    if(letra == "X"):
        print("BIEN HECHO")
    if(letra == "Y"):
        print("SIGUE ASI")
    if(letra == "Z"):
        print("INTENTA DE NUEVO")
#fin_iterador

print("fin del bucle")
