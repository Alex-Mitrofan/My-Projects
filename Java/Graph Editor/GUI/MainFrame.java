package GUI;

import CityEditor.City;
import CityEditor.CityBuilder;
import CityEditor.Intersection;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class MainFrame extends JFrame{
    DrawGraph drawGraph;
    ControlPanel controlPanel;
    InfoPanel infoPanel;
    private List<Intersection> nodeList = new ArrayList<>();
    private City city;



    public MainFrame(City city) throws SQLException, IOException {
        super();
        setNodeList(city.getListOfIntersections());
        setCity(city);
        InitFrame();
    }

    /**
     *InitFrame initialize the frame
     */
    public void InitFrame() throws SQLException, IOException {
        setTitle("Traffic Simulator");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setSize(1500,800);
        setLocationRelativeTo(null);
        setLayout(null);
        //setUndecorated(true);

        ImageIcon icon = new ImageIcon("src/main/resources/icon.png"); //adds favicon
        setIconImage(icon.getImage());


        drawGraph = new DrawGraph(this, nodeList);
        add(drawGraph, BorderLayout.CENTER);

        controlPanel = new ControlPanel(this);
        add(controlPanel, BorderLayout.EAST);

        infoPanel = new InfoPanel(this);
        add(infoPanel, BorderLayout.WEST);

    }

    /**
     * Setters
     */
    public void setNodeList(List<Intersection> nodeList) {
        this.nodeList = nodeList;
    }
    public void setCity(City city) {
        this.city = city;
    }

    /**
     * Getters
     */
    public List<Intersection> getNodeList() {
        return nodeList;
    }
    public City getCity() {
        return city;
    }
}
