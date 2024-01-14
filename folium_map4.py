# %%
import folium

mapObj = folium.Map(location=[48.8659788,2.0686104], zoom_start=10)


folium.LayerControl().add_to(mapObj)

mapObj.save('map3_output.html')

mapObj

# %%
