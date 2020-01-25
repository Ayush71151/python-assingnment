p=input("enter the packages : ")
price=p*99 
dis=0
if p>10:   
    dis=price*10/100 
elif p>=20:    
    dis=price*20/100
elif p>=50:
    dis=price*30/100
else:
    dis=price*40/100   
M=price - dis
print "total price",M
d=price-M
print "discount",d   
