
import folium

mapObj = folium.Map(location=[48.8659788,2.0686104], zoom_start=10,
                    tiles='OpenStreetMap')

          
folium.Circle(radius=5000, 
                location=[48.8659788,2.0686104],
                color='red',
                weight=10,
                fill=True,
                fill_color='blue',
                fill_opacity=0.8,
                stroke=False,
                popup=folium.Popup("""<h2>This is a <b>popup</b></h2><br>
                This a <b>new line</b><br/>
                <img src="https://www.w3schools.com/html/pic_trulli.jpg" alt="Trulli" style="max-width:100%;max-height:100%">""", max_width=500),
                ).add_to(mapObj)

folium.Circle(radius=1000, 
                location=[48.8038984,2.0985952],
                color='red',
                weight=10,
                fill=True,
                tooltip="This a circle",
                popup=folium.Popup("This is a popup", max_width=500),
                # fill_color='blue',
                # fill_opacity=0.8,
                # stroke=True,
                ).add_to(mapObj)


mapObj.save("map8_output.html")

