# takes nodes and edges as input, returns the edges calculated distances with weights

import math

# Define the coordinates
lat_lon_1 = [47.617756, -122.334014]  # Point 1 (latitude, longitude)
lat_lon_2 = [47.618493, -122.334320]  # Point 2 (latitude, longitude)

# Convert latitude and longitude to radians
lat_lon_1[0], lat_lon_1[1], lat_lon_2[0], lat_lon_2[1] = map(math.radians,
                                                              [lat_lon_1[0], lat_lon_1[1],
                                                               lat_lon_2[0], lat_lon_2[1]])

# Haversine formula
dlat = lat_lon_2[0] - lat_lon_1[0]
dlon = lat_lon_2[1] - lat_lon_1[1]
a = math.sin(dlat / 2)**2 + math.cos(lat_lon_1[0]) * math.cos(lat_lon_2[0]) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Radius of Earth in miles
radius_miles = 3958.8
distance = radius_miles * c

# Output the result
print(f"Distance: {distance:.4f} miles")
