import os
#Comprar un pasaje

#declaracion de variables
nombre,apellido,destino,edad="","","",0

#input
nombre=os.sys.argv[1]
apellido=os.sys.argv[2]
destino=os.sys.argv[3]
edad=int(os.sys.argv[4])

#mientras que la edad no sea el correcta, pedir nuevamente
#validador
while(edad<0 or edad>=110):
    edad=int(input("ingrese la edad correcta para terminar el proceso : "))

#fin_whiile

#ouput
print("AEROLINEA VIVA AER")
print("LLENAR LOS REQUISITOS PEDIDOS")
print("NOMBRE: ", nombre)
print("APELLIDO ", apellido)
print("DESTINO ", destino)
print("edad: ", edad)
print("FELICIDADES; Que tenga un buen viaje")

print("fin del bucle")
