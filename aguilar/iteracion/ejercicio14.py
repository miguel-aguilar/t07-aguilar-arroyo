import os
#declaracion de variables
MSG=""

#MENSAJE INCRIPTADO
#INPUT
MSG=os.sys.argv[1].upper()

#ouput
print("COMUNICADO")
print("SEGUN LA AVERIGUACIONES, LA NASA HA DEJADO EL SIGUIENTE MENSAJE:" , MSG)
print("que significa: ")

#DESIFRAR EL SIGUIENTE MENSAJE

#bucle
for letra in MSG:
    if(letra == "C"):
        print("CUANDO ESCUCHEN")
    if(letra == "O"):
        print("POR UN ALTAVOZ")
    if(letra == "L"):
        print("LA PALABRA DEL MENSAJE")
    if(letra == "M"):
        print("TIENEN QUE")
    if(letra == "E"):
        print("INMEDIATAMENTE ")
    if(letra == "N"):
        print("OCULTARSE PARA NO SER")
    if(letra == "A"):
        print("ASESINADOS POR LOS ALIENIGENAS")
#fin_iterador

print("fin del bucle")

