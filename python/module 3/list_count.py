n=int(input("enter the value of list : "))
l=[]
for i in range(0,n):
    a=int(input("value of list : "))
    l.append(a)
    l.sort()
print(l)
c=0
l2=[]
for i in range(0,n-1):
    if l[i+1] == l[i]:
       l2.append(l[i])
       l2.sort()
print(l2) 
l3=[]
for i in range(0,n-1):
    if l[i+1] != l[i]:
       l3.append(l[i])
       l3.sort()
l4=l2+l3
print(l4)