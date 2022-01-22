
class Store:
    def __init__(self,name,star,) -> None:
        self.name = name
        self.star = star
        self.growthRate = star * 0.01
        self.maxlevel = star * 100
        self.basicIncome = 100 * star
        self.moneytoLvUp = 100 * star
        self.level = 1
        self.Maxemployee = int(10 + star * 2 + self.level * 0.1)
        self.income = self.basicIncome
        
    def setIncome(self):
        self.income = int(self.basicIncome * ( 1 +self.growthRate) ** self.level)

    def leveUpstore(self,money):
        if money >= self.moneytoLvUp:
            self.level +=1
            self.moneytoLvUp = self.moneytoLvUp * (1+0.05) ** self.level
            self.setIncome()

if __name__ == "__main__":
    newStore = Store("empire Book Store",5)
    newStore.level = 100
    newStore.setIncome()
    print(newStore.income)