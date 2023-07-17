'''
def suma(a, b):
    c=a+b
    print("la suma es: "+str(c))

suma(5,6)
'''
def suma(*args):
    res=0
    for n in args:
        res=res+n
    print(res)


suma(8,6,7,9,4,5,6,4)