import os
os.system("cls")

numero = float(input("digite um número: "))

if numero > 10:
    print(f"{numero} É MAIOR QUE 10.")
elif numero == 10:
    print(f"{numero} É IGUAL A 10")
else:
    print(f"{numero} MENOR QUE 10")
    