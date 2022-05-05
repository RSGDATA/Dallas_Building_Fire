import math

# Magical mathematical formula:
# https://www.adamsmith.haus/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python
# Adapted to use as callable function that can returns kilometers by default or miles by option
def haversine(lat1, lon1, lat2, lon2, unit='km'):
    # radius of the Earth in km
    R = 6373.0

    # coordinates
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # change in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1


    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    #Haversine formula

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    
    if unit=='mi':
        distance = distance * 0.621371
    return distance