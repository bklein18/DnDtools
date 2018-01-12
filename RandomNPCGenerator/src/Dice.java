import java.util.Random;

/**
 * This rolls a n sided die where n is provided
 * @Author Brady Klein
 * @Date 01/11/18
 */

public class Dice {
    //attributes
    private int sides;
    private Random rand = new Random();
    //constructor
    public Dice(int sides){
        this.sides = sides;
    }
    //method
    public int roll(){
        return rand.nextInt(sides);
    }

    public int getStat(){
        int possibles[] = new int[4];
        possibles[0] = rand.nextInt(6);
    }
}
