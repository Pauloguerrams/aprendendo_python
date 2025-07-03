indiceReclamacao = input()
percentReclamResolPrim = input()
percentCliCancel = input()
indiceIndisponibilidade = input()
canceladoPorProblema = input()
indiceReclamacao = int(indiceReclamacao)
percentReclamResolPrim = int(percentReclamResolPrim)
percentCliCancel = int(percentCliCancel)
indiceIndisponibilidade = int(indiceIndisponibilidade)
canceladoPorProblema = int(canceladoPorProblema)



if (percentReclamResolPrim > 60):
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
print(f'{indice}')

if ( percentCliCancel <= 10):
    if (canceladoPorProblema==0):
        indice = indice + 80
    else:
        indice = indice - 30
else:
    if (canceladoPorProblema==0):
        indice = indice + 50
    else:
        indice = indice - 10
print(f'{indice}')

if (indiceIndisponibilidade> 10):
    indice = indice - 70
else:
    indice = indice + 20
print(f'{indice}')