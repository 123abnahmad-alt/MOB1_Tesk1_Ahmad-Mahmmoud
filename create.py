from pathlib import Path

apps = {
"Article": ("com.example.article", "Article", "Read interesting articles"),
"BirthdayCard": ("com.example.birthdaycard", "Happy Birthday!", "Wishing you a wonderful day!"),
"BusinessCard": ("com.example.businesscard", "Ahmad Mahmoud", "Business Card"),
"Quadrant": ("com.example.quadrant", "Quadrant", "Four sections"),
"TaskDone": ("com.example.taskdone", "Task Done!", "All tasks completed!")
}

for name, (package, title, description) in apps.items():
    root = Path(name)
    java = root / "app/src/main/java" / Path(*package.split("."))
    java.mkdir(parents=True, exist_ok=True)

    (root / "settings.gradle.kts").write_text(
        'pluginManagement { repositories { google(); mavenCentral(); gradlePluginPortal() } }\n'
        'dependencyResolutionManagement { repositories { google(); mavenCentral() } }\n'
        f'rootProject.name = "{name}"\ninclude(":app")\n'
    )

    (root / "build.gradle.kts").write_text(
        'plugins {\n'
        'id("com.android.application") version "8.6.1" apply false\n'
        'id("org.jetbrains.kotlin.android") version "2.0.21" apply false\n}\n'
    )

    (root / "gradle.properties").write_text(
        "android.useAndroidX=true\n"
    )

    (root / "app/build.gradle.kts").write_text(
        'plugins {\n'
        'id("com.android.application")\n'
        'id("org.jetbrains.kotlin.android")\n'
        '}\n'
        'android {\n'
        f'namespace = "{package}"\n'
        'compileSdk = 35\n'
        'defaultConfig {\n'
        f'applicationId = "{package}"\n'
        'minSdk = 23\n'
        'targetSdk = 35\n'
        'versionCode = 1\n'
        'versionName = "1.0"\n'
        '}\n'
        'compileOptions {\n'
        'sourceCompatibility = JavaVersion.VERSION_17\n'
        'targetCompatibility = JavaVersion.VERSION_17\n'
        '}\n'
        'kotlinOptions { jvmTarget = "17" }\n'
        '}\n'
    )

    (root / "app/src/main/AndroidManifest.xml").write_text(
        '<manifest xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '<application android:theme="@android:style/Theme.Material.Light.NoActionBar" '
        f'android:label="{title}">\n'
        '<activity android:name=".MainActivity" android:exported="true">\n'
        '<intent-filter><action android:name="android.intent.action.MAIN"/>'
        '<category android:name="android.intent.category.LAUNCHER"/></intent-filter>\n'
        '</activity></application></manifest>\n'
    )

    kotlin = f'''package {package}

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.TextView
import android.widget.LinearLayout

class MainActivity : Activity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        val layout = LinearLayout(this)
        layout.orientation = LinearLayout.VERTICAL
        layout.gravity = Gravity.CENTER
        layout.setPadding(24, 24, 24, 24)
        layout.setBackgroundColor(Color.rgb(35, 75, 130))

        val text = TextView(this)
        text.text = "{title}\\n\\n{description}"
        text.textSize = 26f
        text.setTextColor(Color.WHITE)
        text.gravity = Gravity.CENTER
        layout.addView(text)
        setContentView(layout)
    }}
}}
'''
    (java / "MainActivity.kt").write_text(kotlin)
    (root / "README.md").write_text(f"# {name}\nAndroid Kotlin project\n")

print("SUCCESS: Created all five Android projects!")
