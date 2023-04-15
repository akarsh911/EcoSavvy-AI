import numpy as np
import pandas as pd
num_samples = 5000
lat_range = (8.4, 37.6)
lon_range = (68.1, 97.4)
pop_range = (100000, 20000000)
gdp_range = (1000, 100000)
dist_range = (1, 100)
latitude = np.random.uniform(lat_range[0], lat_range[1], size=num_samples)
longitude = np.random.uniform(lon_range[0], lon_range[1], size=num_samples)
population = np.random.uniform(pop_range[0], pop_range[1], size=num_samples)
gdp = np.random.uniform(gdp_range[0], gdp_range[1], size=num_samples)
distance = np.random.uniform(dist_range[0], dist_range[1], size=num_samples)
capacity = 0.5*latitude + 0.3*longitude + 1.5 * \
    population/1000 + 0.7*gdp/1000 + 2*distance
data = pd.DataFrame({'Latitude': latitude, 'Longitude': longitude, 'Population': population,
                    'GDP': gdp, 'Distance to Nearest City': distance, 'Capacity': capacity})
data.to_csv('e-waste-data.csv', index=False)
