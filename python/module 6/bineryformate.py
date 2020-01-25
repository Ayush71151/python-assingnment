import pickle 
phonebook={"chris":'555-100',"katie":'555-555','agile':'111-000'}
outfile=open('phonebook.dat','wb')
pickle.dump(phonebook,outfile)
outfile.close()
outfile=open('phonebook.dat','r')
print(outfile.read())