# This code snippet does not run on its own.  This is intended to be copy / pasted into Jupyter Notebook.
from config import gkey

lats = []
lngs = []
# geocoordinates
base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
for row in clean_fire_df:
    address = clean_fire_df['ADDRESS'] + ",Dallas,TX"

    # set up a parameters dictionary
    params = {
        "address": address,
        "key": gkey
    }
    response = requests.get(base_url, params=params)
    geo_data = response.json()
    # Extract latitude and longitude
    lat = geo_data["results"][0]["geometry"]["location"]["lat"]
    lng = geo_data["results"][0]["geometry"]["location"]["lng"]

clean_fire_df['Lat'] = lats
clean_fire_df['Lng'] = lngs

