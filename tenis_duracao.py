h1 = int(input("insira a hora em que a partida de tenis começou: "))
m1 = int(input("insira o minuto em que a partida de tenis começou: "))
s1 = int(input("insira os segundos em que a partida de tenis começou: "))
h2 = int(input("insira a hora em que a partida de tenis terminou: "))
m2 = int(input("insira o minuto em que a partida de tenis terminou: "))
s2 = int(input("insira os segundos em que a partida de tenis terminou: "))
hor = h2 - h1
min = m2 - m1
seg = s2 - s1
print("a duracao da partida foi de %d:%d:%d"%(hor, min, seg))