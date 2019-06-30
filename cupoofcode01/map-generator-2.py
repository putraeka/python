import folium

map3 = folium.Map(location = [-7.840243, 110.408333], zoom_start=15, tiles='Stamen Terrain')

# we want to add some markers to our map

# Menambahkan marker icon cloud dan popup "Iam so lost"
folium.Marker(location = [-7.840243, 110.408333], popup = 'Iam so lost', icon = folium.Icon(icon='cloud')).add_to(map3)

# Menambahkan marker icon green dan Popup But "I can see you"
folium.Marker(location = [-7.840240, 110.408335], popup = 'But I can see you', icon = folium.Icon(color='green')).add_to(map3)

print(map3.save('test3.html'))