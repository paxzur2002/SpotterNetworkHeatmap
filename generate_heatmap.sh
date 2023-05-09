mkdir tmp/
sh save_current_spotternetwork_db.sh
cat tmp/spotternetwork_db.txt | sh awk_filter.sh > coordinates.csv
cat coordinates.csv | grep -Eo '^[-0-9.]+,[-0-9.]+' > latlon.csv
/usr/local/opt/python@3.10/bin/python3.10 heatmap.py
