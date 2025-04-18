import random
import time

opcoes = ["pedra", "tesoura", "papel"]
opcoes2 = ["🏔️", "✂️", "📝"]
placar_j = 0
placar_c = 0

def traducao(palavra, conjunto1, conjunto2):
    indice = conjunto1.index(palavra)
    return conjunto2[indice]


def valida_input(palavra, conjunto):
    if palavra in conjunto:
        return(True)
    elif palavra == "sair":
        return(True)
    else: 
        return(False)

def venceu(p, c):
    if p == c:
        return "empate"
    elif (p, c) in [("pedra", "tesoura"), ("tesoura","papel"), ("papel", "pedra")]:
        return "jogador"
    else:
        return "computador"
 

while True:
    jogador = input("Qual é sua escolha?").lower()

    if not valida_input(jogador, opcoes):
        print("Opção inválida!")
        continue
    
    if jogador == "sair":
        break

    computador = random.choice(opcoes)  
    time.sleep(1)
    print(f"{'o computador escolheu: ' + computador + ' ' + traducao(palavra = computador, conjunto1 = opcoes, conjunto2 = opcoes2)}")
    vencedor = venceu(jogador, computador)
    
    time.sleep(1)
    if vencedor == "jogador":
        placar_j = placar_j + 1
        print("jogador fez 1 ponto!")
    elif vencedor == "computador":
        placar_c = placar_c + 1
        print("computador fez 1 ponto!")
    else:
        print("empatou")
    
    time.sleep(1)
    print(f"{'póxima rodada o placar está:'}")
    print(f"{'jogador: ' + str(placar_j) + ' X computador: '+ str(placar_c)}")

time.sleep(1)
print(f"{'O jogo acabou 😊 placar final'}")
print(f"{'jogador: ' + str(placar_j) + ' X computador: '+ str(placar_c)}")
