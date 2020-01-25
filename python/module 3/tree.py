a=int(input("a : "))
time=int(input())
b,c,=[],[]
for i in range(a):
    f=int(input())
    c.append(f)
for i in range(a-1):
    s=c[i]+c[i+1]
    count=1
    j=i+2
    while count<time-1 and j<a:
        count = count+1
        s = s+c[j]
        j=j+1
        b.append(s)
print(max(b))