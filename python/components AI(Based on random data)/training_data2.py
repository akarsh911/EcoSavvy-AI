import numpy as np
import pandas as pd


np.random.seed(42)


appliances = ['Toaster', 'Refrigerator', 'Washing Machine', 'Dishwasher', 'Microwave', 'Oven']


lifespans = np.random.randint(low=1, high=20, size=len(appliances))
components = [['Heating Element', 'Bread Rack'],
              ['Compressor', 'Fan', 'Thermostat'],
              ['Motor', 'Pump', 'Drum'],
              ['Spray Arm', 'Rack', 'Heating Element'],
              ['Turntable', 'Magnetron', 'Control Panel'],
              ['Heating Element', 'Broiler', 'Burner']]


data = {'appliance_name': appliances, 'lifespan': lifespans, 'useful_components': components}
df = pd.DataFrame(data)


df.to_csv('appliance_dataset.csv', index=False)
