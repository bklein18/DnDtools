import random

"""
 * The purpose of this project is to randomly generate NPC's with rolled stats, and depth, as well as backgrounds.
 * Everything will come from the Player's Handbook, and the Dungeon Master's
 * This is the python version, which I'll be implementing online using Flask
 * @Author Brady Klein
 * @Date 01/17s/18
"""
"""
import flask

app = flask.Flask(__name__)
app.secret_key = "pikukluhldlidfjkhvsvnioldkf.,hbvwnklwudf"


@app.route("/home/")
def homepage():
    user = {"username": "Brady"}
    return flask.render_template('home.html', name="Brady")


app.run()
"""


class Dice:
    sides = 0

    def __init__(self, side_number):
        self.sides = side_number

    # method
    def roll(self):
        return random.randrange(0, self.sides)

    def get_stat(self):
        possibles = [0, 0, 0, 0]
        possibles[0] = random.randrange(0, 6)
        possibles[1] = random.randrange(0, 6)
        possibles[2] = random.randrange(0, 6)
        possibles[3] = random.randrange(0, 6)
        min_index = 0
        i = 0
        while i < possibles.__len__():
            if possibles[i] < possibles[min_index]:
                min_index = i
        stat = 0
        for i in possibles:
            if i != possibles[min_index]:
                stat += i + 1
        return stat


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
    interaction_trait = ""

    def __init__(self):
        law_v_chaos = random.randrange(0, 3)
        good_v_evil = random.randrange(0, 3)
        law = ["Lawful", "Neutral", "Chaotic"]
        good = ["Good", "Neutral", "Evil"]
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
              self.interaction_trait)


def get_max_index(rolls):
    max_index = 0
    i = 0
    while i < len(rolls):
        if rolls[i] > rolls[i]:
            max_index = i
    return max_index


def get_min_index(rolls):
    min_index = 0
    i = 0
    while i < len(rolls):
        if rolls[i] < rolls[min_index]:
            min_index = i
    return min_index


