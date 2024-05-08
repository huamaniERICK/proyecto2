# ESCRIBIR UN PROGRAMA QUE VERIFIQUE SI UN NUMERO INGRESADO POR EL USUARIO ES PAR Y POSITIVO.
numero=int(input("ingrese numero: "))
if numero >0 and numero % 2 == 0:
    print("el numero ingresado es positivo y par")
else:
    print("el numero ingresado no cumple co  las condiciones")


# escribir un programa que verifique si un año ingresado por el usuario es un año bisiesto
año=int(input("ingrese el año: "))
if (año % 4 == 0 and año % 100 !=0) or (año % 400 == 0):
    print("el año ingresado es un año bisiesto.")
else:
    print("el año ingresado no es un año bisiestol.")
    