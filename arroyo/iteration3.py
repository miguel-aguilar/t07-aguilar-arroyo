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
    if letra == "M":
        print("¿Que tal?")
    if letra == "A":
        print("¿Como estas hoy?")
    if letra == "R":
        print("Espero, que bien")
    if letra == "C":
        print("La otra semana te visitare")
    if letra == "O":
        print("PAra Jugar futbol")

#fin_iteration
print("/n")
print("Fin de bucle")