def main():
    # No user input will be required, all that is necessary is to actually run the class
    # determine race, then from race, determine sex, height, and weight
    rando = Character()
    rando.__init__()
    races = ["Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Lightfoot Halfling",
             "Stout Halfling", "Human", "Dragonborn", "Forest Gnome", "Rock Gnome", "Half-Elf", "Half-Orc",
             "Tiefling"]
    appearances = ["Distinctive jewelry", "Piercing", "Flamboyant or Outlandish clothes", "Formal, clean clothes",
                   "Ragged, dirty looking clothes", "Pronounced scar", "Missing teeth", "Missing fingers",
                   "Unusual eye color or heterochromia", "Tattoos", "Birthmark", "Unusual skin color", "Bald",
                   "Braided beard or hair", "Unusual hair color", "Nervous eye twitch", "Distinctive nose",
                   "Distinctive posture (rigid or crooked)", "Exceptionally beautiful", "Exceptionally ugly"]
    talents = ["Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky",
               "perfect memory", "Great with animals", "Great with children", "Great at solving puzzles",
               "Great at one game", "Great at impersonations", "Draws beautifully", "Paints beautifully",
               "Sings beautifully", "Drinks everyone under the table", "Expert carpenter", "Expert cook",
               "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise",
               "Skilled dancer", "Knows thieve's cant"]
    mannerisms = ["Prone to singing, whistling, or humming quietly", "Speaks in rhymes or some peculiar way",
                  "Particularly high or low voice", "Slurs words, lisps, or stutters", "Enunciates over clearly",
                  "Speaks loudly", "Whispers", "Uses flowery speech or long words",
                  "Frequently uses the wrong word", "Uses colorful oaths and exclamations",
                  "Makes constant jokes and puns", "Prone to predictions of doom", "Fidgets", "Squints",
                  "Stares into the distance", "Chews something", "Paces", "Taps fingers", "Bites fingernails",
                  "Twirls hair or tugs beard"]
    interactions = ["Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest",
                    "Hot tempered", "Irritable", "Ponderous", "Quiet", "Suspicious"]
    ideals_by_alignment = [["Beauty", "Charity", "Greater Good", "Life", "Respect", "Self Sacrifice"],
                           ["Domination", "Greed", "Might", "Pain", "Retribution", "Slaughter"],
                           ["Community", "Fairness", "Honor", "Logic", "Responsibility", "Tradition"],
                           ["Change", "Creativity", "Freedom", "Independence", "No limits", "Whimsy"],
                           ["Balance", "Knowledge", "Live and Let Live", "Moderation", "Neutrality", "People"],
                           ["Aspiration", "Discovery", "Glory", "Nation", "Redemption", "Self-knowledge"]
                           ]
    bonds = ["Dedicated to fulfilling a personal life goal", "Protective of close family members",
             "Protective of colleagues or compatriots", "Loyal to a benefactor, patron, or employer",
             "Captivated by a romantic interest", "Drawn to a special place", "Protective of a special keepsake",
             "Protective of a valuable possession", "Out for revenge"]
    flaws = ["Forbidden love or susceptibility to romance", "Enjoys decadent pleasures", "Arrogance",
             "Envies another creature's power or station", "Overpowering greed", "Prone to rage",
             "Has a powerful enemy", "Specific phobia", "Shameful or scandalous history", "Secret crime or misdeed",
             "Possession of forbidden lore", "Foolhardy bravery"]
    race_die = Dice(len(races))
    r = races[race_die.roll()]
    rando.race = r
    d2 = Dice(2)
    genders = d2.roll()
    if genders == 0:
        rando.gender = "Male"

    else:
        rando.gender = "Female"
    d20 = Dice(20)
    d12 = Dice(12)
    d10 = Dice(10)
    d8 = Dice(8)
    d6 = Dice(6)
    d4 = Dice(4)
    # height/weight calculation
    if rando.race == "Human":
        height_mod = d10.roll() + 1
        height_mod += d10.roll() + 1
        temp_height = 56 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "\'" + inches.__str__() + "\"")
        weight_mod = d4.roll()
        weight_mod += d4.roll()
        rando.weight = 110 + (height_mod * weight_mod)

    elif rando.race == "Half-Elf" or rando.race == "Tiefling":
        height_mod = d8.roll() + 1
        height_mod += d8.roll() + 1
        temp_height = 57 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "\'" + inches.__str__() + "\"")
        weight_mod = d4.roll()
        weight_mod += d4.roll()
        rando.weight = 110 + (height_mod * weight_mod)

    elif rando.race == "Hill Dwarf":
        height_mod = d4.roll() + 1
        height_mod += d4.roll() + 1
        temp_height = 44 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "'" + inches.__str__() + "\"")
        weight_mod = d6.roll()
        weight_mod += d6.roll()
        rando.weight = 115 + (height_mod * weight_mod)

    elif rando.race == "Mountain Dwarf":
        height_mod = d4.roll() + 1
        height_mod += d4.roll() + 1
        temp_height = 46 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "'" + inches.__str__() + "\"")
        weight_mod = d4.roll()
        weight_mod += d4.roll()
        rando.weight = 110 + (height_mod * weight_mod)

    elif rando.race == "High Elf" or rando.race == "Wood Elf":
        height_mod = d10.roll() + 1
        height_mod += d10.roll() + 1
        temp_height = 44 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "'" + inches.__str__() + "\"")
        weight_mod = d4.roll()
        if rando.race == "High Elf":
            rando.weight = 90 + (height_mod * weight_mod)
        else:
            rando.weight = 100 + (height_mod * weight_mod)

    elif rando.race == "Lightfoot Halfling" or rando.race == "Stout Halfling":
        height_mod = d4.roll() + 1
        height_mod += d4.roll() + 1
        temp_height = 31 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "'" + inches.__str__() + "\"")
        rando.weight = 35 + height_mod

    elif rando.race == "Dragonborn":
        height_mod = d8.roll() + 1
        height_mod += d8.roll() + 1
        temp_height = 66 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "'" + inches.__str__() + "\"")
        weight_mod = d6.roll()
        weight_mod += d6.roll()
        rando.weight = 175 + (height_mod * weight_mod)

    elif rando.race == "Forest Gnome" or rando.race == "Rock Gnome":
        height_mod = d4.roll() + 1
        height_mod += d4.roll() + 1
        temp_height = 35 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "'" + inches.__str__() + "\"")
        rando.weight = 35 + height_mod

    else:
        height_mod = d10.roll() + 1
        height_mod += d10.roll() + 1
        temp_height = 58 + height_mod
        inches = temp_height % 12
        feet = temp_height / 12
        rando.__setattr__(rando.height, feet.__str__() + "\'" + inches.__str__() + "\"")
        weight_mod = d6.roll()
        weight_mod += d6.roll()
        rando.weight = 140 + (height_mod * weight_mod)

    # now that height/weight assignment is done, we move on to NPC traits, using the alignment that's already been made
    possible_aligns = [0, 0, 0]
    possible_aligns[2] = 5
    if "True Neutral" == rando.alignment:
        possible_aligns[0] = 4
        possible_aligns[0] = 4
    else:
        if "Lawful" in rando.alignment:
            possible_aligns[0] = 2
        if "Good" in rando.alignment:
            possible_aligns[1] = 0
        if "Neutral " in rando.alignment:
            possible_aligns[0] = 4
        if " Neutral" in rando.alignment:
            possible_aligns[1] = 4
        if "Chaotic" in rando.alignment:
            possible_aligns[0] = 3
        if "Evil" in rando.alignment:
            possible_aligns[1] = 1

    d3 = Dice(3)
    align = d3.roll()
    temp = d6.roll()
    rando.ideal = ideals_by_alignment[possible_aligns[align]][temp]
    # setting flaws
    rando.flaw = flaws[d12.roll()]
    # setting appearances
    rando.appearance = appearances[d20.roll()]
    # setting talents
    rando.talent = talents[d20.roll()]
    # setting mannerisms
    rando.mannerism = mannerisms[d20.roll()]
    # setting interaction traits
    rando.interaction_trait = interactions[d12.roll()]
    # setting their randomly assigned stats
    good_stat = d6.roll()
    bad_stat = d6.roll()
    if bad_stat == good_stat:
        while bad_stat == good_stat:
            bad_stat = d6.roll()
    temp_stats = [0, 0, 0, 0, 0, 0]
    i = 0
    while i < 6:
        temp = d6.get_stat()
        temp_stats[i] = temp
        i = i + 1
    i = 0
    rolls = [0, 0, 0, 0, 0, 0]
    while i < 6:
        if i == bad_stat:
            rolls[i] = rolls[get_min_index(rolls)]
        elif i == good_stat:
            rolls[i] = rolls[get_max_index(rolls)]
        else:
            rolls[i] = rolls[i]
        i += 1
    rando.stats = rolls
    # set their bond
    temp_bond = d10.roll()
    if temp_bond == 10:
        d9 = Dice(9)
        temp_string = ""
        j = d9.roll()
        temp_string += bonds[j]
        k = d9.roll()
        if j == k:
            k = d9.roll()
        temp_string = temp_string + " , and " + bonds[k]
        rando.bond = temp_string
    else:
        rando.bond = bonds[temp_bond]
    rando.print_character()


main()
