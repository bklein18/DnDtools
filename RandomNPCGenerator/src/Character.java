import java.util.ArrayList;

/**
 * This class acts as an object to hold all character info as a utility for the main class
 * @Author Brady Klein
 * @Date 01/11/18
 */

public class Character {
    //attributes
    private String race;
    private String gender;
    private String height;
    private int weight;
    private int stats[];
    private String mannerism;
    private String appearance;
    private String talent;
    private String alignment;
    private String ideal;
    private String bond;
    private String flaw;
    private String interactionTrait;
    //constructor
    public Character(){
        Dice d = new Dice(3);
        int lawVChaos = d.roll();
        int goodVEvil = d.roll();
        String law[] = {"Lawful", "Neutral", "Chaotic"};
        String good[] = {"Good", "Neutral", "Evil"};
        if(lawVChaos == 1 && goodVEvil == 1){
            this.alignment = "True Neutral";
        }
        else{
            this.alignment = law[lawVChaos] + " " + good[goodVEvil];
        }
    }
    //methods
    public void printCharacter(){
        System.out.printf("The NPC generated is a nameless ")
    }

    public String getRace() {
        return race;
    }

    public void setRace(String race) {
        this.race = race;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int[] getStats() {
        return stats;
    }

    public void setStats(int stats[]) {
        this.stats = stats;
    }

    public String getMannerism() {
        return mannerism;
    }

    public void setMannerism(String mannerism) {
        this.mannerism = mannerism;
    }

    public String getAppearance() {
        return appearance;
    }

    public void setAppearance(String appearance) {
        this.appearance = appearance;
    }

    public String getTalent() {
        return talent;
    }

    public void setTalent(String talent) {
        this.talent = talent;
    }

    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }

    public String getIdeal() {
        return ideal;
    }

    public void setIdeal(String ideal) {
        this.ideal = ideal;
    }

    public String getBond() {
        return bond;
    }

    public void setBond(String bond) {
        this.bond = bond;
    }

    public String getFlaw() {
        return flaw;
    }

    public void setFlaw(String flaw) {
        this.flaw = flaw;
    }

    public String getInteractionTrait() {
        return interactionTrait;
    }

    public void setInteractionTrait(String interactionTrait) {
        this.interactionTrait = interactionTrait;
    }
}
