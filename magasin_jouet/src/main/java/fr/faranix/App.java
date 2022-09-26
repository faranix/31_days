package fr.faranix;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.lang.Double;

public class App {
    public static void main(String[] args) {
        Object[][] toys = {
                {
                        "Barbie", "Une barbie", 25.0, 25.5
                },
                {
                        "Yo-Yo", "Un yo-yo", 10.2, 10.0
                },
                {
                        "L'écran magique", "Un écran magique", 125.0, 50.0
                },
                {
                        "Le Hula Hoop", "un hula hoop", 55.0, 45.5
                },
                {
                        "Les Legos", "Des legos", 215.0, 25.5
                },
                {
                        "Rubik's Cube", "Un rubik's cube", 5.0, 0.0
                },
                {
                        "Le Super Soaker", "Le super soaker", 25.0, 25.5
                },
                {
                        "Les voitures miniatures", "des voitures miniatures", 2.0, 30.0
                },
                {
                        "Les GI-Joe", "les GI-Joe", 25.0, 25.5
                },
                {
                        "Les figurines Star War", "des figurines Star War", 155.0, 85.5
                },
        };

        // === Création d'une liste de Toys === //
        List<Toys> listOfToys = new ArrayList<Toys>();

        // === Ajouts des jouets dans la liste === //
        for (int i = 0; i < toys.length; i++) {
            listOfToys
                    .add(new Toys((String) toys[i][0], (String) toys[i][1], (Double) toys[i][2], (Double) toys[i][3]));
        }

        // Tri la liste par prix.
        Collections.sort(listOfToys, new Toys.SortPrice());

        for (Toys element : listOfToys) {
            System.out.println(element.getPrice());
        }
    }
}
