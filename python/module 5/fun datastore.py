datastore={"office":{"medical":[
                                {"room_no":100,"use":"recption","sq_ft":50,"price":75}
                                ,{"room_no":101,"use":"waiting","sq_ft":250,"price":75}
                                ,{"room_no":102,"use":"waiting","sq_ft":125,"price":150}
                                ,{"room_no":103,"use":"examine","sq_ft":125,"price":150}
                                ,{"room_no":104,"use":"examine","sq_ft":150,"price":100}]
                        ,"price":{"location":"premium","style":"covered","price":750}}}
print(datastore)
print("************************************************************************")
def room(datastore):
    old=int(input("enter old."))
    new=int(input("enter new."))
    for i in range(0,5):
      if datastore["office"]["medical"][i]["room_no"] == old:
         datastore["office"]["medical"][i]["room_no"] = new
    print (datastore)  
room(datastore)
print("************************************************************************")
def delete(datastore):
    old=int(input("enter no."))  
    for i in range(0,5):
      if datastore["office"]["medical"][i]["room_no"] == old:
       del datastore["office"]["medical"][i]
       break
    print (datastore)  
delete(datastore)
print("************************************************************************")
def add(datstore):
         l={}
         r=int(input("enter new."))
         u=input("enter the value")
         s=int(input("enter the value"))
         p=int(input("enter the value"))
         l={"room":r,"use":u,"sq_ft":s,"price":p}
         datastore['office']['medical'].append(l)
         print (datastore)  
add(datastore)
print("************************************************************************")