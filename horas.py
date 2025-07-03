horas, minutos, segundos = input().split(':')
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)
horas = (horas)*60
minutos = (horas + minutos)*60
segundos = minutos + segundos
print(f"La se foram {segundos} segundos que nao voltam mais...")
