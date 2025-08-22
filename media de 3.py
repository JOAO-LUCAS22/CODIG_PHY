import os
os.system("cls")

n1 = float(input("Digite a nota 1: \n"))
n2 = float(input("Digite a nota 2: \n"))
n3 = float(input("Digite a nota 3: \n"))

soma = n1 + n2 + n3

media = soma / 3

print("= = = = = = NOTAS = = = = = =")
print("")
print(f"UNIDADE I: {n1}")
print("")
print(f"UNIDADE I: {n1}")
print("")
print(f"UNIDADE I: {n1}")
print("")
print(f"Média: {media:.2f}")
print("")
if media >= 7:
    print("APROVADO!!!!!!!!!")
else:
    print("REPROVADO!!!!!!!!!!")
print("")