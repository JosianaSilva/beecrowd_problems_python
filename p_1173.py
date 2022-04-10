elemento = int(input())
if(elemento<=50):
    vetor = []
    vetor.append(elemento)
    for i in range(1,10):
        elemento *= 2
        vetor.append(elemento)

    for i in range(10):
        print('N[{}] = {}'.format(i, vetor[i]))