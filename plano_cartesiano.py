import math
p1x = int(input("insira o valor A do ponto 1: "))
p1y = int(input("insira o valor B do ponto 1: "))
p2x = int(input("insira o valor A do ponto 2: "))
p2y = int(input("insira o valor B do ponto 2: "))
dab = math.sqrt(((p2x - p1x)**2) + ((p2y - p1y)**2))
print("a distancia entre p1 e p2 é %.2f" %dab)