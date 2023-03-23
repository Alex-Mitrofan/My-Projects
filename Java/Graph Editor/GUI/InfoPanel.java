package GUI;

import CityEditor.Intersection;
import CityEditor.Street;

import javax.swing.*;
import java.awt.*;

public class InfoPanel extends JPanel {
    final MainFrame frame;

    InfoPanel(MainFrame frame){
        this.frame = frame;
        init();
    }
    private void init() {
        setBounds(0, 0, 300, 800);
        setBackground(new Color(0x82879F));
        setOpaque(true);
        setLayout(null);

        JLabel header = new JLabel();
        header.setText("City: " + this.frame.getCity().getName());
        header.setFont(new Font("Comic Sanse", Font.PLAIN, 25));
        header.setBounds(20,30,280,70);

        JLabel body = new JLabel();

        StringBuilder text = new StringBuilder();
        text.append("<html>");
        for(Intersection intersection : this.frame.getCity().getListOfIntersections()){
            text.append(intersection.getNumberName() + ": ");
            text.append(intersection.getName());
            text.append("<br>");
        }

        text.append("<br><br><br><br>");
        for(Street street : this.frame.getCity().getListOfStreets()){
            text.append(street.getName() + ": ");
            for(Intersection intersection : this.frame.getCity().getListOfIntersections())
                if(intersection.getName().equals(street.getIntersection1().getName()))
                    text.append(intersection.getNumberName());
            text.append(" - ");
            for(Intersection intersection : this.frame.getCity().getListOfIntersections())
                if(intersection.getName().equals(street.getIntersection2().getName()))
                    text.append(intersection.getNumberName());


            text.append("<br>");
        }


        text.append("</html>");


        body.setText(String.valueOf(text));
        body.setFont(new Font("Comic Sanse", Font.PLAIN, 20));
        body.setBounds( 20, 150,280,600);

        add(header);
        add(body);
       // setLayout(new GridLayout(9, 1));
    }


}
