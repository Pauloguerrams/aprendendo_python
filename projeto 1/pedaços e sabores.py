sabor, pedaços = input("Você comeu qual sabor e quantos pedaços?").split()
pedaços = int(pedaços)
valor = pedaços * 3.25
if (pedaços == 1):
    print("foi",pedaços,"pedaço de bolo de",sabor,",então fica",valor,"reais")
else:
    print("Foram", pedaços, "pedaços de bolo de", sabor,", então fica", valor,"reais")