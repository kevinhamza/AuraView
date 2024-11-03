package com.example.arsocialglasses

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.ar.sceneform.AnchorNode
import com.google.ar.sceneform.rendering.ViewRenderable
import com.google.ar.sceneform.ux.ArFragment
import okhttp3.*
import org.json.JSONObject
import java.io.IOException

class MainActivity : AppCompatActivity() {

    private lateinit var arFragment: ArFragment

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        arFragment = supportFragmentManager.findFragmentById(R.id.ux_fragment) as ArFragment
        arFragment.setOnTapArPlaneListener { hitResult, _, _ ->
            val anchor = hitResult.createAnchor()
            fetchUserData("John Doe", anchor)  // Example name, replace with detected face name
        }
    }

    private fun fetchUserData(name: String, anchor: Anchor) {
        val url = "http://YOUR_SERVER_IP:5000/get_user_info?name=$name"
        val client = OkHttpClient()

        val request = Request.Builder().url(url).build()
        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) { e.printStackTrace() }

            override fun onResponse(call: Call, response: Response) {
                val data = JSONObject(response.body?.string())
                runOnUiThread {
                    val linkedin = data.optJSONObject("LinkedIn")?.getString("name") ?: "N/A"
                    val twitter = data.optJSONObject("Twitter")?.getString("username") ?: "N/A"
                    val instagram = data.optJSONObject("Instagram")?.getString("username") ?: "N/A"
                    createLabel(anchor, name, linkedin, twitter, instagram)
                }
            }
        })
    }

    private fun createLabel(anchor: Anchor, name: String, linkedin: String, twitter: String, instagram: String) {
        ViewRenderable.builder()
            .setView(this, R.layout.user_info_layout)
            .build()
            .thenAccept { renderable ->
                val anchorNode = AnchorNode(anchor)
                anchorNode.renderable = renderable

                val nameText = renderable.view.findViewById<TextView>(R.id.nameText)
                val linkedinText = renderable.view.findViewById<TextView>(R.id.linkedinText)
                val twitterText = renderable.view.findViewById<TextView>(R.id.twitterText)
                val instagramText = renderable.view.findViewById<TextView>(R.id.instagramText)

                nameText.text = name
                linkedinText.text = "LinkedIn: $linkedin"
                twitterText.text = "Twitter: $twitter"
                instagramText.text = "Instagram: $instagram"

                arFragment.arSceneView.scene.addChild(anchorNode)
            }
    }
}
