#Idades
chave = True
soma,contador = 0,0
while(chave):
    idade = int(input())
    if(idade>=0):
        soma += idade
        contador += 1
    else:
        chave = False

media = soma/contador
print('{:.2f}'.format(media))

#ACEITO! 12/12/2021