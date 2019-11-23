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
    if letra == "O":
        print("Hola")
    if letra == "I":
        print("Bebe")
    if letra == "A":
        print("Te quiero")
    if letra == "E":
        print("cuidate")
    if letra == "U":
        print("Adios")

#fin_iteration
print("Fin de bucle")
