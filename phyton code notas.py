
import os
os.system("cls")

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
turma = input("Digite a turma: ")

unidade_I = float(input("Digite a nota referente à Unidade I: "))
print("")
unidade_II = float(input("Digite a nota referente à Unidade II: "))
print("")
unidade_III = float(input("Digite a nota referente à Unidade III: "))

soma = unidade_I + unidade_II + unidade_III
media = soma / 3

print("")
print(f"Olá professor, o aluno/a {nome} de {idade} anos, turma {turma}, obteve as seguintes notas:")
print("")
print(f"= = = BOLETIM = = =")
print("")
print(f"Unidade I: {unidade_I}")
print("")
print(f"Unidade II: {unidade_II}")
print("")
print(f"Unidade III: {unidade_III}")
print("")
print(f"Média final: {media:.2f}")
print("")
if media >= 6:
    print("APROVADO!!!!")
else:
    print("REPROVADO!!!")
print("")
