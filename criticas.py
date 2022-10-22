import time

print(" 📽 "*5)
print("Bem-Vindo")
print(" 📽 "*5)

atuação = (float(input("Nota da atuação: ")))
ambientação = (float(input("Nota da ambientação: ")))
Enredo = (float(input("Nota do roteiro: ")))
personagens = (float(input("Nota dos personagens: ")))
direção = (float(input("Nota da direção: ")))

média = (atuação + ambientação + Enredo + personagens + direção)
nota_final = média / 5

time.sleep(2)
print (" ")
print ("nota final:", nota_final)