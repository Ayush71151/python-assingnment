n=5
for i in range(0,n+1): 
    if i!=0:
         b=(i*2-1)
         print (" "*(n-i),"*"," "*b,"*")
         if i==n:
           print("*","*  "*(i))
    else:
         print(" "*(n+1-i),"*")