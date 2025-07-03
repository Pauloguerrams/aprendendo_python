import math
xa =int(input())
ya = int(input())
xb = int(input())
yb = int(input())
distancia = (xb-xa)**2 + (yb-ya)**2
distancia = math.sqrt(distancia)
if(distancia<=100):
    print("É o amor da minha vida!")
elif(100<distancia<=200):
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")