p=input("enter the no. : ")
p0="green"
if p>0 and p<11:
    if p%2==0: 
      print "black"
    else:
        print "red"
elif p>=11 and p<19:
    if p%2==0:
        print "red"
    else:
        print "black"
elif p>19 and p<29:
    if p%2==0:
        print "black"
    else :
        print "red"
elif p>=29 and p<=36:
    if p%2==0:
        print "red"
    else:
        print "black"
else :
    print "plz enter between 0 to 36"
