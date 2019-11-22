import os
#compra limite

#declaracion de variables
cliente,producto,kg,pu="","",0.0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
kg=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total =float(pu * kg)

#mientras que la compra no sea la correcta o haya pasado el limite, dovelver algunos productos hasta tener lo necesario
#validador
while(total<0 or total>=1000):
    kg=int(input("ingrese el el nuevo total de kg: "))
    pu=float(input("ingrese el precio: "))
    total=(kg*pu)

#fin_whiile

#OUTPUT
print("#############################")
print("# BODEGA - ANITA")
print("#############################")
print("#")
print("# Cliente  : ", cliente)
print("# Producto :", producto)
print("# Item     : ",kg, "kg")
print("# P.U.     : ", pu)
print("# Total    : ", total)
print("#############################")

print("fin del bucle")
