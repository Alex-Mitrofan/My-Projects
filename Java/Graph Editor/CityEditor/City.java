package CityEditor;

import java.util.ArrayList;
import java.util.List;

public class City {
    private String name = null;
    /**
     * Lista cu perechi de tipul <CityEditor.Intersection, List of Streets>
     */
    private List<Pair<Intersection, ArrayList<Street>>> cityMap = new ArrayList<>();
    private List<Intersection> listOfIntersections = new ArrayList<>();
    private List<Street> listOfStreets = new ArrayList<>();
    /**
     * Constructor
     */
    public City(List<Pair<Intersection, ArrayList<Street>>> cityMap) {
        this.cityMap = cityMap;
    }
    public City() {
        this.cityMap = null;
    }
    /**
     * Getters
     */
    public String getName() {
        return name;
    }
    public List<Intersection> getListOfIntersections() {
        return listOfIntersections;
    }
    public List<Street> getListOfStreets() {
        return listOfStreets;
    }
    /**
     *Setters
     */
    public void setName(String name) {
        this.name = name;
    }
    public void setListOfIntersections(List<Intersection> listOfIntersections) {
        this.listOfIntersections = listOfIntersections;
    }
    public void setListOfStreets(List<Street> listOfStreets) {
        this.listOfStreets = listOfStreets;
    }

    /**
     * toString function
     */

    @Override
    public String toString() {
        StringBuilder list = new StringBuilder();
        for(Pair pair : cityMap){
            list.append(pair);
            //list.append('\n');
        }

        return String.valueOf(this.name) + '\n' +
                 String.valueOf(list);
    }
}
