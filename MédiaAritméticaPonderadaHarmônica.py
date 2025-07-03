n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
letra = input()
if(letra=='P'):
    print("Ponderada")
    p1,p2,p3 = input().split()
    p1=int(p1)
    p2=int(p2)
    p3=int(p3)
    p = (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)
    print(f'{p:.2f}')
elif(letra=='H'):
    print("Harmonica")
    h = 3/((1/n1)+(1/n2)+(1/n3))
    print(f'{h:.2f}')
elif(letra=='A'):
    print("Aritmetica")
    a = (n1+n2+n3)/3
    print(f'{a:.2f}')
else:
    print("Operacao inexistente")