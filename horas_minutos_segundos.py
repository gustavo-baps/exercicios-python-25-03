seg = int(input("insira a duração de um evento em segundos: "))
horas = seg/3600
minutos = (seg % 3600)/60
segundos = (seg%3600)%60
print("a duração no formato horas:minutos:segundos é %d:%d:%d"%(horas,minutos,segundos))