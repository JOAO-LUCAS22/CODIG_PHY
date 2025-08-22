
import os
os.system("cls")

def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir (a, b):
    if b!=0:
        return a / b
    else:
        print("erro divisão por zero")
        
def calculadora():
    while True:
        print("\n= = = = = = CALCULADORA SIMPLES = = = = = =")
        print("")
        print("1 - soma")
        print("")
        print("2 - subtrair")
        print("")
        print("3 - multiplicar")
        print("")
        print("4 - dividir")
        print("")
        print("5 - sair")
        print("")
        
        escolha = input("Escolha uma opção (1/2/3/4/5): ")
        
        if escolha == "5":
            print("Encerrando calculadora.")
            break
                 
        print("")      
        num1 = float(input("Digite o primeiro número (operador): "))
        print("")
        num2 = float(input("Digite o segundo número (operando): "))
        print("")

        if escolha == "1":
            resultado = soma(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == "2":
            resultado = subtrair(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == "3":
            resultado = multiplicar(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == "4":
            resultado = dividir(num1, num2)
            print("Resultado: ", resultado)
        else:
            print("Opção invalida")
            
if __name__ == "__main__":
    calculadora()