
import folium

mapObj = folium.Map(location=[48.8659788,2.0686104], zoom_start=10,
                    tiles='OpenStreetMap')

shapesLayer = folium.FeatureGroup(name="shapes").add_to(mapObj)

circlesData =[
    [25, 74, 80000],
    [22, 79, 60000],
    [26, 82, 90000]
]

for d in circlesData:
    folium.Circle(radius=d[2], 
                location=[d[0],d[1]],
                color='red',
                weight=10,
                fill=True,
                fill_color='blue',
                fill_opacity=0.2,
                stroke=False,
                popup=folium.Popup("""<h2>This is a <b>popup</b></h2><br>
                This a <b>new line</b><br/>
                <img src="https://www.w3schools.com/html/pic_trulli.jpg" alt="Trulli" style="max-width:100%;max-height:100%">""", max_width=500),
                ).add_to(shapesLayer)

folium.LayerControl().add_to(mapObj)

mapObj.save("map9_output.html")

