package com.dbocharov.testneo4j;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ContentType;
import org.apache.hc.core5.http.HttpEntity;
import org.apache.hc.core5.http.ParseException;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.io.entity.StringEntity;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class QuestionActivity extends AppCompatActivity {
    public final static String QUESTION_KEY = "CURRENT_QUESTION";
    final String neo4j_user= "app150253094-11630428245111380";
    final String neo4_password = "b.TUEkTw35WtVH.NY3HIFhT6Kj2cHwr";
    final String neo4_uri = "https://hobby-deeblmpbgjnagbkegbbohnel.dbs.graphenedb.com:24780/db/data/";
    final CypherQueryUtils queryUtils = CypherQueryUtils.getInstance();
    final ObjectMapper mapper = new ObjectMapper();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question);
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }
        Bundle extras = getIntent().getExtras();
        final String currentQuestion = extras != null ? extras.getString(QuestionActivity.QUESTION_KEY) : "";
        final TextView textView = (TextView) findViewById(R.id.question);
        textView.setText(currentQuestion);
        /*String query = "MATCH (n1)-[r]->(n2) where n1.question=\"Как вы оцениваете свое самочувствие?\"  RETURN r, n1, n2";
        String test_result = neo4JMobileClient.executeGetDataQuery(query);*/
        //
        // textView.setText("test_result");

        final RadioGroup radioGroup = (RadioGroup) findViewById(R.id.answers);
        //HorizontalScrollView anwers_view = findViewById(R.id.answers);
        generateAndroidViewForEachAnser(radioGroup, getNodesFromNeo4j(generateJsonRequestEntity(
                queryUtils.generateCypherGetQueryParams(queryUtils.getAllRelationshipsByQuestionQuery(currentQuestion))
        ),"name"));
        final Button nextButton = findViewById(R.id.next);
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                RadioButton checkedRadioButton = findViewById(radioGroup.getCheckedRadioButtonId());
                String checkedOption = checkedRadioButton.getText().toString();
                List <String> questions = getNodesFromNeo4j(generateJsonRequestEntity(
                        queryUtils.generateCypherGetQueryParams(
                                queryUtils.getNodeByQuestionAndAnswer(currentQuestion,checkedOption)
                        )),"question");
                if (questions.size() > 0){
                    Intent intent = new Intent(getBaseContext(), QuestionActivity.class);
                    intent.putExtra(QuestionActivity.QUESTION_KEY, questions.get(0));
                    startActivity(intent);
                } else {
                    List <String> solutions = getNodesFromNeo4j(generateJsonRequestEntity(
                            queryUtils.generateCypherGetQueryParams(
                                    queryUtils.getNodeByQuestionAndAnswer(currentQuestion,checkedOption)
                            )),"solution");
                    String solution = solutions.size() > 0 ? solutions.get(0) : "Error in application, please try again";
                    Intent intent = new Intent(getBaseContext(), SolutionActivity.class);
                    intent.putExtra(SolutionActivity.SOLUTION_KEY, solution);
                    startActivity(intent);
                }

            }
        });

    }





    private List<String> getNodesFromNeo4j(HttpEntity requestEntity, String key) {
        try (final CloseableHttpClient httpclient = HttpClients.createDefault()) {
            HttpPost httpPost = new HttpPost(neo4_uri + "cypher");
            httpPost.setEntity(requestEntity);
            String creds = String.format("%s:%s", neo4j_user, neo4_password);
            String auth = "Basic " + Base64.encodeToString(creds.getBytes(), Base64.NO_WRAP);
            httpPost.addHeader("Authorization", auth);
            CloseableHttpResponse response = httpclient.execute(httpPost);
            return getNodesFromJsonResponseByKey(EntityUtils.toString(response.getEntity()), key);
        } catch (IOException | ParseException ex) {
            ex.printStackTrace();
        }
        return new ArrayList<>();
    }


    private HttpEntity generateJsonRequestEntity(Map<String, String> params){
        ObjectNode objectNode = mapper.createObjectNode();
        for(Map.Entry<String, String> entry : params.entrySet()){
            objectNode.put(entry.getKey(),entry.getValue());
        }
        return new StringEntity(objectNode.toString(), ContentType.APPLICATION_JSON);
    }

    private List<String> getNodesFromJsonResponseByKey(String json, String key) throws IOException {
        return mapper.readTree(json).findValuesAsText(key);
    }
    
    private void generateAndroidViewForEachAnser(RadioGroup view, List<String> answers){
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        params.setMargins(10, 20, 30, 40);
        for (String answer: answers){
            RadioButton radioButton = new RadioButton(this);
            radioButton.setText(answer);
            radioButton.setTextSize(24);
            view.addView(radioButton, params);
        }
    }




}
