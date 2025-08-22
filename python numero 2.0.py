import os
os.system("cls")

print("")      
num1 = float(input("Digite o primeiro número (operador): "))
print("")
num2 = float(input("Digite o segundo número (operando): "))
print("")

soma = num1 + num2

media = soma / 2

produto = num1 * num2

print("")
print(f"O resultado da soma é: {soma}")
print("")
print(f"O resultado da média é: {media}")
print("")
print(f"O resultado do produto entre eles é: {produto}")
print("")
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 == num2:
    print(f"{num1} é igual a {num2}")
else:
    print(f"{num2} é maior que o {num1}")
print("")
