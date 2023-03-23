package CityEditor;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Intersection {
    private String name;
    private int nrOfStreets;
    private List<Street> listOfStreets = new ArrayList<>();
    private List<Intersection> neighbours = new ArrayList<>();
    private Integer numberName; //used when graph is drawn

    /**
     *Constructor
     */
    public Intersection(String name) {
        this.name = name;
        this.nrOfStreets = 0;
    }

    /**
     *Getters
     */
    public Integer getNrOfStreets() {
        return nrOfStreets;
    }
    public List<Street> getListOfStreets() {
        return listOfStreets;
    }
    public String getName() {
        return name;
    }
    public List<Intersection> getNeighbours() {
        return neighbours;
    }
    public Integer getNumberName() {
        return numberName;
    }

    /**
     * Setters
     */
    public void setName(String name) {
        this.name = name;
    }
    public void setNumberName(Integer numberName) {
        this.numberName = numberName;
    }

    /**
     *incrementNrOfStreets by 1
     */
    public void incrementNrOfStreets() {
        this.nrOfStreets ++;
    }

    /**
     * addStreet functions adds a street to the list
     */
    public void addStreet(Street street)
    {
        this.listOfStreets.add(street);
    }

    /**
     * addNeighbour function add an Intersection to neighbour list
     */
    public void addNeighbour(Intersection intersection){
        this.neighbours.add(intersection);
    }
    /**
     * printNeighbours functions
     * (not used)
     */
  /*
    public void printNeighbours(){
        for(Intersection intersection : this.neighbours)
            System.out.println(intersection);
    }
*/
    /**
     *toString function
     */
    @Override
    public String toString() {
        return  name + ": ";
    }
    /**
     * equals method
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Intersection that = (Intersection) o;
        return Objects.equals(name, that.name);
    }

}
