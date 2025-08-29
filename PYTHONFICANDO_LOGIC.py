
import os
os.system("cls")

login = str("joao157")
senha = str("gaymer")

l = str(input("Login: "))
s = str(input("Password: "))

if l == login and s == senha:
    print("Bem vindo playboyzinho")
elif l==login and s != senha:
    print("Senha invalida")
elif l!=login and s == senha:
    print("Usuário invalido")
else:
    print("Entrada invalida receba virus!!!")
