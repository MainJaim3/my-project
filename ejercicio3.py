
import datetime

now = datetime.datetime.now()



def print_numero(x, es_hoy=False):
    if es_hoy:
        return f" *{x}* "
    else:
        return f" *{x}* "
    
texto_salida = "L M X J V S D \n"
dia_inicial_mes = 27

total_num = 7 * 6
contador = 0


def print_de_numero(param):
    pass


for i in range(total_num):
       dia = dia_inicial_mes + i
       if dia > 31:
           dia = dia - 31
       if now.day == dia:
           texto_salida = texto_salida + print_de_numero(str(dia))
           dia_inicial_mes = 0
           
    texto_salida = texto_salida + print_numero(str(dia))
    contador = (contador + 1)
   if contador == 7:
       texto_salida = texto_salida + "\n"
       contador = 0

print(texto_salida)