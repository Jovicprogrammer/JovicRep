from platform import python_version
import sys

versao = sys.version

print (versao)

numero = int(input("Número para verificação: "))
num1, num2 = 0, 1
contador = 0

while contador < numero:
    num3 = num1 + num2
    if num3 == numero:
        print ("Termo encontrado")
        break

    num1 = num2
    num2 = num3
    contador += 1