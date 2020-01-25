datastore={"office":{"medical":[
                                {"room_no":100,"use":"recption","sq_ft":50,"price":75}
                                ,{"room_no":101,"use":"waiting","sq_ft":250,"price":75}
                                ,{"room_no":102,"use":"waiting","sq_ft":125,"price":150}
                                ,{"room_no":103,"use":"examine","sq_ft":125,"price":150}
                                ,{"room_no":104,"use":"examine","sq_ft":150,"price":100}]
                        ,"price":{"location":"premium","style":"covered","price":750}}}
print(datastore)
print("******************************************************************************************************************")
print ("do you want to chNGE ROOM NO.")
yes=input("enter only yes or no plzz")
def room(datastore):
    try:
       old=int(input("enter old.  "))
       new=int(input("enter new.  "))
    except:
        print("you enter wrong information and may not be exist")
        room(datastore)
    for i in range(0,5):
      if datastore["office"]["medical"][i]["room_no"] == old:
         datastore["office"]["medical"][i]["room_no"] = new
    print (datastore) 
if     yes == "yes":
  room(datastore)
else :
    print("room no. is not change")
    
    
print("************************************************************************")
print ("do you want to delete any room")
yes=input("enter only yes or no plzz")
def delete(datastore):
    try:
         old=int(input("enter no. for delete room"))  
    except:
        print("you enter wrong information and may not be exist")
        delete(datastore)
    for i in range(0,5):
      if datastore["office"]["medical"][i]["room_no"] == old:
       del datastore["office"]["medical"][i]
       break
    print (datastore)  
if     yes == "yes":
  delete(datastore)
else :
    print("room no. is not delete")

print("************************************************************************")
print ("do you ant to add room")
yes=input("enter only yes or no plzz")
def add(datstore):
    try:
         l={}
         r=int(input("enter new room "))
         u=input("enter value use ")
         s=int(input("enter sq_ft "))
         p=int(input("enter price "))
    except:
        print("you enter wrong information")
        add(datastore)
    l={"room":r,"use":u,"sq_ft":s,"price":p}
    datastore['office']['medical'].append(l)
    print (datastore)  
if     yes == "yes":
   add(datastore)
else :
    print("room no. is not delete")

print("************************************************************************")
