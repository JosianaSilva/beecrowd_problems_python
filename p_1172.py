vetor = []
for i in range(0,10):
    elemento = int(input())
    if (elemento > 0):
        vetor.append(elemento)
    elif (elemento <= 0):
        vetor.append(1)


for i in range(10):
    print('X[{}] = {}'.format(i, vetor[i]))

