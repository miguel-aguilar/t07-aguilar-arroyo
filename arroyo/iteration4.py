#Decodificador mensaje encriptado
import  os
#declaracion de variables
MSG=""

#input
MSG=os.sys.argv[1].upper()

#Ahora descubrir el siguiente enunciado
print("El mensaje descubierto es:")
#bucle
for letra in MSG:
    if letra == "S":
        print("Auxilio")
    if letra == "O":
        print("Necesito ayuda")
    if letra == "C":
        print("Rescatenme")
    if letra == "F":
        print("Mi barco se estrello")
    if letra == "B":
        print("Necesito proviciones")
    if letra == "I":
        print("Estoy con 13 soldados")


#fin_iteration
print("/n")
print("Fin de bucle")
