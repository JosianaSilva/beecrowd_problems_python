vetor = []
for i in range(0,10):
    elemento = float(input())
    vetor.append(elemento)
tam = len(vetor)    
for i in range(tam):
    if(vetor[i]<=10):
        print('A[{}] = {}'.format(i, vetor[i]))