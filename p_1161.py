#Soma de Fatoriais
def fatorial(a):
    resultado = 1
    for i in range(a,1,-1):
        resultado *= i
    return resultado
while True:
    try:
        m,n = input().split()
        m,n = int(m),int(n)
        r1 = fatorial(m)
        r2 = fatorial(n)
        somaF = r2+r1
        print('{}'.format(somaF))
    except EOFError:
        break

#ACEITO! 14/12/2021