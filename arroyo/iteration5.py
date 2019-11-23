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
    if letra == "C":
        print("Estoy en el restaurante")
    if letra == "A":
        print("El individuo acaba de llegar")
    if letra == "F":
        print("Esten atentos a sus movimientos")
    if letra == "E":
        print("Esta con polo azul")
    if letra == "T":
        print("Pantalon negro")
    if letra == "A":
        print("zapatos oscuros")


#fin_iteration
print("/n")
print("Fin de bucle")
