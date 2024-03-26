print("=====PESQUISA: Quantos dias você perdeu?===")
nome = input("por favor, insira seu nome: ")
cig = int(input("quantos cigarros você fuma por dia? "))
anos = int(input("e há quantos anos você fuma? "))
dias_anos = anos * 365
print("você fuma %d cigarros por dia" %cig)
total_cig = cig * dias_anos
print("desde que começou, você fumou um total de %d cigarros em %d dias"%(total_cig, dias_anos))
print("esses cigarros lhe custaram o tempo que você passará aqui, essa foi sua única chance e sua decisão foi estragá-la com %d cigarros"%total_cig)
dias_perdidos = ((cig * 10)/1440)*dias_anos
print("você perdeu um total de %.2f dias de vida."%dias_perdidos)
print(nome, ", não acha melhor parar?")