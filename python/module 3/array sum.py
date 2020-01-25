arr=[1,2,3,4,5,6,7,8,9]
s=int(input("enter the sum"))
a=0
b=0
for i in arr:
   a=i
   for j in arr:
       b=j
       c=a+b
       if c==s:
          print("c is ",a,b,c)

          