from random import random
from People import People

class Hero(People):
    def __init__(self,name) -> None:
        # inherit all parent method and attritubes
        super().__init__(name)
        self.features = {
            "intellenge": 0,
            "force": 0,
            "physicalPower": 0,
            "lucky": 0,
            "charm": 0,
        }
        self.totalFeatures = 0
        self.star = 0 

    def setStar(self):
        randomNum = random()
        if randomNum <= 0.01:
            self.star = 5
        elif randomNum <= 0.05:
            self.star = 4
        elif randomNum <= 0.125:
            self.star = 3
        elif randomNum <= 0.65:
            self.star = 2
        else:
            self.star = 1
        print(f'randomNum:{randomNum}')
        return self.star
        
if __name__ == "__main__":
    newHero = Hero("haokun")
    print(newHero.setStar())