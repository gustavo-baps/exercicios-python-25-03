import math

print("se delta resultar em 0 o programa quebra e eu NAO SEI RESOLVER")
a = int(input("insira o valor a da equação: "))
b = int(input("insira o valor b da equação: "))
c = int(input("insira o valor c da equação: "))
delta = (b ** 2) - (4 * a * c)
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)
print("as raizes da equação são %.2f e %.2f" %(x1, x2))