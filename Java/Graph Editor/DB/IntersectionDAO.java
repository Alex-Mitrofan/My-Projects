package DB;

import java.sql.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class IntersectionDAO {

    public IntersectionDAO() {}
    /**
     * create method inserts in the table intersectii attributes: id, oras, nume
     */
    public void create(Integer id, String nume, Integer numar, String oras) throws SQLException {
        Connection connection = Database.getConnection();
        try (PreparedStatement preparedStatement = connection.prepareStatement("insert into intersectii (ID,NUME,NUMAR,ORAS) values (?,?,?,?)"))
        {
            preparedStatement.setInt(1, id);
            preparedStatement.setString(2, nume);
            preparedStatement.setInt(3,numar);
            preparedStatement.setString(4, oras);

            preparedStatement.execute();
        }

    }

    public boolean findCity(String name) throws SQLException{
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(
                     "select * from intersectii where oras='" + name + "'")) {
            if (resultSet.next())
                return true;
            else return false;
        }
    }


    /**
     * findByName find and prints attributes from the database.
     */
    public ArrayList<String> findByName(String name) throws SQLException {
        ArrayList<String> output = new ArrayList<>();
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(
                     "select * from intersectii where nume='" + name + "'")) {
            if(resultSet.next()){
                //System.out.println(resultSet.getInt(1)+"  "+resultSet.getString(2)+"  "+resultSet.getInt(3) + "  "+resultSet.getString(4));
                output.add(String.valueOf(resultSet.getInt(1)));
                output.add(resultSet.getString(2));
                output.add(String.valueOf(resultSet.getInt(3)));
                output.add(resultSet.getString(4));
            }
            else //System.out.println("This intersection doesn't exist");
                return null;

            return output;
        }
    }

    /**
     * findById method find and prints attributes from the database.
     */
    public void findById(int id) throws SQLException {
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("select * from intersectii where id='" + id + "'")) {
            if(resultSet.next())  System.out.println(resultSet.getInt(1)+"  "+resultSet.getString(2)+"  "+resultSet.getInt(3) + "  "+resultSet.getString(4));
            else System.out.println("This intersection doesn't exist");
        }
    }
    /**
     * finMaxId method finds maximum id from the table
     */
    public int findMaxId() throws SQLException {
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("select max(id) from intersectii")) {
            resultSet.next();
             return resultSet.getInt(1);
        }
    }
    /**
     * getFirstCities method finds maximum id from the table
     */
    public ArrayList<String> getFirstCities() throws SQLException {
        ArrayList<String> cities = new ArrayList<>();

        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("select distinct oras from intersectii")) {
            while (resultSet.next())
                cities.add(resultSet.getString(1));

            return cities;
        }
    }
    /**
     * findIntersectionsByCity
     */
    public ArrayList<String> findIntersectionsByCity(String cityName) throws SQLException {
        ArrayList<String> output = new ArrayList<>();
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(
                     "select nume from intersectii where oras='" + cityName + "'")) {
            while(resultSet.next())
                output.add(resultSet.getString(1));
            return output;
        }
    }

}
