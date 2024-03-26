sal = float(input("insira seu salario fixo: "))
vend = float(input("insira o valor total de suas vendas no mês: "))
por_com = (15/100) * vend
print("o valor de sua comissão é de %.2f" %por_com)
print("o seu salario total será de %.2f"%(sal + por_com))

