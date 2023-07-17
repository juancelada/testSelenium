lenguajes = ["java", "php", "Python", "C#"]

print("Lenguaje Seleccionado: " + lenguajes[2])
lenguajes[2] = "tu vieja"

print("Lenguaje seleccionado: " + lenguajes[2])

lenguajes.append("tu mama")    #agrega un valor mas a la lista, al final de la misma
print(lenguajes)

lenguajes.remove("java")  #remueve un valor de la lista
print(lenguajes)