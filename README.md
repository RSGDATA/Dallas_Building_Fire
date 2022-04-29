# Dallas_Building_Fire

Sprinkler & Fire Alarm vs % Loss
Time of Fire vs frequency
Fire vs weather
% loss vs battalion
per structure type
# stories vs % loss
% loss vs structure type
Many of these, we can also begin searching for correlation with that magical heatmap chart.  Still probably should demonstrate whether some inputs affect likelihood of a fire.


Data cleaning & prep:

drop columns:
MAPSCO
Census Tract
drop rows:
stories < 100
total_saved > 0
total_value > 1
create columns:
% loss
lat
lon
