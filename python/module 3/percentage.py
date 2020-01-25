s=input("enter name and marks")
a=s.split(",")
b=int(a[1])+int(a[2])+int(a[3])+int(a[4])+int(a[5])
c=int(a[6])+int(a[7])+int(a[8])
e=b+c
print ("student ",a[0]," of theory marks is ",b,"and of practicle marks",c,"and total % is ",e/590*100)

