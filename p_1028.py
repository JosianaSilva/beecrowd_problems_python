# Figurinhas
n = int(input())
for i in range(n):
    f1 = int(input())
    f2 = int(input())
    if(f2>f1):
        ctrl = f1
    else:
        ctrl = f2
    while True:
        t1 = f1/ctrl
        t2 = f2/ctrl
        if(t1.is_integer() and t2.is_integer()):
            break
        else:
            ctrl -= 1
    print(ctrl)
