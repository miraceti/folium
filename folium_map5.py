
import folium

mapObj = folium.Map(location=[48.8659788,2.0686104], zoom_start=10,
                    tiles='OpenStreetMap')

folium.TileLayer('stamenterrain', attr='stamenterrain').add_to(mapObj)
folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', 
            name='OpenTopoMap',
            attr='OpenTopoMap').add_to(mapObj)

folium.LayerControl().add_to(mapObj)

mapObj.save('map5_output.html')

mapObj

