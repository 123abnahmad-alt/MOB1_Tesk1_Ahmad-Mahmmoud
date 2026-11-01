package com.example.birthdaycard

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.TextView
import android.widget.LinearLayout

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val layout = LinearLayout(this)
        layout.orientation = LinearLayout.VERTICAL
        layout.gravity = Gravity.CENTER
        layout.setPadding(24, 24, 24, 24)
        layout.setBackgroundColor(Color.rgb(35, 75, 130))

        val text = TextView(this)
        text.text = "Happy Birthday!\n\nWishing you a wonderful day!"
        text.textSize = 26f
        text.setTextColor(Color.WHITE)
        text.gravity = Gravity.CENTER
        layout.addView(text)
        setContentView(layout)
    }
}
