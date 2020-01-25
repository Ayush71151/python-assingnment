class car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
       return 'a',self.color,'car',self.mileage
c=car('red',1000)
print(c.__str__())

            