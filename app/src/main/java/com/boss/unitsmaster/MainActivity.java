package com.boss.unitsmaster;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText etCny = findViewById(R.id.et_cny);
        Button btnConvert = findViewById(R.id.btn_convert);
        TextView tvResult = findViewById(R.id.tv_result);

        btnConvert.setOnClickListener(v -> {
            String input = etCny.getText().toString();
            if (input.isEmpty()) return;

            double cny = Double.parseDouble(input);
            // 简单写死固定汇率演示逻辑
            double usd = cny * 0.14; 
            double jpy = cny * 21.0;
            double eur = cny * 0.13;

            String result = getString(R.string.res_usd) + String.format("%.2f", usd) + "\n"
                          + getString(R.string.res_jpy) + String.format("%.2f", jpy) + "\n"
                          + getString(R.string.res_eur) + String.format("%.2f", eur);
            
            tvResult.setText(result);
        });
    }
}
