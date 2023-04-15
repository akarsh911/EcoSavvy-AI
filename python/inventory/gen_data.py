import pandas as pd
import numpy as np

# Define the parameters and their distributions
n_samples = 1000
pop_density_mean = 1000
pop_density_std = 500
gdp_mean = 5000
gdp_std = 2000
urbanization_mean = 0.5
urbanization_std = 0.2
e_waste_gen_mean = 0.1
e_waste_gen_std = 0.05
capacity_mean = 1000
capacity_std = 500

# Generate the data
pop_density = np.random.normal(loc=pop_density_mean, scale=pop_density_std, size=n_samples)
gdp = np.random.normal(loc=gdp_mean, scale=gdp_std, size=n_samples)
urbanization = np.random.normal(loc=urbanization_mean, scale=urbanization_std, size=n_samples)
e_waste_gen = np.random.normal(loc=e_waste_gen_mean, scale=e_waste_gen_std, size=n_samples)
capacity = np.random.normal(loc=capacity_mean, scale=capacity_std, size=n_samples)

# Combine the data into a DataFrame
data = pd.DataFrame({'Location': [f'Location {i+1}' for i in range(n_samples)],
                     'Population density': pop_density,
                     'GDP': gdp,
                     'Urbanization rate': urbanization,
                     'E-waste generation rate': e_waste_gen,
                     'Inventory capacity': capacity})

# Save the data as a CSV file
data.to_csv('e-waste-data.csv', index=False)
