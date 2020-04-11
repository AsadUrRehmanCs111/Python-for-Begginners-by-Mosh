import random
for i in range(0, 7):
    print(random.random())
    print(random.randint(10, 20))
members = ["ali", "asad", "Usama"]
leader = random.choice(members)
print(leader)
class Dice:
    def roll(self):
        result = (random.randint(1, 6), random.randint(1, 6))
        return result


dice = Dice()
print(dice.roll())
