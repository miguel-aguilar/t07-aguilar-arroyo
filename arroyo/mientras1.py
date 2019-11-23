import os
#reunion familiar

#declaracion de variables
Alumno,motivo,dia="","",""

#input
Alumno=os.sys.argv[1]
motivo=os.sys.argv[2]
dia=os.sys.argv[3]


#mientras que el dia de la semana  no sea el correcto, pedir el dia que si es correcto
#validador
while(dia != "lunes" and dia != "martes" and
                  dia != "miercoles" and dia != "jueves" and
                  dia != "viernes" and dia != "sabado" and
                  dia != "domingo"):
    dia=input("ingrese el dia correcto: ")


#fin_whiile

#ouput
print("NOTIFICACION PARA EL ALUMNO")
print("para: ", nombre)
print("se llevara a cabo este ", dia)
print("por el motivo que es ", motivo)
print("Si no viene sus padres, se bajara la nota en su conducta")

print("fin del bucle")
