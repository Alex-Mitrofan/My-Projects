package GUI;

import CityEditor.City;
import CityEditor.CityBuilder;
import CityEditor.Intersection;
import CityEditor.Street;
import DB.Database;
import DB.IntersectionDAO;
import DB.StreetDAO;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class ControlPanel extends JPanel implements ActionListener {
    final MainFrame frame;
    JButton exitBtn = new JButton("Exit ");
    JButton loadBtn = new JButton("Load");
    JButton saveBtn = new JButton("Save");
    JButton generateBtn = new JButton ("Random Generate");
    String loadCityName;
    private final  List<JButton> buttons = new ArrayList<>();
    private final  List<Intersection> listOfIntersections = new ArrayList<>();
    private final  List<Street> listOfStreets = new ArrayList<>();

    ControlPanel(MainFrame frame){
        this.frame = frame;
        init();
    }

    private void init() {
        setBounds(1200,0,300,800);
        setBackground(new Color(0x82879F));
        setLayout(new GridLayout(9,1));

        JPanel firstRow = new JPanel();
        firstRow.setLayout(new GridLayout(1,3));
        firstRow.add(exitBtn);
        firstRow.add(loadBtn);
        firstRow.add(saveBtn);

        JPanel secondRow = new JPanel();
        secondRow.setLayout(new FlowLayout(FlowLayout.CENTER));
        secondRow.add(generateBtn);
        secondRow.setBackground(new Color(0x82879F));


        add(firstRow);
        add(secondRow);


        exitBtn.addActionListener(this::exitGame);
        exitBtn.setFont(new Font("Comic Sanse", Font.PLAIN, 15));
        exitBtn.setFocusable(false);
       // exitBtn.setPreferredSize(new Dimension(100,100));

        loadBtn.setFont(new Font("Comic Sanse", Font.PLAIN, 15));
        loadBtn.setFocusable(false);
        loadBtn.addActionListener(this::load);
        //loadBtn.setPreferredSize(new Dimension(100,100));

        saveBtn.setFont(new Font("Comic Sanse", Font.PLAIN, 15));
        saveBtn.setFocusable(false);
        saveBtn.addActionListener(this::save);
        //saveBtn.setPreferredSize(new Dimension(100,100));

        generateBtn.setFont(new Font("Comic Sanse", Font.PLAIN, 15));
        generateBtn.setFocusable(false);
        generateBtn.addActionListener(this::generateRandomCity);
        generateBtn.setPreferredSize(new Dimension(220, 70));



    }
    /**
     * exitGame called when exitBtn is pressed
     */
    private void exitGame(ActionEvent e) {
        frame.dispose();
    }

    /**
     * save called when saveBtn is pressed
     */
    private void save(ActionEvent e){
        try {
            Database myDatabase=new Database();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        try{
            Class.forName("oracle.jdbc.driver.OracleDriver");
            Database.createConnection();
            //Add intersections and streets in the database
            IntersectionDAO intersectionDAO = new IntersectionDAO();
            //int id = intersectionDAO.findMaxId() + 1;

int id=1;
            if(!intersectionDAO.findCity(this.frame.getCity().getName())) {
                for (Intersection intersection : this.frame.getCity().getListOfIntersections()) {
                    intersectionDAO.create(id, intersection.getName(), intersection.getNumberName(), this.frame.getCity().getName());
                    id++;
                }
                StreetDAO streetDAO = new StreetDAO();
                //id = streetDAO.findMaxId() + 1;

id=1;
                for (Street street : this.frame.getCity().getListOfStreets()) {
                    streetDAO.create(id, street.getName(), street.getLength(), this.frame.getCity().getName(), street.getIntersection1().getName(), street.getIntersection2().getName() );
                    id++;
                }
                Database.closeConnection();
            }
            else System.out.println("City already exists in database");
        }catch(Exception ee){ System.out.println(ee);}
    }

    /**
     * generateRandomCity called when generateBtn is pressed
     */
    private void generateRandomCity(ActionEvent e) {

        //create a new random city
        CityBuilder cityBuilder = new CityBuilder();
        City city = new City();
        try {
            city = cityBuilder.generateRandomCity();
        } catch (SQLException | IOException ex) {
            ex.printStackTrace();
        }
        System.out.println("New city generated:");
        System.out.println(city);

        this.frame.remove(this.frame.drawGraph);

        //set the new city
        this.frame.setCity(city);

        try {
            this.frame.drawGraph = new DrawGraph(this.frame, city.getListOfIntersections());
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        this.frame.add(this.frame.drawGraph, BorderLayout.CENTER);

        //update the new infoPanel
        this.frame.remove(this.frame.infoPanel);
        this.frame.infoPanel = new InfoPanel(this.frame);
        this.frame.add(this.frame.infoPanel, BorderLayout.WEST);

        this.frame.revalidate();
        this.frame.repaint();

    }
    /**
     *load called when loadBtn is pressed
     */
    public void load(ActionEvent e){
        //remove old controlPanel from MainFrame
        this.frame.remove(this.frame.controlPanel);
        this.frame.controlPanel = new ControlPanel(this.frame);


        //add new controlPanel to MainFrame
        ArrayList<String> cities = new ArrayList<>();

        try {
            Database myDatabase=new Database();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        try{
            Class.forName("oracle.jdbc.driver.OracleDriver");
            Database.createConnection();
            //Add intersections and streets in the database
            IntersectionDAO intersectionDAO = new IntersectionDAO();
            cities = intersectionDAO.getFirstCities();

            int count=0; //used for naming buttons
            for(String cityName : cities){
                count++;
                JButton button = new JButton(cityName);

                JPanel panel = new JPanel();
                panel.setLayout(new FlowLayout(FlowLayout.CENTER));
                panel.add(button);
                panel.setBackground(new Color(0x82879F));


                button.setFont(new Font("Comic Sanse", Font.PLAIN, 15));
                button.setFocusable(false);
                button.setName("button" + count);
                this.buttons.add(button);
                button.addActionListener(this::loadCity);
                button.setPreferredSize(new Dimension(220, 70));

                this.frame.controlPanel.add(panel);
            }

            Database.closeConnection();
        }catch(Exception ee){ System.out.println(ee);}

        this.frame.add(this.frame.controlPanel, BorderLayout.WEST);
        revalidate();
        repaint();
        this.frame.revalidate();
        this.frame.repaint();

    }

    /**
     *loadCity called when buttons under the loadBtn are pressed
     */
    public void loadCity(ActionEvent e) {
        for(JButton button : this.buttons)
            if(button.equals(e.getSource()))
                this.loadCityName=button.getText();   //get text from the pressed button


        try {
            Database myDatabase=new Database();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        try{
            Class.forName("oracle.jdbc.driver.OracleDriver");
            Database.createConnection();
            IntersectionDAO intersectionDAO = new IntersectionDAO();
            ArrayList<String> intersections = new ArrayList<>();
            intersections = intersectionDAO.findIntersectionsByCity(this.loadCityName);  //we got the intersections names from database

            //foreach intersection name we recreate the intersection objects
            for(String name : intersections){
                Intersection newIntersection = new Intersection(name);
                ArrayList<String> intersectionInfo = new ArrayList<>();
                intersectionInfo = intersectionDAO.findByName(name);
                newIntersection.setNumberName(Integer.valueOf(intersectionInfo.get(2))); //set the number name of the intersection

                this.listOfIntersections.add(newIntersection);


            }

            //recreate streets from the database
            StreetDAO streetDAO = new StreetDAO();
            ArrayList<String> streets = new ArrayList<>();
            streets = streetDAO.findStreetsByCity(this.loadCityName);

            for(String name : streets){
                Street newStreet = new Street(name, 1);
                ArrayList<String> streetInfo = new ArrayList<>();
                streetInfo = streetDAO.findByName(name);

                //find intersection1
                for(Intersection intersection : this.listOfIntersections)
                    if(intersection.getName().equals(streetInfo.get(4)))
                        newStreet.setIntersection1(intersection);
                //find intersection2
                for(Intersection intersection : this.listOfIntersections)
                    if(intersection.getName().equals(streetInfo.get(5)))
                        newStreet.setIntersection2(intersection);

                newStreet.getIntersection1().addNeighbour(newStreet.getIntersection2()); //add neighbours for intersection
                newStreet.getIntersection2().addNeighbour(newStreet.getIntersection1());

               this.listOfStreets.add(newStreet);
            }


            Database.closeConnection();
        }catch(Exception ee){ System.out.println(ee);}




      //DrawGraph with the new input city
        this.frame.remove(this.frame.drawGraph);

        this.frame.getCity().setListOfStreets(listOfStreets);
        this.frame.getCity().setListOfIntersections(listOfIntersections);
        this.frame.setNodeList(listOfIntersections);
        this.frame.getCity().setName(loadCityName);

        try {
            this.frame.drawGraph = new DrawGraph(this.frame, listOfIntersections);
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        this.frame.add(this.frame.drawGraph, BorderLayout.CENTER);

        // remove old controlPanel from MainFrame
        this.frame.remove(this.frame.controlPanel);
        this.frame.controlPanel = new ControlPanel(this.frame);
        this.frame.add(this.frame.controlPanel, BorderLayout.WEST);

        //update infoPanel
        this.frame.remove(this.frame.infoPanel);
        this.frame.infoPanel = new InfoPanel(this.frame);
        this.frame.add(this.frame.infoPanel, BorderLayout.EAST);

        this.frame.revalidate();
        this.frame.repaint();

    }

    @Override
    public void actionPerformed(ActionEvent e) {

    }
}
