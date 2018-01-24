"""
 * This rolls a n sided die where n is provided
 * Now implemented in python
 * @Author Brady Klein
 * @Date 01/11/18
 """

class Dice :
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

    def getStat getStat():
        possibles
        possibles[0] = rand.nextInt(6);
        possibles[1] = rand.nextInt(6);
        possibles[2] = rand.nextInt(6);
        possibles[3] = rand.nextInt(6);
        int minIndex = 0;
        for(int i = 0; i < 4; i++){
            if(possibles[i] < possibles[minIndex]){
                minIndex = i;
            }
        }
        int stat = 0;
        for(int i = 0; i < 4; i++){
            if(i != minIndex){
                stat += possibles[minIndex] + 1;
            }
        }
        return stat;
    }

