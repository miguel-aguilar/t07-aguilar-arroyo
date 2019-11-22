import os
#crear cuenta de google

#declaracion de variables
usuario,correo,contraseña,edad="","","",0

#input
usuario=os.sys.argv[1]
correo=os.sys.argv[2]
contraseña=os.sys.argv[3]
edad=int(os.sys.argv[4])

#mientras que la edad no sea la correcta, pedir una que si es correcta
#validador
while(edad<0 or edad>=120):
    edad=int(input("ingrese la edad correcta: "))

#fin_whiile

#ouput
print("BIENVENIDO A GOOGLE")
print("Por favor llenar los siguientes espacios")
print("usuario: ", usuario)
print("correo electronico ", correo)
print("contraseña ", contraseña)
print("edad: ", edad)
print("iniciar sesion")

print("fin del bucle")
