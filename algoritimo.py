
import os
os.system("cls")

print("Olá usuário indique os dois números a serem operados")
print("")
num1 = float(input("Digite o primeiro número (operador): "))
print("")
num2 = float(input("Digite o segundo número (operando): "))

soma = num1 + num2

sub = num1 - num2

Mult = num1 * num2

Divide = num1 / num2

print("= = = RESULTADOS = = =")
print("")
print(f"Soma: {soma:.2f}")
print("")
print(f"Subtração: {sub:.2f}")
print("")
print(f"Multiplicação: {Mult:.2f}")
print("")
print(f"Divisão: {Divide:.2f}")
print("")
