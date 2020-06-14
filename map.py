import folium
import pandas



map = folium.Map(zoom_start= 7, tiles = "CartoDB dark_matter")
fg = folium.FeatureGroup(name = "My Map")

data = pandas.read_csv("confirmcase.csv")


print(data)
lat = list(data["Lat"])
lon = list(data["Long"])
no= list(data["6/13/20"])

for lat , lon ,no in zip(lat , lon, no):
    fg.add_child(folium.Marker(location=[lat, lon] , popup= no, icon = folium.Icon(color= 'red')))





map.add_child(fg)
map.save("Map1.html")