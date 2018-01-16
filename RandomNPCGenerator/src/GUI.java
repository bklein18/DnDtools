import java.swing.*;

public class GUI{
    //attributes

    //constructor
    public GUI(){
     JFrame frame = new JFrame("Random NPC Generator");
     JPanel panel = new JPanel();
     frame.add(panel);
     Label test = new Label("test");
     panel.add(test);
     frame.setVisibile(true);
    }
    //methods

    //main method
    public static void main(String args[]){
        new GUI();
    }
}