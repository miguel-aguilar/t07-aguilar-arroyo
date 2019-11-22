import os
#carta

#declaracion de variables
para,de,mes,mensaje="","","",""

#input
para=os.sys.argv[1]
de=os.sys.argv[2]
mes=os.sys.argv[3]
mensaje=os.sys.argv[4]


#mientras que el mes no sea el correcto, pedir el mes que si es correcto
#validador
while(mes != "enero" and mes != "febrero" and mes != "marzo" and
      mes != "abril" and mes != "mayo" and mes != "junio" and mes != "julio" and
      mes != "agosto" and mes != "setiembre" and mes != "octubre" and
      mes != "noviembre" and mes != "diciembre"):
    mes=input("ingrese el mes correcto: ")


#fin_whiile

#ouput
print("CARTA")
print("para: ", para)
print("de: ", de)
print("mes: ", mes)
print("mensaje: ", mensaje)
print("espero tu respuesta")

print("fin del bucle")
