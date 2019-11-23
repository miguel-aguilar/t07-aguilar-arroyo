import os
#INVITACION

#declaracion de variables
para,cumpleañero,mes,invitacion="","","",""

#input
para=os.sys.argv[1]
cumpleañero=os.sys.argv[2]
mes=os.sys.argv[3]
invitacion=os.sys.argv[4]


#mientras que el mes no sea el correcto, pedir el mes que si es correcto
#validador
while(mes != "enero" and mes != "febrero" and mes != "marzo" and
      mes != "abril" and mes != "mayo" and mes != "junio" and mes != "julio" and
      mes != "agosto" and mes != "setiembre" and mes != "octubre" and
      mes != "noviembre" and mes != "diciembre"):
    mes=input("ingrese el mes correcto: ")


#fin_whiile

#ouput
print("INVITACION DE CUMPLEAÑOS")
print("Para: ", para)
print("De: ", cumpleañero)
print("Mes: ", mes)
print("Mensaje: ", invitacion)
print("TE espero con ansias,")
print("NO OLVIDAR; REGALOS")

print("fin del bucle")
