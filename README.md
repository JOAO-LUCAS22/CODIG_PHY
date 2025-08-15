# INSTRUÇÕES

## inicio da aula.
Comandos:


1)Fazer login no GITHUB no navegador de internet
2)Fazer login no terminal 
```
"gh auth login"
```
```
Aperte a tecla "enter" até gerar o código
Copie o código gerado no terminal e cole no navegador de internet
```
3)Clonar o repositório usado nas aulas para o computador

```
"gh repo clone CODIG_PHY"
```
4)Entrar na pasta criada com o clone do repositório:
```
"cd CODIG_PHY"
```
5)Abrir VSCode pelo terminal
```
"code ."
```
codigo de calculo de notas
```

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
```
codigo de operações
```

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
```