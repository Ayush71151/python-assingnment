f={'fruit':{'name':['apple','mango','bananA','PAPYA'],'BIO_name':['a','m','b','p'],'major_producer':['india','us','russia','uk'],'countries':['india','us','russia','uk'],'nutrition':{'carbohydrates':['1','2','3','4'],'protein':[4,2,3,5],'vitamin':['9','8','7','6']}}}
for i in range(0,4):
          if f['fruit']['nutrition']['protein'][i]==max(f['fruit']['nutrition']['protein']):        
              x=f['fruit']['name'][i]   
print(x)