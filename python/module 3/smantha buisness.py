item=int(input("no. of item"))
whole=0
for i in range(0,item):
   while (True):
      print ("no. of item",i+1)
      a=int(input("enter the price"))
      if a>=0:
         whole=whole+a
         break
      else: pass 
retail=whole*0.5
print("retail",retail)