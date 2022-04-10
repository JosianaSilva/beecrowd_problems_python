inicio = input().split()
horario_inicial = input().split(":")
if (inicio[1].isdigit() == True):
    dia_inicial = int((inicio[1]))
hora_inicial = int(horario_inicial[0])
minuto_inicial = int(horario_inicial[1])
segundo_inicial = int(horario_inicial[2])

fim = input().split()
horario_final = input().split(":")
if (fim[1].isdigit() == True):
    dia_final = int((fim[1]))
hora_final = int(horario_final[0])
minuto_final = int(horario_final[1])
segundo_final = int(horario_final[2])

dias = dia_final - dia_inicial

if (hora_final < hora_inicial):
    hora_final += 24
    dias -= 1
horas = hora_final - hora_inicial

#if ((hora_final < hora_inicial) or (hora_final==hora_inicial and (minuto_final<minuto_inicial or minuto_final==minuto_inicial))):
#   hora_final += 2

if (minuto_final < minuto_inicial):
    minuto_final += 60
    horas -= 1
minutos = minuto_final - minuto_inicial

if (segundo_final < segundo_inicial):
    segundo_final += 60
    minutos -= 1    
segundos = segundo_final - segundo_inicial

print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))

