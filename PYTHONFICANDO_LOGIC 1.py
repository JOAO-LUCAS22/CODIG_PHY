
import os
os.system("cls")

l = input("Login: ")
s = input("Senha: ")
login_salvo = "John_Slverhand"
senha_salva = "Engraçaralho pra cadinho"
if l == login_salvo and s == senha_salva:
    print("Bem-vindo, playboyzinho 😎")
elif l == login_salvo and s != senha_salva:
    print("Senha inválida!")
elif l != login_salvo and s == senha_salva:
    print("Usuário inválido!")
else:
    print("Entrada inválida, receba vírus!!! 💀")

