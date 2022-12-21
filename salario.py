
from re import X


ganho_por_hora = float(input("Quanto você ganha por hora: "))
horas_trabalhadas = int(input("Horas trabalhadas por mês: "))

salario_mensal = horas_trabalhadas * ganho_por_hora

print ("Seu salário é:" , salario_mensal)

imposto_de_renda = salario_mensal / 100 
porcentagem_imposto = imposto_de_renda * 11

inss = salario_mensal / 100
porcentagem_inss = inss * 8

sindicato = salario_mensal / 100
porcentagem_sindicato = sindicato * 5

salario_final1 = porcentagem_imposto + porcentagem_inss + porcentagem_sindicato
salario_restante = salario_mensal - salario_final1

print ("o saldo restante é de: " , salario_restante)