class contact:
    def __init__(self,name,phone,email):
        self.name=input("enter your name")
        self.phone=int(input("enter your number"))
        self.email=input("enter your email")
    def __repr__(self):
         return "%s,%s,%s"%(self.name,self.phone,self.email)

con={}
n=int(input("enter the range of dictionary plzz"))
def add():
    for i in range(0,n):    
      c=contact("sgohrsor","54364","iuhgv")
      con[i]=c
      print(con)
print(add())
def delete():
    old=int(input("enter key for delete : "))
    for i in range (0,n):
     if con[i]==con[old]:
         del con[i]
         break
     else : print("error some occur")
     print (con)
print(delete())
def search():
    srch=int(input("enter the value for search"))
    for i in range(0,n):
        if con[i]==con[srch]:
            print(con[i])
            break
        else: print ("info is not exist")
print(search())