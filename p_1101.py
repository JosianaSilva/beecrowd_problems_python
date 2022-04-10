# Sequência de Números e Soma
m,n=1,1
chave = True
while chave:
    aux,soma = 0,0
    entrada = input().split()
    m,n = int(entrada[0]),int(entrada[1])
    if((m!=0 and n!=0)and(m>0 and n>0)):
        if(m>n):
            aux = n
            for i in range(n,m+1):
                print(aux, end=" ")
                soma += aux
                aux +=1
            print('Sum=%i' %soma)
        elif(n>m):
            aux = m
            for i in range(m,n+1):
                print(aux, end=" ")
                soma += aux
                aux +=1
            print('Sum=%i' %soma)
    else:
        chave = False