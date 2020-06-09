package com.dbocharov.testneo4j;

import java.util.HashMap;
import java.util.Map;

public class CypherQueryUtils {

    private static CypherQueryUtils instance;

    public String getAllRelationshipsByQuestionQuery(String question){
        return String.format("MATCH (n1)-[r]->(n2) where n1.question = '%s'  RETURN r", question);
    }

    public String getNodeByQuestionAndAnswer(String question, String answer) {
        return String.format("MATCH (n1)-[r]->(n2) where n1.question = '%s' and r.name = '%s'  RETURN n2", question, answer);
    }

    public Map<String, String> generateCypherGetQueryParams(String query){
        Map <String, String> result = new HashMap<>();
        result.put("query", query);
        return result;
    }

    private CypherQueryUtils(){}


    public static CypherQueryUtils getInstance() {
        if (instance == null) {
            synchronized (CypherQueryUtils.class){
                if (instance == null){
                    instance = new CypherQueryUtils();
                }
            }
        }
        return instance;
    }
}
