import random
"""
 * This class acts as an object to hold all character info as a utility for the main class
 * Now implemented in Python
 * @Author Brady Klein
 * @Date 01/17/18
"""

class Character :

    def __init__(self, race, gender, height, weight, stats, mannerism, appearance, talent, alignment, ideal, bond, flaw, interactionTrait):
        ##character = {race, gender, height, weight, stats, mannerism, appearance, talent, alignment, ideal, bond, flaw, interactionTrait}

        lawVChaos = random.randrange(0,3)
        goodVEvil = random.randrange(0,3)
        law = {"Lawful", "Neutral", "Chaotic"};
        good = {"Good", "Neutral", "Evil"};
        if(lawVChaos == 1 && goodVEvil == 1):
            self.__setattr__(self, alignment, "True Neutral")
        else:
            self.__setattr__(self, alignment

        def printCharacter():
                print("The NPC generated is a nameless %s %s. They stand %s tall, and weighs %d.\nIn terms of appearance they have %s," +
                    " and they tend to %s.\nThey are/have/can %s, and their alignment is %s. Their ideal is %s, their bond is %s, and their flaw is %s.\n" +
                    " When interacting with others, they tend to be %s.\n" % gender, race, height, weight, appearance, mannerism,
                    talent, alignment, ideal, bond, flaw, interactionTrait);
