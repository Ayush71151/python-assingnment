n=int(input("enter the value of list : "))
l=[]
l2=[]
l3=[]
for i in range(n):
    a=int(input("value of list : "))
    l.append(a)
l.sort()
for j in range(n):
    x=1
    c=l[j]
    for k in range(n):
        if c==l[k]and k!=j:
            x=x+1
    l2.append(x)
    for i in range(len(l2)):
        a=l2.index(max(l2))
        b=l[a]
        l3.append(b)
        l2[a]=0
print(l3)