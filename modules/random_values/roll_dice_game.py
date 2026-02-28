import random

class Dice:
    numbers = (1,2,3,4,5,6)
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

d1 = Dice()
print(d1.roll())

