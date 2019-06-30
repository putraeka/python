# Tutorial dari https://youtu.be/xKAtjW-1i9E

# Folium adalah library yang berhubungan dengan map
import folium

# Print semua fungsi dan method dari folium
# print(dir(folium))
map = folium.Map(location=[-7.840243, 110.408333], zoom_start=7)

# need html file out of this object - to create a map
# Look in the map method directory to see all the methods we can apply to MAP

# print(dir(folium.map))

# Export map ke format html
print(map.save('test.html'))

# go look under your files for the surprise
# right click on your html file and open in browser

# change the zoom to 15 and and add tiles = 'Stamen Terrain' and recreate the html file

map = folium.Map(location=[-7.840243, 110.408333], zoom_start=15, tiles='Stamen Terrain')
print(map.save('test2.html'))