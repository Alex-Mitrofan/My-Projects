package DB;

import java.sql.*;
import java.util.ArrayList;

public class StreetDAO {
    public StreetDAO() {}
    /**
     * create method inserts in the table intersectii attributes: id, intersectie1, intersectie2, lungime, oras, nume
     */
    public void create(Integer id,String nume, Integer lungime, String oras, String intersectie1, String intersectie2) throws SQLException {
        Connection connection = Database.getConnection();
        try (PreparedStatement preparedStatement = connection.prepareStatement("insert into strazi (ID,NUME,LUNGIME,ORAS,INTERSECTIE1,INTERSECTIE2) values (?,?,?,?,?,?)"))
        {
            preparedStatement.setInt(1, id);
            preparedStatement.setString(2, nume);
            preparedStatement.setInt(3, lungime);
            preparedStatement.setString(4, oras);
            preparedStatement.setString(5, intersectie1);
            preparedStatement.setString(6, intersectie2);

            preparedStatement.execute();
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
                     "select * from strazi where nume='" + name + "'")) {
            if(resultSet.next())  {
                output.add(String.valueOf(resultSet.getInt(1)));
                output.add(resultSet.getString(2));
                output.add(String.valueOf(resultSet.getInt(3)));
                output.add(resultSet.getString(4));
                output.add(resultSet.getString(5));
                output.add(resultSet.getString(6));
                //System.out.println(resultSet.getInt(1)+"  "+resultSet.getString(2)+"  "+resultSet.getInt(3)+" "+resultSet.getString(4)+" "+resultSet.getString(5)+" "+resultSet.getString(6));
            }
            else //System.out.println("This street doesn't exist");
                return null;
        }
        return output;
    }

    /**
     * findById method find and prints attributes from the database.
     */
    public void findById(int id) throws SQLException {
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("select * from strazi where id='" + id + "'")) {
            if(resultSet.next())  System.out.println(resultSet.getInt(1)+"  "+resultSet.getString(2)+"  "+resultSet.getInt(3)+" "+resultSet.getString(4)+" "+resultSet.getString(5)+" "+resultSet.getString(6));
            else System.out.println("This street doesn't exist");
        }
    }
    /**
     * finMaxId method finds maximum id from the table
     */
    public int findMaxId() throws SQLException {
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("select max(id) from strazi")) {
             resultSet.next();
             return resultSet.getInt(1);
        }
    }
    /**
     * findStreetsByCity
     */
    public ArrayList<String> findStreetsByCity (String cityName) throws SQLException {
        ArrayList<String> output = new ArrayList<>();
        Connection connection = Database.getConnection();
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(
                     "select nume from strazi where oras='" + cityName + "'")) {
            while(resultSet.next())
                output.add(resultSet.getString(1));
            return output;
        }
    }
}
