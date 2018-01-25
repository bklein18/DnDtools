import random
"""
 * This class acts as an object to hold all character info as a utility for the main class
 * Now implemented in Python
 * @Author Brady Klein
 * @Date 01/17/18
"""


class Character:
    race = ""
    gender = ""
    height = ""
    weight = 0
    stats = [0, 0, 0, 0, 0, 0]
    mannerism = ""
    appearance = ""
    talent = ""
    alignment = ""
    ideal = ""
    bond = ""
    flaw = ""
    interactionTrait = ""

    def __init__(self):
        law_v_chaos = random.randrange(0, 3)
        good_v_evil = random.randrange(0, 3)
        law = {"Lawful", "Neutral", "Chaotic"};
        good = {"Good", "Neutral", "Evil"};
        if law_v_chaos == 1 & good_v_evil == 1:
            self.alignment = "True Neutral"
        else:
            self.alignment = (law[law_v_chaos] + " " + good[good_v_evil])

    def print_character(self):
        print("The NPC generated is a nameless %s %s. They stand %s tall, and weighs %d.\nIn terms of " +
              "appearance they have %s, and they tend to %s.\nThey are/have/can %s, and their alignment is " +
              "%s. Their ideal is %s, their bond is %s, and their flaw is %s.\n When interacting with others," +
              "they tend to be %s.\n" % self.gender, self.race, self.height, self.weight, self.appearance,
              self.mannerism, self.talent, self.alignment, self.ideal, self.bond, self.flaw,
              self.interactionTrait)
