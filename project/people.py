
from project.F1 import Features1


class People:
    def __init__(self,name,age = 18,star = 1,sex = 0) -> None:
        self.name = name
        self.currentage = age
        self.sex = 0
        self.star = star
        self.personalFeature = Features1


if __name__ == '__main__':
    myself = People("KyleLiang", age = 28,star = 1,sex = 1)
    print(myself.personalFeature.charm)