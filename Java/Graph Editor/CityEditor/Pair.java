package CityEditor;

import java.util.ArrayList;
import java.util.List;

public class Pair<Intersection, ArrayList > {
    private Intersection intersection;
    private List<Street> listOfStreets = new java.util.ArrayList<>();
    /**
     * Constructor
     */
    public Pair(Intersection intersection, List<Street> listOfStreets) {
        this.intersection = intersection;
        this.listOfStreets = listOfStreets;
    }
    /**
     * toString function
     */
    @Override
    public String toString() {
        StringBuilder streetNames = new StringBuilder();
        for(Street street:listOfStreets){
            streetNames.append("( ");
            streetNames.append(street.getName());
            streetNames.append(", ");
            streetNames.append(street.getLength());
            streetNames.append(" )  ");
        }
       return  intersection + " " + String.valueOf(streetNames) + '\n';

    }
}
