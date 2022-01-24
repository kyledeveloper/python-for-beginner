import Tool
from People import People
from Skill import Skill

class Employee(People):
    def __init__(self, name,star) -> None:
        super().__init__(name,)
        self.abilities = {
            # sell is the ability to raise the sell price.
            # cost is the ability to lower the production cost.
            # serve is the ability to lower customer's saving.
            "sell" : 0, 
            "cost" : 0,
            "serve": 0,
        }
        self.lv = 0 
        self.exp = 0
        self.expToLvUp = 100
        self.NumOfSkills = 0
        self.star = star


if __name__ == "__main__":
    newEmployee = Employee(Tool.nameGenerator(),Tool.setStar())
    print(f'{newEmployee.name} with {newEmployee.star} star')