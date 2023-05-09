# SpotterNetworkHeatmap
A tool to make a heatmap of all the spotter network dots. Generates a HTML file that you can open in your browser.

## Requirements
To run this script, you need to have Python 3.10 installed on your computer. You also need the following packages:
```
pandas
folium
```
You can install these packages using the following commands:

```
pip install pandas
pip install folium
```

## Usage
Download or clone this repository to your local machine.

```
git clone https://github.com/paxzur2002/SpotterNetworkHeatmap
```

Go into this repository/folder on your local machine.

```
cd SpotterNetworkHeatmap/
```

Run the script by typing the following command:

```
sh ./generate_heatmap.sh
```
The script will generate a heatmap of the coordinates.csv file that was downloaded by save_current_spotternetwork_db.sh, filtered by awk_filter.sh, and plotted by heatmap.py to be then saved it to an HTML file named "spotternetwork_heatmap_current.html"!

### Just navigate to the folder of this repository on your drive and open up the html file to view the heatmap!
