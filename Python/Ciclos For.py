'''
for x in range(1):
    print("franco" + str(x))  #ciclos de repeticion

colores=["rojo", "verde", "amarillo", "azul", "magenta"] #lista
for vcol in colores:
    print(vcol)


nom="Franco Ariel Duperre"
for vnom in nom:
    print(vnom)
'''
'''
for x in range(10,20): #rango entre 10 y 20
    print(x)
'''
'''
for n in range(0,101,7): #0 al 101 con incrementos de 5
    if(n >=90):
        break
    print(n)
'''


for num in range(10):
    if(num==3 or num==6 or num==5):     #sirve par no ejecutar ciertos valores especificos en el ciclo for
        continue                        #puede servir para las selecciones de checkbox en tablas
    print(num)