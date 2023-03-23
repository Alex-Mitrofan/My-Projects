import CityEditor.*;
import DB.Database;
import DB.IntersectionDAO;
import DB.StreetDAO;
import GUI.MainFrame;
import com.github.javafaker.Faker;
import oracle.jdbc.OracleType;

import java.io.IOException;
import java.sql.CallableStatement;
import java.sql.SQLException;
import java.sql.Types;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.concurrent.Callable;



public class Main {
    public static void main(String[] args) throws SQLException, IOException {

        CityBuilder cityBuilder = new CityBuilder();
        City city = new City();
        city = cityBuilder.generateRandomCity();
        System.out.println(city);

         new MainFrame(city).setVisible(true);




         Database myDatabase=new Database();
        try{
            Class.forName("oracle.jdbc.driver.OracleDriver");
            Database.createConnection();
            IntersectionDAO intersectionDAO = new IntersectionDAO();

            CallableStatement callableStatement = Database.getConnection().prepareCall("{CALL graf_complet(?,?,?)}");
            callableStatement.registerOutParameter(2, Types.VARCHAR);
            callableStatement.registerOutParameter(3, Types.VARCHAR);
            String cityName = new String();
            cityName = "North Kenishamouth";
            callableStatement.setString(1, cityName);

            callableStatement.execute();

            String result1 = callableStatement.getString(2);
            String result2 = callableStatement.getString(3);
            System.out.println("Nu exista strada intre intersectia " + result1 + " si " + result2);
            if(result1 != null && result2 != null)
                System.out.println("Graful nu este complet");
            else System.out.println("Graful este complet");


            Database.closeConnection();
        }catch(Exception e){ System.out.println(e);}


    }
}

