import pandas as pd


df = pd.read_csv('appliance_dataset.csv')


appliance_name = input("Enter the name of the appliance: ")
lifespan = int(input("Enter the age of the appliance (in years): "))


filtered_df = df[(df['appliance_name'] == appliance_name) & (df['lifespan'] >= lifespan)]


if filtered_df.empty:
    print("No matching appliance found.")
else:
    useful_components = filtered_df.iloc[0]['useful_components']

    print(f"The useful components of {appliance_name} with a lifespan of at least {lifespan} years are: {useful_components}")
