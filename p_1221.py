#Primo Rápido
n = int(input())
for i in range(n):
    x = int(input())
    primo = True
    if(x==1): primo = False
    if(x%2==0 and x!=2): primo = False
    if (x==3): primo = True
    else:
        cont = 5
        while(cont<x):
            if (x%cont==0):
                primo = False
                break
            cont += 2
    if(primo==True):
        print('Prime')
    else:
        print('Not Prime')