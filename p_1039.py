#Flores de Fogo
import math
PI = 3.1415
def teste(leitura):
    if(not leitura):
        key = False
    else: 
        key = True
    return key

entrada = input().split()
chave = teste(entrada)
while (chave is True):
    #círculo do caçador
    r1,x1,y1 = int(entrada[0]),int(entrada[1]),int(entrada[2]) 
    #círculo da flor
    r2,x2,y2 = int(entrada[3]),int(entrada[4]),int(entrada[5])
    area1 = PI*(r1**2)
    area2 = PI*(r2**2)
    def esta_contido(a1,a2):
        if(a2>a1):
            resultado = False
        else:
            dist_centro = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
            if(r1 > (dist_centro+r2)): 
                resultado = True
            else:
                resultado = False
        return resultado
    if (esta_contido(area1,area2) == True):
        print("RICO")
    else:
        print("MORTO")
    entrada = input().split()
    chave = teste(entrada)