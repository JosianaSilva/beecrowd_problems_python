#Fibonacci Fácil
n = int(input())

def escreva_sequencia(n):
    f1,f2=0,0
    for i in range(n):   
        if(i<2):
            fn = i
            f1 = fn
        else:
            fn = (f2)+(f1)
            f2 = f1
            f1 = fn
        if(i<n-1):
            print(fn,end=" ") 
        elif(i==n-1):
            print('{}'.format(fn))
if(n<=46 and n>0):
    escreva_sequencia(n)
#ACEITO! 12/12/2021