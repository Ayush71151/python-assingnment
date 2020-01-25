n=int(input("enter no :  "))
for i in range(0,n):
    if i==int(n/2):
        print(" ", end = " ")
        for i in range (0,n):
            print("*",end=" ")
            if i==n-1:
                print()
    else:
       print(" "*n+"*")