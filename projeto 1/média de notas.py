# PMédia Ponderada
# Elabore um programa que lê três notas de um aluno, o peso de cada nota e apresenta a média final deste aluno


# A Entrada consiste de:
# uma linha contendo três números do tipo floats n1, n2 e n3, que representam as notas de um aluno.
# A segunda linha da entrada contém números três inteiros p1, p2 e p3, que representam os pesos de cada nota.

# A Saída deve apresentar:
# Uma linha com a média ponderada do aluno, com seis casas decimais.

# Observações:
# Não é necessário validar se os valores de entrada estão dentro dos tipos e intervalos definidos.

# Descrição dos Exemplos:
# No terceiro exemplo, a nota 9.1 tem peso 1, a nota 5.1 tem peso 2 e a nota 5.1 tem peso 3. Então a média ponderada resultante é 5.766667.
# Dica:

# Para ler mais de um valor por linha use a função split(), como mostrado a seguir, para ler 2 ou mais valores em uma mesma linha:
# x, y, z = input().split()

# Para quem quiser se aprofundar no funcionamento da função split() consulte a documentação de Python 3.x, em particular procure pelos métodos da classe str. 


# Por exemplo:

# Input	Resultado
# 10 10 10
# 1 1 1
# 10.000000
# 9 9 9
# 1 2 3
# 9.000000
# 9.1 5.1 5.1
# 1 2 3
# 5.766667
# Resposta:(penalty regime: 0, 0, 10, 20, ... %)

n1, n2, n3 =  input("quais foram suas três notas? ").split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

p1, p2, p3 = input("quais são os pesos de cada nota respectivamente? ").split()
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)

resposta = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)

print (f"{resposta:.6f}")