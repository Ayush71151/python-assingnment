s=input("enter subject and marks")
a=s.split(" ")
avg=i=sub=0
while i<=len(a):
   try:
      avg=avg+int(a[i])
      sub=sub+1
      i=i+1
   except : i=i+1
print ("avg is ",avg/sub)