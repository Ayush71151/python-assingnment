import random 
class no:
    def __init__(self):
        self.sideup='heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='heads'
        else:
            self.sideup='tails'
    def get_side(self):
        eturn self.sideup
c=no()
print(c.toss())
