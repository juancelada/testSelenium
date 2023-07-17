'''
def saludar():
    print("hola")

def salir():
    print("nos vemos")

saludar()


def suma(a,b):
    resultado= a + b
    print("la suma es: " + str(resultado))

suma(8,5) #aca definis el valor de los parametros a y b
salir()
'''


def datos(nom, sn, ap, am):
    print("tu nombre es: {} {} {} {}".format(nom, sn, ap, am))


datos("Franco", "Ariel", "Duperre", "")
datos("Claudia", "Alejandra", "Rionegro", "")
