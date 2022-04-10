#Flores de Fogo com tratamento de erro EOF (end of file)
import math
PI = math.pi
chave =  True
while chave:
    try:
        entrada = input().split()
        #círculo do caçador
        r1,x1,y1 = int(entrada[0]),int(entrada[1]),int(entrada[2]) 
        #círculo da flor
        r2,x2,y2 = int(entrada[3]),int(entrada[4]),int(entrada[5])

        if(r1>=1 and r2<=1000 and y2<=1000):
            area1 = PI*(r1**2)
            area2 = PI*(r2**2)
            def esta_contido(a1,a2):
                if(a2>a1):
                    resultado = False
                else:
                    dist_centro = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
                    if(r1 >= (dist_centro+r2)): 
                        resultado = True
                    else:
                        resultado = False
                return resultado
        if (esta_contido(area1,area2) == True):
            print("RICO")
        else:
            print("MORTO")
    except EOFError:
        break

# ACEITO! 12/12/2021