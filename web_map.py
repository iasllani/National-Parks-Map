import folium
import pandas as pd

# read the volcano.txt file (even though the
# function is 'read_csv') and store as 'df1' variable,
# then read national_parks.csv and save as 'df2'
df1 = pd.read_csv("volcano.txt")
df2 = pd.read_csv("us_national_parks.txt")

# correct apostrophes that mess with separation
df1['NAME'] = df1['NAME'].str.replace("'", "&#39;")
df2['Name'] = df2['Name'].str.replace("'", "&#39;")

avg_lat = (df1['LAT'].mean() + df2['Latitude'].mean()) / 2
avg_lon = (df1['LON'].mean() + df2['Longitude'].mean()) / 2
latmean = avg_lat
lonmean = avg_lon

map = folium.Map(location=[latmean, lonmean], zoom_start=4, tiles='Stamen Terrain')


# function that determines marker color based on elevation
def color(elevation):
    if elevation in range(0, 1000):
        col = 'green'
    elif elevation in range(1001, 1999):
        col = 'orange'
    elif elevation in range(2000, 2999):
        col = 'blue'
    else:
        col = 'red'
    return col


# create a for loop that will go through each volcano and mark it. We zip it due to the different iterators we want
for lat1, lon1, name1, elev in zip(df1['LAT'], df1['LON'], df1['NAME'], df1['ELEV']):
    folium.Marker(location=[lat1, lon1], popup=name1, icon=folium.Icon(color=color(elev), icon_color='white', icon='cloud')).add_to(map)

for lat2, lon2, name2 in zip(df2['Latitude'], df2['Longitude'], df2['Name']):
    folium.Marker(location=[lat2, lon2], popup=name2, icon=folium.Icon(color='gray', icon='info-sign')).add_to(map)

print(map.save('mark_map.html'))

