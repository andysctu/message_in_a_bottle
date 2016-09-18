package com.example.andy.messageinabottle;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.StrictMode;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import java.io.IOException;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private EditText mMessageEditText;
    private Button mMessageSubmitButton;

    private String serverUrl = "http://b3397fac.ngrok.io";

    private OkHttpClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        client = new OkHttpClient();
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        mMessageEditText = (EditText) findViewById(R.id.message_edit_text);
        mMessageSubmitButton = (Button) findViewById(R.id.message_submit_button);

        mMessageSubmitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View mMessageSubmitButton) {
                sendMessage();
            }
        });
    }


    public void sendMessage() {
    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        // Add a marker in Sydney and move the camera
//        LatLng e5 = new LatLng(43.473010, -80.540047);
        LatLng e5 = new LatLng(43.6532, 79.3832);
        mMap.addMarker(new MarkerOptions().position(e5).title("We're Hacking the North"));
//        mMap.moveCamera(CameraUpdateFactory.newLatLng(e5));

        try {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                    .permitAll().build();
            StrictMode.setThreadPolicy(policy);
            System.out.println(getMessages(serverUrl));
        } catch (IOException e) {
            System.out.println(e);
        }

        enableMyLocation();
    }

    /**
     * Enables the My Location layer if the fine location permission has been granted.
     */
    private void enableMyLocation() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
            mMap.setMyLocationEnabled(true);
            mMap.getUiSettings().setMyLocationButtonEnabled(true);
        } else {
            System.out.println("Error need location access");
        }
    }

    private String getMessages(String url) throws IOException {
        Request request = new Request.Builder()
                .url(url)
                .build();

        Response response = client.newCall(request).execute();
        return response.body().string();
    }
}
