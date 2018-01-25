import random
"""
 * This rolls a n sided die where n is provided
 * Now implemented in python
 * @Author Brady Klein
 * @Date 01/11/18
 """

class Dice :
    sides = 0

    def __init__(self, side_number):
        self.sides = side_number

    #method
    def roll(self):
        return random.randrange(0, self.sides)

    def get_stat(self):
        possibles = [0, 0, 0, 0]
        possibles[0] = random.randrange(0, 6);
        possibles[1] = random.randrange(0, 6);
        possibles[2] = random.randrange(0, 6);
        possibles[3] = random.randrange(0, 6);
        min_index = 0
        for i in possibles:
            if i < possibles[min_index]:
                min_index = i
        stat = 0
        for i in possibles:
            if i != possibles[min_index]:
                stat += i + 1
        return stat
