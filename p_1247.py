#Guarda Costeira || Maratona
import math
while True:
    try:
        d, vf, vg = input().split()
        d = int(d)
        vf = int(vf)
        vg = int(vg)
        percurso_fugitivo = 12/ int(vf)
        percurso_guarda_costeira = math.sqrt((d**2 + 144)) / int(vg)
        #print('Fugitivo: {:.2f} h || Guarda Costeira: {:.2f} h'.format(percurso_fugitivo,percurso_guarda_costeira))
        if((1<=vg<=100)and(1<=d<=100)and(1<=vf<=100)):
            if(percurso_guarda_costeira <= percurso_fugitivo):
                print("S")
            else:
                print("N")
    except EOFError:
        break

#ACEITO! 12/12/2021