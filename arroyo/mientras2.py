import os
#maraton de 100 metros

#declaracion de variables
comprador,nombre_de_la_tienda,monto="","",0.0

#input
comprador=os.sys.argv[1]
nombre_de_la_tienda=os.sys.argv[2]
monto=int(os.sys.argv[3])


#mientras que el monto no no esta en el intervalo entres 0 y 100  , pedir nuevamente
#validador
while(monto<0 or monto>=100):
    distancia=int(input("ingrese el monto correcto: "))

#fin_whiile

#ouput
print("BOLETA DE VENTA")
print("CLIENTE: ", comprador)
print("NOMBRE DE LA TIENDA  ", nombre_de_la_tienda)
print("ha comprado un total de ", monto , " s/")
print("buena compra")

print("fin del bucle")
