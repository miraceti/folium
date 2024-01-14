
import folium

mapObj = folium.Map(location=[48.8659788,2.0686104], zoom_start=10,
                    tiles='OpenStreetMap')

bordersStyle = {
    'color' : 'green',
    'weight' : 2,
    'fillColor': 'blue',
    'fillOpacity' : 0.3
}

bordersStyle2 = {
    'color' : 'red',
    'weight' : 2,
    'fillColor': 'yellow',
    'fillOpacity' : 0.3
}

folium.GeoJson("states_india.geojson", 
                name = "India", 
                style_function= lambda x:bordersStyle ).add_to(mapObj)

folium.GeoJson("srilanka.geojson", 
                name = "Srilanka", 
                style_function= lambda x:bordersStyle2 ).add_to(mapObj)     

# import requests
# folium.GeoJson(requestw.get("https://github.com/nagasudhirpulla/taming_python/raw/master/blog/skills/assets/data/states_india.geojson").text, 
#         name = "Srilanka", 
#         style_function= lambda x:bordersStyle2 ).add_to(mapObj)               

folium.LayerControl().add_to(mapObj)                       

mapObj.save("map7_output.html")

