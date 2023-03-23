package CityEditor;

import java.util.Objects;

public class Street {
    private String name;
    private Integer length;
    private Intersection intersection1;
    private Intersection intersection2;

    /**
     * Constructor
     */
    public Street(String name, int length) {
        this.name = name;
        this.length = length;
    }


    /**
     * Getters
     */
    public String getName() {
        return name;
    }
    public Integer getLength() {
        return length;
    }
    public Intersection getIntersection1() {
        return intersection1;
    }
    public Intersection getIntersection2() {
        return intersection2;
    }
    /**
     * Setters
     */
    public void setIntersection1(Intersection intersection1) {
        this.intersection1 = intersection1;
    }
    public void setIntersection2(Intersection intersection2) {
        this.intersection2 = intersection2;
    }
    public void setName(String name) {
        this.name = name;
    }

    /**
     * toString function
     */
    @Override
    public String toString() {
        return "( " + name + ", " + length + " )";
    }

    /**
     * equals method
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Street that = (Street) o;
        return Objects.equals(name, that.name);
    }

}

