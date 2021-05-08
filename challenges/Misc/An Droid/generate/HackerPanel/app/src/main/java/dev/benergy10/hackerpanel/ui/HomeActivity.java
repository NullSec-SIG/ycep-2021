package dev.benergy10.hackerpanel.ui;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import dev.benergy10.hackerpanel.R;

public class HomeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        String userName = getIntent().getStringExtra("username");
        ((TextView) findViewById(R.id.textViewName)).setText(userName);
    }
}