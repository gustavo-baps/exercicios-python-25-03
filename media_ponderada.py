n1 = int(input("insira a primeira nota do aluno (peso 2): "))
n2 = int(input("insira a segunda nota do aluno (peso 3): "))
n3 = int(input("insira a terceira nota do aluno (peso 5): "))
p1 = 2
p2 = 3
p3 = 5
med = ((n1 * p1) + (n2 * p2) + (n3 * p3))/(p1 + p2 + p3)
print("a média ponderada das notas do aluno é %.2f " %med)
