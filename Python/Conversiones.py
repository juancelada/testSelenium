a=20
b=20
nom = "Franco"
print("el valor de a es: "  + str(type(a)))

print("el valor de b es: "  + str(type(b)))

print("la suma es: " + str(a+b))  # se convierte las variables en String ya que estas imprimiendo sobre una cadena de texto

a=str(a)
b=str(b)
print("ahora el valor de a es: " + str(type(a)))

print("a es igual a: " + a) #ahora funciona sin str ya q    ue lo convertimos en String en la linea anterior
                            #ahora que son string no se puden sumar como valores

