a=60
b=60
c=60

if(a<b):
    print("El mayor es A")
else:
    print("El mayor es B")

nom="Juan"
if(nom=="Juan"):
    print("Tu nombre es: " + nom)

if(a<=b):
    print("{} es menor o igual a {}".format(a,b))
else:
    print("{} es mayor a {}".format(a,b))

if(a!=b):
    print("A es diferente que B")
else:
    print("son iguales")

if(a>b and a>c):
    print("el mayor es : "+str(a))
elif(b>a and b>c):
    print("El mayor es: "+str(b))
elif(c>a and c>b):
    print("El mayor es: "+str(c))
else:
    print("niguna se cumple")

