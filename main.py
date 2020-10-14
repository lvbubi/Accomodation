import folium
import pandas as pd

import accomodationService as service

statistics = service.loadTable()
coordinates = service.loadCoordinates()

mapModel = pd.merge(coordinates, statistics, left_on='id', right_on='id', how='left')

print(mapModel)
#Budapest 47.509113,19.0282913
# Make a data frame with dots to show on the map
data = mapModel


# Make an empty map
m = folium.Map(location=[47.509113, 19.0282913], tiles="OpenStreetMap", zoom_start=7)

# I can add marker one by one on the map
for i in range(0,len(data)):
   folium.Circle(
      location=[data.iloc[i]['longitude'], data.iloc[i]['latitude']],
      popup=data.iloc[i]['county'],
      radius=int(data.iloc[i]['foreign'] / 10),
      color='crimson',
      fill=True,
      fill_color='crimson'
   ).add_to(m)

# Save it as html

m.save('mymap.html')
