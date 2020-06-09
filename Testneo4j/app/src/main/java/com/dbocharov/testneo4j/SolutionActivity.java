package com.dbocharov.testneo4j;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class SolutionActivity extends AppCompatActivity {
    public static final String SOLUTION_KEY = "CURRENT_SOLUTION";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_solution);
        Bundle extras = getIntent().getExtras();
        final String currentSolution = extras != null ? extras.getString(SolutionActivity.SOLUTION_KEY) : "";
        if ("Плановая диспансеризация".equals(currentSolution)){
            TextView textView = findViewById(R.id.doctor);
            textView.setText(currentSolution);
            TextView textView1 = findViewById(R.id.research);
            textView1.setText("");
        }
        else {
            TextView textView = findViewById(R.id.doctor);
            String[] temp = currentSolution.split(" с ");
            String recomendation = temp[0];
            textView.setText(recomendation);
            TextView textView1 = findViewById(R.id.research);
            textView1.setText(temp[temp.length - 1]);
        }
        final Button recordButton = findViewById(R.id.record);
        recordButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://er.saratov.gov.ru/"));
                startActivity(intent);
            }
        });
    }
}
