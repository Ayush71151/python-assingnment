class contact_information:
    def __init__(self,name,phone,email):
        print("welcome")
    def set_name(self,name):
        self.name=name
    def set_phone(self,phone):       
        self.phone=phone
    def set_email(self,email) :
       self.email=email
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    def __str__(self):
        return self.name,self.phone,self.email
a=contact_information("jhon wick","564645","ajfiajkn")
a.set_name('jhon wick')
a.set_phone('8734934')
a.set_email('jdkjdaj')
print(a.__str__())