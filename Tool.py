from importlib.resources import read_text

from random import Random, randint, random

counter = 0
validDecimalInput = ["0","1","2","3","4","5","6","7","8","9","."]

def setStar():
    star = 0
    randomNum = random()
    if randomNum <= 0.01:
        star = 5
    elif randomNum <= 0.05:
        star = 4
    elif randomNum <= 0.125:
        star = 3
    elif randomNum <= 0.65:
        star = 2
    else:
        star = 1

    return star

def nameGenerator():
    random1 = randint(1,13000)
    firstName = None
    f = open("data/namelist.txt", "r")
    for i in range(random1):
        firstName = f.readline().capitalize().strip()
    f.close()
    return firstName

