# Escreva um programa que leia um caractere do teclado e o apresente de diversas formas diferentes.

# Entrada
# A entrada consiste de um único caractere que é garantidamente alfanumérico (uma letra alfabeto latino, maiúscula ou minúscula, ou um dígito).

# Saída
# A saída deve ser composta de 5 linhas, cada uma como apresentada a seguir.
# somente o caractere lido;
# duas vezes o caractere lido;
# duas vezes o caractere lido, separados por um espaço;
# a mensagem "2x" (onde x
#  deve ser substituído pelo caractere lido);
# o caractere lido, envolto em colchetes.
# Observações
# A formatação da saída é importante, saiba usar f-string.

# Por exemplo:

# Input	Resultado
# a
# a
# aa
# a a
# 2a
# [a]
# B
# B
# BB
# B B
# 2B
# [B]
# 5
# 5
# 55
# 5 5
# 25
# [5]






caractere = input("digite um caractere: ")
print(caractere)
print(f"{caractere*2}")
print(f"{caractere + ' ' + caractere}")
print(f"{'2'+ caractere}")
print(f"{'['+ caractere + ']'}")