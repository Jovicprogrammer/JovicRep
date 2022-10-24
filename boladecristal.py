
import time
import random

("🔮"*10)
(print ("Faça qualquer pergunta de sim ou não, \n e eu sabiamente responderei"))
("🔮"*10)

time.sleep(2)
print (" ")

pergunta = (str(input("Sua pergunta: ")))

resposta = random.randrange (1,5)
if resposta == 1:
    time.sleep(2)
    print ("*✧･ﾟ: *✧･.ﾟ:")
    time.sleep(1)
    print ("Sim")

if resposta == 2:
    time.sleep(2)
    print ("*✧･ﾟ: *✧･ﾟ:")
    time.sleep(1)
    print ("Não")

if resposta == 3:
    time.sleep(2)
    print ("*✧･ﾟ: *✧･ﾟ:")
    time.sleep(1)
    print ("Talvez")

if resposta == 4:
    time.sleep(2)
    print ("*✧･ﾟ: *✧･ﾟ:")
    time.sleep(1)
    print ("Complicado")




