#Divisores || Maratona
a,b,c,d = input().split()
a,b,c,d = int(a), int(b),int(c),int(d)
num = -1
n = a
if (a!=b and c!=d):
    while (n<=c):
        if (c%n==0):
            if ((n%b!=0)and(d%n!=0)):
                num = n
                break
        n +=a
print(num)