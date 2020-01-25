n=int(input("enter no. plz"))
for i in range(n,0,-1):
     if i!=1:
        print("*"*i)
     else:
        print("*",end = " ")
for j in range(0,n+1):
    print("*"*j)