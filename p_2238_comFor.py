#Divisores || Maratona
a,b,c,d = input().split()
a,b,c,d = int(a),int(b),int(c),int(d)
num = -1
#if (1<=a<=10**9 and 1<=b<=10**9 and 1<=c<=10**9 and 1<=d<=10**9):
if (a!=b and c!=d):
    for n in range(a,c+1,a):
        if ((n%a==0) and (c%n==0) and (n%b!=0) and (d%n!=0)):
            num = n
            break
print(num)   

# ACEITO 21/12/2021