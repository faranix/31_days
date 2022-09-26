package fr.faranix;

import java.util.Comparator;

public class Toys {
    private String name;
    private String description;
    private Double price;
    private Double promotion;

    public Toys(String name, String description, Double price, Double promotion) {
        this.name = name;
        this.description = description;
        this.price = price;
        this.promotion = promotion;
    }

    /**
     * Permets d'obtenir le nom.
     * 
     * @return le nom.
     */
    public String getName() {
        return name;
    }

    /**
     * Permets de redéfinir le nom.
     */
    public void setName() {
        this.name = name;
    }

    /**
     * Permets d'obtenir la description.
     * 
     * @return la description.
     */
    public String getDescription() {
        return description;
    }

    /**
     * Permets de redéfinir la description.
     */
    public void setDescription() {
        this.description = description;
    }

    /**
     * Permets d'obtenir le prix.
     * 
     * @return le prix.
     */
    public Double getPrice() {
        return price;
    }

    /**
     * Permets de redéfinir le prix.
     */
    public void setPrice() {
        this.price = price;
    }

    /**
     * Permets d'obtenir la promotion.
     * 
     * @return la promotion.
     */
    public Double getPromotion() {
        return promotion;
    }

    /**
     * Permets de redéfinir la promotion.
     */
    public void setPromotion() {
        this.promotion = promotion;
    }

    /*
     * Trier les jouet par leur prix.
     */
    public static class SortPrice implements Comparator<Toys> {

        @Override
        public int compare(Toys s1, Toys s2) {
            return s1.getPrice().compareTo(s2.getPrice());
        }

    }
}
