package fr.faranix;

public class Toys {
    private String description;
    private Number price;
    private Double promotion;

    public Toys(String description, Number price, Double promotion) {
        this.description = description;
        this.price = price;
        this.promotion = promotion;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription() {
        this.description = description;
    }

    public Number getPrice() {
        return price;
    }

    public void setPrice() {
        this.price = price;
    }

    public Double getPromotion() {
        return promotion;
    }

    public void setPromotion() {
        this.promotion = promotion;
    }
}
