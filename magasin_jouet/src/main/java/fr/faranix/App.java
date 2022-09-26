package fr.faranix;

import java.util.ArrayList;
import java.util.Collections;

public class App {
    public static void main(String[] args) {
        String[] toys = {
                "Barbie", "Yo-Yo", "L'écran magique",
                "Le Hula Hoop", "Les Lego", "Rubik's Cube",
                "Le Super Soaker", "Les voitures miniatures",
                "Les GI-Joe", "Les figurines Star Wars"
        };

        ArrayList<String> listOfToys = new ArrayList<>();

        // === Ajoute les jouets dans la liste === //
        for (int i = 0; i < toys.length; i++) {
            listOfToys.add(toys[i]);
        }

        System.out.println(listOfToys);
        Collections.sort(listOfToys);

        Toys toys1 = new Toys("test de la description", 20, 25.5);

        System.out.println(toys1.getDescription());

    }
}
