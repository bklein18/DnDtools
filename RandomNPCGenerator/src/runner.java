/**
 * The purpose of this project is to randomly generate NPC's with rolled stats, and depth, as well as backgrounds.
 * Everything will come from the Player's Handbook, and the Dungeon Master's Guide
 * @Author Brady Klein
 * @Date 01/11/18
 */

import java.util.ArrayList;

public class runner {
    public static void main(String args[]){
        //No user input will be required, all that is necessary is to actually run the class
        //determine race, then from race, determine sex, height, and weight
        Character rando = new Character();
        String races[] = {"Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Lightfoot Halfling",
                "Stout Halfling", "Human", "Dragonborn", "Forest Gnome", "Rock Gnome", "Half-Elf", "Half-Orc",
                "Tiefling"};
        String appearances[] = {"Distinctive jewelry", "Piercing", "Flamboyant or Outlandish clothes", "Formal, clean clothes",
        "Ragged, dirty looking clothes", "Pronounced scar", "Missing teeth", "Missing fingers", "Unusual eye color or heterochromia",
        "Tattoos", "Birthmark", "Unusual skin color", "Bald", "Braided beard or hair", "Unusual hair color", "Nervous eye twitch",
        "Distinctive nose", "Distinctive posture (rigid or crooked)", "Exceptionally beautiful", "Exceptionally ugly"};
        String abilities[] = {"Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"};
        String talents[] = {"Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "perfect memory",
        "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations",
        "Draws beautifully", "Paints beautifully", "Sings beautifully", "Drinks everyone under the table", "Expert carpenter",
        "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise",
        "Skilled dancer", "Knows thieve's cant"};
        String mannerisms[] = {"Prone to singing, whistling, or humming quietly", "Speaks in rhymes or some peculiar way",
        "Particularly high or low voice", "Slurs words, lisps, or stutters", "Enunciates over clearly", "Speaks loudly",
        "Whispers", "Uses flowery speech or long words", "Frequently uses the wrong word", "Uses colorful oaths and exclamations",
        "Makes constant jokes and puns", "Prone to predictions of doom", "Fidgets", "Squints", "Stares into the distance",
        "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"};
        String interactions[] = {"Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot tempered",
        "Irritable", "Ponderous", "Quiet", "Suspicious"};
        String[][] idealsByAlignment= {{"Beauty", "Charity", "Greater Good", "Life", "Respect", "Self Sacrifice"},
                                       {"Domination", "Greed", "Might", "Pain", "Retribution", "Slaughter"},
                                       {"Community", "Fairness", "Honor", "Logic", "Responsibility", "Tradition"},
                                       {"Change", "Creativity", "Freedom", "Independence", "No limits", "Whimsy"},
                                       {"Balance", "Knowledge", "Live and Let Live", "Moderation", "Neutrality", "People"},
                                       {"Aspiration", "Discovery", "Glory", "Nation", "Redemption", "Self-knowledge"}
                                      };
        String bonds[] = {"Dedicated to fulfilling a personal life goal", "Protective of close family members", "Protective of colleagues or compatriots",
        "Loyal to a benefactor, patron, or employer", "Captivated by a romantic interest", "Drawn to a special place",
        "Protective of a special keepsake", "Protective of a valuable possession", "Out for revenge"};
        String flaws[] = {"Forbidden love or susceptibility to romance", "Enjoys decadent pleasures", "Arrogance", "Envies another creature's power or station",
        "Overpowering greed", "Prone to rage", "Has a powerful enemy", "Specific phobia", "Shameful or scandalous history",
        "Secret crime or misdeed", "Possession of forbidden lore", "Foolhardy bravery"};
        Dice raceDie = new Dice(races.length);
        String race = races[raceDie.roll()];
        rando.setRace(race);
        Dice coin = new Dice(2);
        int genders = coin.roll();
        //lol
        switch(genders){
            case 0:  rando.setGender("Male");
                     break;
            case 1:  rando.setGender("Female");
                     break;
            default: break;
        }
        Dice d20 = new Dice(20);
        Dice d12 = new Dice(12);
        Dice d10 = new Dice(10);
        Dice d8 = new Dice(8);
        Dice d6 = new Dice(6);
        Dice d4 = new Dice(4);
        //height/weight calculation
        if(rando.getRace().equals("Human")){
            int heightMod = d10.roll() + 1;
            heightMod += d10.roll() + 1;
            int tempHeight = 56 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d4.roll();
            weightMod += d4.roll();
            rando.setWeight(110 + (heightMod * weightMod));
        }
        else if(rando.getRace().equals("Half-Elf") || rando.getRace().equals("Tiefling")){
            int heightMod = d8.roll() + 1;
            heightMod += d8.roll() + 1;
            int tempHeight = 57 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d4.roll();
            weightMod += d4.roll();
            rando.setWeight(110 + (heightMod * weightMod));
        }
        else if(rando.getRace().equals("Hill Dwarf")){
            int heightMod = d4.roll() + 1;
            heightMod += d4.roll() + 1;
            int tempHeight = 44 + heightMod;
            int inches = tempHeight % 12;
            int feet = tempHeight / 12;
            rando.setHeight(feet + "'" + inches + "\"");
            int weightMod = d6.roll();
            weightMod += d6.roll();
            rando.setWeight(115 + (heightMod * weightMod));
        }
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
        //now that height/weight assignment is done, we move on to NPC traits, using the alignment that's already been generated
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
        //setting flaws
        rando.setFlaw(flaws[d12.roll()]);
        //setting appearances
        rando.setAppearance(appearances[d20.roll()]);
        //setting talents
        rando.setTalent(talents[d20.roll()]);
        //setting mannerisms
        rando.setMannerism(mannerisms[d20.roll()]);
        //setting interaction traits
        rando.setInteractionTrait(interactions[d12.roll()]);
        //setting their randomly assigned stats
        int goodStat = d6.roll();
        int badStat = d6.roll();
        if(badStat == goodStat) {
            while (badStat == goodStat) {
                badStat = d6.roll();
            }
        }
        ArrayList<Integer> rolls = new ArrayList<Integer>();
        for(int i = 0; i < 6; i++){
            int temp = d6.getStat();
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
       //finally, we set their bond
       int tempBond = d10.roll();
       if(tempBond = 10){
           Dice d9 = new Dice(9);
           String tempString;
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

    public int getMaxIndex(ArrayList<Integer> a){
        int maxIndex = 0;
        for(int i = 0; i < a.size(); i++){
            if(a.get(i) > a.get(maxIndex)){
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    public int getMinIndex(ArrayList<Integer> a){
        int minIndex = 0;
        for(int i = 0; i < a.size(); i++){
            if(a.get(i) < a.get(minIndex)){
                minIndex = i;
            }
        }
        return minIndex;
    }
}
