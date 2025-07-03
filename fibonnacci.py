def imprimejogo(matriz):
    for linha in matriz:
        print(''.join(linha))
def atualizamatriz (matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz
       
