#Primo Rápido
import math
n = int(input())

for i in range(n):
    x = int(input())
    primo = True
    if (x<2): 
        primo = False
    if (x==2):
        primo = True
    if (x==3):
        primo: True
    
    if(x%2==0 and x!=2):
        primo = False
    else:
        cont = 3
        root = int(math.sqrt(x))
        while(cont<=root):
            if (x%cont==0):
                primo = False
                break
            cont += 2

    if(primo==True):
        print('Prime')
    else:
        print('Not Prime')
# ACEITO 21/12/2021