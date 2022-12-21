from http.client import PRECONDITION_FAILED
from re import L
from xml.etree.ElementInclude import LimitedRecursiveIncludeError


while True:
    litros_cliente = (float(input("Litros do combustível: ")))
    litros_cliente1 = int (litros_cliente)
    while litros_cliente1 <0:
        print ("Serviço Indisponível")
    else:
        continue
         
    
    while True:
        combustível_cliente = str(input("Combústivel desejado: \n [A] é Álcool \n [G] é Gasolina: "))
        if combustível_cliente != 'A' or combustível_cliente != 'G':
            print ("Serviço indisponível")
        elif combustível_cliente == 'A' or combustível_cliente == 'G':
            continue


        if combustível_cliente == "A":
            if litros_cliente1 <=20 and litros_cliente1 >0:
                preço_alcool = litros_cliente1 * 4.59
                print ("Seu preço é:{}".format(preço_alcool))
            elif litros_cliente1 >20:
                desconto_alcool = 0.05 
                preço_alcool = litros_cliente * 4.59
                alcool_com_desconto = preço_alcool - desconto_alcool
                print ("Seu preço é: {}".format(alcool_com_desconto))


        if combustível_cliente == "G":
            if litros_cliente1 <=40 and litros_cliente1 >0:
                preço_gasolina = litros_cliente1 *5.85
                print ("Seu preço é {}".format(preço_gasolina))
            elif litros_cliente1 >40:
                desconto_gasolina = 0.06
                preço_gasolina = litros_cliente1 *5.85
                gasolina_com_desconto = preço_gasolina - desconto_gasolina
                print ("Seu preço é: {}".format(gasolina_com_desconto))



