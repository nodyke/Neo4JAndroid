package com.dbocharov.testneo4j.neo4utils;

//import org.neo4j.jdbc.Driver;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Neo4jJdbcClient {
    final String user,password,uri;

    public Neo4jJdbcClient(String user, String password, String uri) {
        this.user = user;
        this.password = password;
        this.uri = uri;
    }

    public String executeQuery(String query){
        StringBuilder result = new StringBuilder("Start\n");
        try(Connection con = DriverManager.getConnection(uri,user,password)){
            try(PreparedStatement stmt = con.prepareStatement(query)){
                try(ResultSet rs = stmt.executeQuery()){
                    while (rs.next()){
                        result.append("RECORD:");
                        result.append(rs.toString());
                        result.append("\n");
                    }
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        result.append("End");
        return result.toString();
    }
}
