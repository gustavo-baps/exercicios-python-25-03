import math

r = int(input("insira o raio para calcular o volume da esfera: "))
vol = (4 * math.pi * (r ** 3))/3
print("o volume de uma esfera de raio %d é %.2f" %(r, vol))