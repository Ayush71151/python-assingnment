from automobile import automobile
class car(automobile):
    def __init__(self,make,model,mileage,price,door):
        automobile.__init__(self,make,model,mileage,price)
    def set_door(self,door):
        self.door=door
    def get_door(self):
        return  self.door
        
class truck(automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        pass
    def set_door(self,drive_type):
        self.drive_type=drive_type
    def get_door(self):
        return  self.drive_type

class suv(automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        pass
    def set_door(self,pass_cap):
        self.pass_cap=pass_cap
    def get_door(self):
        return  self.pass_cap

c=car('toyota','cart','800','500K','4')
c.set_make('toyota ')
print(c.get_make())
c.set_model('gfahd')
print(c.get_model())
c.set_mileage('rgdsh')
print(c.get_mileage())
c.set_price('hdhd')
print(c.get_price())
c.set_door('rwhtes')
print(c.get_door())
print("***********************************************************************")

t=truck("troijw",'uyte','uygw','uywg','ugew')
t.set_make('toyota ')
print(c.get_make())
t.set_model('gfahd')
print(c.get_model())
t.set_mileage('rgdsh')
print(c.get_mileage())
t.set_price('hdhd')
print(c.get_price())
t.set_door('rwhtes')
print(c.get_door())
print("***********************************************************************")

s=suv("troijw",'uyte','uygw','uywg','ugew')
s.set_make('toyota ')
print(c.get_make())
s.set_model('gfahd')
print(c.get_model())
s.set_mileage('rgdsh')
print(c.get_mileage())
s.set_price('hdhd')
print(c.get_price())
s.set_door('rwhtes')
print(c.get_door())

