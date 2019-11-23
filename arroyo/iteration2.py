#Decodificador mensaje encriptado
import  os
#declaracion de variables
codigo=""

#input
codigo=os.sys.argv[1].upper()

#Ahora descubrir el siguiente enunciado
print("El mensaje descubierto es:")

#bucle
for letra in codigo:
    if letra == "P":
        print("Hoy")
    if letra == "E":
        print("te extraño")
    if letra == "D":
        print("mas que")
    if letra == "R":
        print("nunca, te quiero")
    if letra == "O":
        print("mucho")
#fin_iteration
print("/n")
print("Fin de bucle")
