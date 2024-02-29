from random import randint

class Die:
    def __init__(self, sides = 0):
        self.sides = sides

    def roll_die(self):
        rand_roll = randint(1, self.sides)
        print(rand_roll)

#n_of_sides = int(input("Enter the number of sides: "))
die = Die(20)
die.roll_die()

