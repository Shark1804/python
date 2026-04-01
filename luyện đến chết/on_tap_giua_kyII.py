def snt(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
a=[int(i) for i in input('Nhap mang:').split()]
print('Mang a:',a)
b=[]
t=0
for i in a:
    if snt(i)==True:
        b=b+[i]
        t=t+i
b.sort()
for i in b:
    print(i,end=' ')
print()
b.sort(reverse=True)
for i in b:
    print(i,end=' ')
print()
print(t)