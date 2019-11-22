import os
#reunion familiar

#declaracion de variables
nombre,motivo,dia="","",""

#input
nombre=os.sys.argv[1]
motivo=os.sys.argv[2]
dia=os.sys.argv[3]


#mientras que el dia no sea el correcto, pedir el dia que si es correcto
#validador
while(dia != "lunes" and dia != "martes" and
                  dia != "miercoles" and dia != "jueves" and
                  dia != "viernes" and dia != "sabado" and
                  dia != "domingo"):
    dia=input("ingrese el dia correcto: ")


#fin_whiile

#ouput
print("RECIBA ESTA CORDIAL INVITACION")
print("para: ", nombre)
print("se llevara a cabo este ", dia)
print("por el motivo que es ", motivo)
print("te esperamos")

print("fin del bucle")
