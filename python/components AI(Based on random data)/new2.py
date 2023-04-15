import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('appliance_dataset.csv')

# Get the user input for the appliance name and lifespan
appliance_name = input("Enter the name of the appliance: ")
lifespan = int(input("Enter the lifespan of the appliance (in years): "))

# Filter the dataframe based on the user input
filtered_df = df[(df['appliance_name'] == appliance_name) & (df['lifespan'] >= lifespan)]

# Check if the filtered dataframe is empty
if filtered_df.empty:
    print("No matching appliance found.")
else:
    # Extract the useful components for the selected appliance
    useful_components = filtered_df.iloc[0]['useful_components']

    # Print the result
    print(f"The useful components of {appliance_name} with a lifespan of at least {lifespan} years are: {useful_components}")
