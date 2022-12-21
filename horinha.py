import datetime


x = datetime.datetime.now()
dianome = (x.strftime("%A"))
hora = x.hour 
minuto = x.minute
segundo = x.second
hora_atual = x.strftime("%X")
print(hora_atual)