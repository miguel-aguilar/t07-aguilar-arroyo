import os
#declaracion de variables
x,y,=0,0
#imprimir los numeros que se encuentran  en cierto intervalo
#input
r=int(os.sys.argv[1])
p=int(os.sys.argv[2])

#ouput
print ("MOSTRAR EL INTERVALO QUE COMIENZE DESDE EL ", r ," Y TERMINE EN ", p)
print ("LUEGO A CADA UNO SUMARLE 2")
print("Rpta: ")

#iterador_rang
resultado = []

for suma in range(r,p):
    suma_mas_uno=(suma + 2)
    resultado.append(suma_mas_uno)

print (resultado)

#fin_iterador_rang
