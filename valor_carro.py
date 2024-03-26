val = float(input("insira o valor de fabrica do carro novo: "))
imp_dist = (val/100) * 28
imp = (val/100) * 45
val_total = val + imp + imp_dist
print("o valor total do carro com a porcentagem do distribuidor de %.2f + impostos de %.2f é %.2f"%(imp_dist, imp, val_total))
