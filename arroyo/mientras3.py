import os
#compra limite

#declaracion de variables
comprador,producto,kg,pu="","",0.0,0.0

#INPUT
comprador=os.sys.argv[1]
producto=os.sys.argv[2]
kg=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total =float(pu * kg)

#mientras que la compra no sea la correcta o haya pasado el monto que tiene, verificar bien su dinero
#validador
while(total<0 or total>=1000):
    kg=int(input("ingrese el el nuevo total de kg: "))
    pu=float(input("ingrese el precio: "))
    total=(kg*pu)

#fin_whiile

#OUTPUT
print("#############################")
print("# TIENDA - PEPITO")
print("#############################")
print("#")
print("# Cliente  : ", comprador)
print("# Producto :", producto)
print("# Item     : ",kg, "kg")
print("# P.U.     : ", pu)
print("# Total    : ", total)
print("#############################")

print("fin del bucle")
