import random
"""
 * The purpose of this project is to randomly generate NPC's with rolled stats, and depth, as well as backgrounds.
 * Everything will come from the Player's Handbook, and the Dungeon Master's
 * This is the python version, which I'll be implementing online using Flask
 * @Author Brady Klein
 * @Date 01/17s/18
"""
import flask

app = flask.Flask(__name__)
app.secret_key = "pikukluhldlidfjkhvsvnioldkf.,hbvwnklwudf"


@app.route("/home/")
def homepage():
    return flask.render_template('home.html', name="Bean")


app.run()

class Dice :
    sides = 0

    def __init__(self, side_number):
        self.sides = side_number

    #method
    def roll(self):
        return random.randrange(0, self.sides)

    def get_stat(self):
        possibles = [0, 0, 0, 0]
        possibles[0] = random.randrange(0, 6)
        possibles[1] = random.randrange(0, 6)
        possibles[2] = random.randrange(0, 6)
        possibles[3] = random.randrange(0, 6)
        min_index = 0
        for i in possibles:
            if i < possibles[min_index]:
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
    interactionTrait = ""

    def __init__(self):
        law_v_chaos = random.randrange(0, 3)
        good_v_evil = random.randrange(0, 3)
        law = ["Lawful", "Neutral", "Chaotic"]
        good = ["Good", "Neutral", "Evil"]
        if law_v_chaos == 1 & good_v_evil == 1:
            self.alignment = "True Neutral"
        else:
            self.alignment = (law[law_v_chaos + " " + good[good_v_evil])

    def print_character(self):
        print("The NPC generated is a nameless %s %s. They stand %s tall, and weighs %d.\nIn terms of " +
              "appearance they have %s, and they tend to %s.\nThey are/have/can %s, and their alignment is " +
              "%s. Their ideal is %s, their bond is %s, and their flaw is %s.\n When interacting with others," +
              "they tend to be %s.\n" % self.gender, self.race, self.height, self.weight, self.appearance,
              self.mannerism, self.talent, self.alignment, self.ideal, self.bond, self.flaw,
              self.interactionTrait)



def main():
        ##No user input will be required, all that is necessary is to actually run the class
        ##determine race, then from race, determine sex, height, and weight
        rando = Character()
        rando.__init__()
        races = ["Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Lightfoot Halfling",
                "Stout Halfling", "Human", "Dragonborn", "Forest Gnome", "Rock Gnome", "Half-Elf", "Half-Orc",
                "Tiefling"]
        appearances = ["Distinctive jewelry", "Piercing", "Flamboyant or Outlandish clothes", "Formal, clean clothes",
        "Ragged, dirty looking clothes", "Pronounced scar", "Missing teeth", "Missing fingers", "Unusual eye color or heterochromia",
        "Tattoos", "Birthmark", "Unusual skin color", "Bald", "Braided beard or hair", "Unusual hair color", "Nervous eye twitch",
        "Distinctive nose", "Distinctive posture (rigid or crooked)", "Exceptionally beautiful", "Exceptionally ugly"]
        abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        talents = ["Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "perfect memory",
        "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations",
        "Draws beautifully", "Paints beautifully", "Sings beautifully", "Drinks everyone under the table", "Expert carpenter",
        "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise",
        "Skilled dancer", "Knows thieve's cant"]
        mannerisms = ["Prone to singing, whistling, or humming quietly", "Speaks in rhymes or some peculiar way",
        "Particularly high or low voice", "Slurs words, lisps, or stutters", "Enunciates over clearly", "Speaks loudly",
        "Whispers", "Uses flowery speech or long words", "Frequently uses the wrong word", "Uses colorful oaths and exclamations",
        "Makes constant jokes and puns", "Prone to predictions of doom", "Fidgets", "Squints", "Stares into the distance",
        "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"]
        interactions = ["Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot tempered",
        "Irritable", "Ponderous", "Quiet", "Suspicious"]
        idealsByAlignment= [["Beauty", "Charity", "Greater Good", "Life", "Respect", "Self Sacrifice"],
                                       ["Domination", "Greed", "Might", "Pain", "Retribution", "Slaughter"],
                                       ["Community", "Fairness", "Honor", "Logic", "Responsibility", "Tradition"],
                                       ["Change", "Creativity", "Freedom", "Independence", "No limits", "Whimsy"],
                                       ["Balance", "Knowledge", "Live and Let Live", "Moderation", "Neutrality", "People"],
                                       ["Aspiration", "Discovery", "Glory", "Nation", "Redemption", "Self-knowledge"]
                            ]
        bonds = ["Dedicated to fulfilling a personal life goal", "Protective of close family members", "Protective of colleagues or compatriots",
        "Loyal to a benefactor, patron, or employer", "Captivated by a romantic interest", "Drawn to a special place",
        "Protective of a special keepsake", "Protective of a valuable possession", "Out for revenge"]
        flaws = ["Forbidden love or susceptibility to romance", "Enjoys decadent pleasures", "Arrogance", "Envies another creature's power or station",
        "Overpowering greed", "Prone to rage", "Has a powerful enemy", "Specific phobia", "Shameful or scandalous history",
        "Secret crime or misdeed", "Possession of forbidden lore", "Foolhardy bravery"]
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
        ##height/weight calculation
        if rando.race == "Human":
            height_mod = d10.roll() + 1
            height_mod += d10.roll() + 1
            temp_height = 56 + height_mod
            inches = temp_height % 12
            feet = temp_height / 12
            rando.__setattr__(rando.height, feet + "\'" + inches + "\"")
            weight_mod = d4.roll()
            weight_mod += d4.roll()
            rando.weight = 110 + (height_mod * weight_mod)

        elif rando.race == "Half-Elf" or rando.race == "Tiefling":
            height_mod = d8.roll() + 1
            height_mod += d8.roll() + 1
            temp_height = 57 + height_mod
            inches = temp_height % 12
            feet = temp_height / 12
            rando.__setattr__(rando.height, feet + "\'" + inches + "\"")
            weight_mod = d4.roll()
            weight_mod += d4.roll()
            rando.weight = 110 + (height_mod * weight_mod)

        elif rando.race = "Hill Dwarf":
            height_mod = d4.roll() + 1
            height_mod += d4.roll() + 1
            temp_height = 44 + height_mod
            inches = temp_height % 12
            feet = temp_height / 12
            rando.__setattr__(rando.height, feet + "\'" + inches + "\"")
            weight_mod = d6.roll()
            weight_mod += d6.roll()
            rando.weight = 115 + (height_mod * weight_mod)

        else if(rando.getRace().equals("Mountain Dwarf")){
            int heightMod = d4.roll() + 1;
            heightMod += d4.roll() + 1;
            int tempHeight = 56 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d4.roll();
            weightMod += d4.roll();
            rando.setWeight(110 + (heightMod * weightMod));
        }
        else if(rando.getRace().equals("High Elf") || rando.getRace().equals("Wood Elf")){
            int heightMod = d10.roll() + 1;
            heightMod += d10.roll() + 1;
            int tempHeight = 44 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d4.roll();
            if(rando.getRace().equals("High Elf")){
                rando.setWeight(90 + (heightMod * weightMod));
            }
            else{
                rando.setWeight(100 + (heightMod * weightMod));
            }
        }
        else if(rando.getRace().equals("Lightfoot Halfling") || rando.getRace().equals("Stout Halfling")){
            int heightMod = d4.roll() + 1;
            heightMod += d4.roll() + 1;
            int tempHeight = 31 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            rando.setWeight(heightMod + 35);
        }
        else if(rando.getRace().equals("Dragonborn")){
            int heightMod = d8.roll() + 1;
            heightMod += d8.roll() + 1;
            int tempHeight = 66 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d6.roll();
            weightMod += d6.roll();
            rando.setWeight(175 + (heightMod * weightMod));
        }
        else if(rando.getRace().equals("Forest Gnome") || rando.getRace().equals("Rock Gnome")){
            int heightMod = d4.roll() + 1;
            heightMod += d4.roll() + 1;
            int tempHeight = 35 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            rando.setWeight(35 + heightMod);

        }
        else{
            int heightMod = d10.roll() + 1;
            heightMod += d10.roll() + 1;
            int tempHeight = 58 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d6.roll();
            weightMod += d6.roll();
            rando.setWeight(140 + (heightMod * weightMod));
        }
        ##now that height/weight assignment is done, we move on to NPC traits, using the alignment that's already been generated
        String randoAlign = rando.getAlignment();
        int possibleAligns[] = new int[3];
        possibleAligns[2] = 5;
        switch(randoAlign){
            case "Lawful Good":     possibleAligns[0] = 0;
                                    possibleAligns[1] = 2;
                                    break;
            case "Lawful Neutral":  possibleAligns[0] = 2;
                                    possibleAligns[1] = 4;
                                    break;
            case "Lawful Evil":     possibleAligns[0] = 1;
                                    possibleAligns[1] = 2;
                                    break;
            case "Neutral Good":    possibleAligns[0] = 0;
                                    possibleAligns[1] = 4;
                                    break;
            case "True Neutral":    possibleAligns[0] = 4;
                                    possibleAligns[1] = 4;
                                    break;
            case "Neutral Evil":    possibleAligns[0] = 1;
                                    possibleAligns[1] = 4;
                                    break;
            case "Chaotic Good":    possibleAligns[0] = 0;
                                    possibleAligns[1] = 3;
                                    break;
            case "Chaotic Neutral": possibleAligns[0] = 3;
                                    possibleAligns[1] = 4;
                                    break;
            case "Chaotic Evil":    possibleAligns[0] = 1;
                                    possibleAligns[1] = 3;
                                    break;
            default:                break;
        }
        Dice d3 = new Dice(3);
        int align = d3.roll();
        int temp = d6.roll();
        rando.setIdeal(idealsByAlignment[possibleAligns[align]][temp]);
        ##setting flaws
        rando.setFlaw(flaws[d12.roll()]);
        ##setting appearances
        rando.setAppearance(appearances[d20.roll()]);
        ##setting talents
        rando.setTalent(talents[d20.roll()]);
        ##setting mannerisms
        rando.setMannerism(mannerisms[d20.roll()]);
        ##setting interaction traits
        rando.setInteractionTrait(interactions[d12.roll()]);
        ##setting their randomly assigned stats
        int goodStat = d6.roll();
        int badStat = d6.roll();
        if(badStat == goodStat) {
            while (badStat == goodStat) {
                badStat = d6.roll();
            }
        }
        ArrayList<Integer> rolls = new ArrayList<Integer>();
        for(int i = 0; i < 6; i++){
            temp = d6.getStat();
            rolls.add(temp);
        }
        int tempStats[] = new int[6];
       for(int i = 0; i < 6; i++){
           if(i == badStat){
               tempStats[i] = rolls.get(getMinIndex(rolls));
               rolls.remove(getMinIndex(rolls));
           }
           else if(i == goodStat){
               tempStats[i] = rolls.get(getMaxIndex(rolls));
               rolls.remove(getMaxIndex(rolls));
           }
           else{
               tempStats[i] = rolls.get(0);
               rolls.remove(0);
           }
       }
       rando.setStats(tempStats);
       ##finally, we set their bond
       int tempBond = d10.roll();
       if(tempBond == 10){
           Dice d9 = new Dice(9);
           String tempString = "";
           int j = d9.roll();
           tempString += bonds[j];
           int k = d9.roll();
           if(j == k){
               k = d9.roll();
           }
           tempString = tempString + " , and " + bonds[k];
           rando.setBond(tempString);
       }
       else{
           rando.setBond(bonds[tempBond]);
       }
       rando.printCharacter();
    }

    public static int getMaxIndex(ArrayList<Integer> a){
        int maxIndex = 0;
        for(int i = 0; i < a.size(); i++){
            if(a.get(i) > a.get(maxIndex)){
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    public static int getMinIndex(ArrayList<Integer> a){
        int minIndex = 0;
        for(int i = 0; i < a.size(); i++){
            if(a.get(i) < a.get(minIndex)){
                minIndex = i;
            }
        }
        return minIndex;
    }
}
