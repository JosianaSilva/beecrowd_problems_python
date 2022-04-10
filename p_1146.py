#Sequências crescentes
while True:
    n = int(input())
    if (n==0):
        break
    for i in range(1,n+1):
        if(i==n):
            print('{}'.format(n))
        else:
            print(i,end=" ")
#ACEITO! 14/12/2021
#   OUTRA SOLUÇÃO:
#   while True:
#       n = int(input())
#       if n == 0: break
#       print(' '.join(map(str, range(1, n + 1))))