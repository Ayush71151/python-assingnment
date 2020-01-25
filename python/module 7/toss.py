import random 
class coin:
    def __init__(self):
        self.sideup='heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='heads'
        else:
            self.sideup='tails'
    def get_side(self):
           return self.sideup
def main():
 my_coin=coin()
 print("the side up : " ,my_coin.get_side())
 print ("i am tossing coin")
 my_coin.toss()
 print("the side up : " ,my_coin.get_side())
main()
