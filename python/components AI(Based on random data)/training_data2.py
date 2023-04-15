import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Create a list of appliances
appliances = ['Toaster', 'Refrigerator', 'Washing Machine', 'Dishwasher', 'Microwave', 'Oven']

# Generate random data for each appliance
lifespans = np.random.randint(low=1, high=20, size=len(appliances))
components = [['Heating Element', 'Bread Rack'],
              ['Compressor', 'Fan', 'Thermostat'],
              ['Motor', 'Pump', 'Drum'],
              ['Spray Arm', 'Rack', 'Heating Element'],
              ['Turntable', 'Magnetron', 'Control Panel'],
              ['Heating Element', 'Broiler', 'Burner']]

# Create a Pandas DataFrame from the data
data = {'appliance_name': appliances, 'lifespan': lifespans, 'useful_components': components}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('appliance_dataset.csv', index=False)
