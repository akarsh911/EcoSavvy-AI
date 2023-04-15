import pandas as pd
import random


states = []
population = []
urban_population = []
gdp = []
literacy_rate = []
internet_penetration = []
e_waste = []

for i in range(30):
    states.append("State_" + str(i+1))
    population.append(random.randint(1000000, 50000000))
    urban_population.append(random.uniform(10, 90))
    gdp.append(random.uniform(500, 50000))
    literacy_rate.append(random.uniform(50, 100))
    internet_penetration.append(random.uniform(10, 90))
    e_waste.append(random.uniform(1000, 50000))


data = pd.DataFrame({
    'State': states,
    'Population': population,
    'Urban Population': urban_population,
    'GDP': gdp,
    'Literacy Rate': literacy_rate,
    'Internet Penetration': internet_penetration,
    'E-Waste (MT)': e_waste
})


data.to_csv('e-waste_data_kanishk.csv', index=False)
