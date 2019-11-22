import os
#maraton de 100 metros

#declaracion de variables
corredor,escuela,distancia="","",0.0

#input
corredor=os.sys.argv[1]
escuela=os.sys.argv[2]
distancia=int(os.sys.argv[3])


#mientras que la distancia no sea la correcta, pedir una que si es correcta
#validador
while(distancia<0 or distancia>=101):
    distancia=int(input("ingrese la distancia correcta: "))

#fin_whiile

#ouput
print("MARATON 2019")
print("CORREDOR: ", corredor)
print("De la escuela de  ", escuela)
print("ha corrido un total de ", distancia , " metros")
print("buena carrera")

print("fin del bucle")
