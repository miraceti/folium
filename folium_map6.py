
import folium

mapObj = folium.Map(location=[48.8659788,2.0686104], zoom_start=10,
                    tiles='OpenStreetMap')

layer1 = folium.GeoJson(
        data = (open("states_india.geojson", 'r').read()),
        name = "India"
)

layer1.add_to(mapObj)

mapObj.save("map6_output.html")

