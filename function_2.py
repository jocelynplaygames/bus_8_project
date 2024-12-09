# takes nodes and edges as input, returns the edges calculated distances with weights

import math

'def define_weights(coord_pairs: list) -> list:'
weights = []
# Define the coordinates

coord_pairs = [[40.712776, -74.005974, 34.052235, -118.243683], [41.878113, -87.629799, 29.760427, -95.369804]]

radius_miles = 3958.8  # Radius of Earth in miles

for pair in coord_pairs:
    # Extract coordinates for the pair
    lat1, lon1, lat2, lon2 = pair
    # Convert coordinates to radians
    lat1, lon1 = map(math.radians, (lat1, lon1))
    lat2, lon2 = map(math.radians, (lat2, lon2))

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius_miles * c

    # Calculate the weight and append to the list
    weight = distance / 20
    weights.append(round(weight, 2))

print(weights)
'return (weights)'
