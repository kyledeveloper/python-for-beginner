
class People:
    def __init__(self,name) -> None:
        self.name = name
        self.age = 18
        self.gender = "male"
    
    def setName(self,newName):
        self.name = newName
    def getName(self):
        return self.name
    def setAge(self,newAge):
        self.age = newAge
    def getAge(self):
        return self.age
   
        
    # def setInitialfeatures(self,star)
    # def __str__(self):
    #     return f'{self.name}\nage:{self.currentage}\nstar:{self.star} and rank:{self.rank}\nall features: {self.features}\n total feature:{self.totalFeatures}'

    # def updatefeature(self,key):
    #     self.features[key] += 1
    #     self.settotalfeatures()

    # def settotalfeatures(self):
    #     for key in self.features:
    #         self.totalFeatures += self.features[key]

# if __name__ == '__main__':
    # myself = People("KyleLiang", age = 28,star = 1,sex = 1)
    # myself.updatefeature("force")

    # print(myself)