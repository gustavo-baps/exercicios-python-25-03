val = int(input("insira um valor em dinheiro: "))
n100 = int(val/100)
val = val - (n100 * 100)
n50 = int(val/50)
val = val - (n50 * 50)
n10 = int(val/10)
val = val - (n10 * 10)
n5 = int(val/5)
val = val - (n5 * 5)
n2 = int(val/2)
val = val - (n2 * 2)
n1 = val

print("para completar esse valor seriam necessárias %d notas de 100, %d de 50, %d de 10, %d de 5, %d de 2 e %d de 1"%(n100,n50,n10,n5,n2,n1))