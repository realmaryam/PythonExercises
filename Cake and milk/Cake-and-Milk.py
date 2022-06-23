n = int(input())
a = list(map(int,input().strip().split()))[:n]

init = 0
final = n - 1
Lmax = 0
Rmax = 0
milk = 0

while (init < final):
    while (init < final and a[init] <= a[init + 1]):
        init += 1
    else:
        Lmax = a[init]
    
    while (init < final and a[final] <= a[final - 1]):
        final -= 1
    else:
        Rmax = a[final]
    
    if Lmax < Rmax :
        init += 1
        while (init < final and a[init] <= Lmax):
            milk += Lmax - a[init]
            init += 1
    else:
        final -= 1
        while (final > init and a[final] <= Rmax):
            milk += Rmax - a[final]
            final -= 1

print ( milk)
