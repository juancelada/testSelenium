texto = "Hola bienvenido a Python"

print(texto)

print(texto[3]) #imprime solo el valor de la posicion 3 en la cadena de texto

print(texto[5:12])

print(texto[5:])

print(texto[-6:])

print("##############################################################################################################################################################################")

print("FUNCIONES CON CADENAS")
nombre="juan"
print(nombre.upper()) #
print(nombre.lower())
print(nombre.capitalize())

cadena="php, java, selenium, javascript"

print(cadena.split(','))

print("##############################################################################################################################################################################")

print("IMPRIMIR CADENAS")


nom="juan"
ape="perez"
am="lara"

print("Tu nombre es {} tu apellido es {} tu apellido materno es {}" .format(nom,ape,am)) #con las llaves mandas a llamar a las variables en el orden que estan dentro de la funcion

print("Tu nombre es {} {} {} " .format(nom,ape,am))

