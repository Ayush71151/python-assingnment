a=input("enter no is:")
s=""
x=list(a)
for i in range(len(x)):
    x[i]=int(x[i])+1
    s=str(x[i])
print(s)
