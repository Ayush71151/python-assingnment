n1=[1,2,3,4,5,7]
n2=[6,7,8,2,1]
x=int(input("enter the value"))
for i in n1:
    a=i
    for j in n2 :
        b=j
        c=a+b
        if c==x:
            print ("a = ",a,"b = ", b,"c = ",c)