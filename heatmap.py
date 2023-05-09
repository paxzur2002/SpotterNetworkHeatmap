import pandas as pd
import folium
from folium import plugins

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('latlon.csv', names=['lat', 'lon'])

# Drop any rows with missing values
df.dropna(inplace=True)

# Create a Folium map centered on the mean of the coordinates
map_heatmap = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=4)

# Add the heatmap layer to the map
heat_data = [[row['lat'], row['lon']] for index, row in df.iterrows()]
plugins.HeatMap(heat_data).add_to(map_heatmap)

# Save the map to an HTML file
map_heatmap.save('spotternetwork_heatmap_current.html')

