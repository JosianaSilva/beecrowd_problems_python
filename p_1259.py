# Pares e Ímpares
pares = []
impares = []

def mostra_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

def ordena_Crescente(lista):
    tam = len(lista)
    for index in range(0, tam):
        min_index = index

        for right in range(index + 1, tam):
            if lista[right] < lista[min_index]:
                min_index = right

        lista[index], lista[min_index] = lista[min_index], lista[index]

def ordena_Descrescente(lista):
    tam = len(lista)
    for index in range(0, tam):
        min_index = index

        for right in range(index + 1, tam):
            if lista[right] > lista[min_index]:
                min_index = right

        lista[index], lista[min_index] = lista[min_index], lista[index]

n = int(input())

for i in range(n):
    a = int(input())
    if (a>=0):
        if(a%2==0):
            pares.append(a)
        else:
            impares.append(a)

ordena_Crescente(pares)
ordena_Descrescente(impares)
mostra_lista(pares)
mostra_lista(impares)
