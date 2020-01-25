dic={1:{'name':'marry','age':20,'sex':'female'},2:{'name':'marie','age':20,'sex':'femal'}}
print (dic)
dic[3]={}
dic[3]['name']='luna'
dic[3]['age']=24
dic[3]['sex']='female'
dic[3]['married']='no'
print(dic[3]['sex'])
dic[4]={}
dic[4]={'name':'gal gadot',"age":24,'sex':'female','married':"yes"}
print(dic[4])
del dic[3]['married']
del dic[4]['married']
print (dic[3])
print (dic[4])
for p_id,p_info in dic.items():
    print("\nPerson ID ",p_id)
    for key in p_info:
        print (key,'',p_info[key])

#for p_id in dic.items():
    print("\nPerson ID ",p_id)

#for p_id,p_info in dic.items():
    print("\nPerson ID ",p_id,p_info)