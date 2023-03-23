package CityEditor;

import GUI.DrawGraph;
import com.github.javafaker.Faker;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class CityBuilder {
    private int numberOfIntersections;
    private int maxNrOfStreets;

    /**
     * Constructors
     */
    public CityBuilder(int numberOfIntersections) {
        this.numberOfIntersections=numberOfIntersections;
        maxNrOfStreets = 5;
    }
    public CityBuilder() {
        Random random = new Random();
        this.numberOfIntersections=random.nextInt(5)+3;
        maxNrOfStreets=5;
    }

    /**
     * Getters
     */
    public int getNumberOfIntersections() {
        return numberOfIntersections;
    }
    public int getMaxNrOfStreets() {
        return maxNrOfStreets;
    }

    /**
     * Setters
     */
    public void setNumberOfIntersections(int numberOfIntersections) {
        this.numberOfIntersections = numberOfIntersections;
    }
    public void setMaxNrOfStreets(int maxNrOfStreets) {
        this.maxNrOfStreets = maxNrOfStreets;
    }

    /**
     * GenerateRandomCity function generates a random city
     */
    public City generateRandomCity() throws SQLException, IOException {
        List<Street> listOfStreets = new ArrayList<>();
        List<Intersection> listOfIntersections = new ArrayList<>();
        List<Pair<Intersection, ArrayList<Street>>> listOfPairs = new ArrayList<>();


        for(int i = 0; i < this.numberOfIntersections; i++){  //<--- generate listOfIntersections
            //Generate a new intersection
            Intersection intersection = new Intersection(new Faker().name().lastName());
           // this.numberOfIntersections++;

            //Verify if the intersection already exists

            for (Intersection intersectionList : listOfIntersections) {
                if (intersection.equals(intersectionList)) {
                    intersection.setName(String.valueOf(new Faker().funnyName()));
                    break;
                }
            }
                //add the new intersection to the listOfIntersections
                listOfIntersections.add(intersection);
            }


        for(Intersection intersection : listOfIntersections)  //<----foreach intersection generate random streets
        {
            Random random = new Random();
            int limit = random.nextInt(4) + 1 - intersection.getNrOfStreets();  //o intersectie va avea intre 2 si 5 strazi

            for(int i = 0; i < limit-1; i++) {

                //generate cost and name of the street with index i
                random = new Random();
                int length = random.nextInt(9) + 1;  //lungimea strazii este intre 1 si 10
                Street street = new Street(new Faker().address().streetName(), length);

                //Verify if the street name already exists
                for (Street streetList : listOfStreets) {
                    if (street.equals(streetList)) {
                        street.setName(String.valueOf(new Faker().funnyName()));
                        break;
                    }
                }

                if(limit > intersection.getNrOfStreets())
                {

                    //search the second intersection for the street
                    for(Intersection intersection2 : listOfIntersections){
                        if(!intersection2.equals(intersection)){
                            if(intersection2.getNrOfStreets()<5){

                                //verify if a street already exists between the two intersections
                                boolean streetAlreadyExists = false;
                                for(Street verifyStreet : listOfStreets)
                                    if((verifyStreet.getIntersection1().equals(intersection) && verifyStreet.getIntersection2().equals(intersection2))
                                    || verifyStreet.getIntersection2().equals(intersection) && verifyStreet.getIntersection1().equals(intersection2)) {
                                        streetAlreadyExists = true;
                                        break;
                                    }

                                if(!streetAlreadyExists) {
                                    street.setIntersection1(intersection);   //add the first intersection to the current street
                                    intersection.incrementNrOfStreets();
                                    intersection.addStreet(street);

                                    street.setIntersection2(intersection2);   //add second intersection to the current street
                                    intersection2.incrementNrOfStreets();
                                    intersection2.addStreet(street);


                                    //add neighbours for both intersection and intersection2
                                    //(we don't add duplicates to the neighbour list)
                                    if (!intersection.getNeighbours().contains(intersection2))
                                        intersection.addNeighbour(intersection2);
                                    if (!intersection2.getNeighbours().contains(intersection))
                                        intersection2.addNeighbour(intersection);

                                    //add the new street to the listOfStreets
                                    listOfStreets.add(street);

                                    break;
                                }
                            }
                        }
                    }
                }
            }
            //create a pais and add it to the listOfPairs
            Pair<Intersection, ArrayList<Street>> pair = new Pair<>(intersection, intersection.getListOfStreets());
            listOfPairs.add(pair);
        }


        City city = new City(listOfPairs);
        city.setName(new Faker().address().city());
        city.setListOfIntersections(listOfIntersections);
        city.setListOfStreets(listOfStreets);

        /*
        Database myDatabase=new Database();
        try{
                Class.forName("oracle.jdbc.driver.OracleDriver");
                Database.createConnection();
            //Add intersections and streets in the database
            IntersectionDAO intersectionDAO = new IntersectionDAO();
            int id = 6;
            for(Intersection intersection : listOfIntersections) {
                intersectionDAO.create(id, city.getName(), intersection.getName());
                id++;
            }
            StreetDAO streetDAO = new StreetDAO();
            id=11;
            for(Street street : listOfStreets){
                streetDAO.create(id, street.getIntersection1(), street.getIntersection2(), street.getLength(), city.getName(), street.getName());
                id++;
            }
            Database.closeConnection();
        }catch(Exception e){ System.out.println(e);}
*/
        return city;

    }
}
