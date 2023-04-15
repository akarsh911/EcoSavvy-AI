import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the training data
data = pd.read_csv('e-Twaste_data.csv')

# Split the data into input features (X) and target variable (y)
X = data.drop('composition', axis=1)
y = data['composition']

# Preprocess the input features
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Take input from the user
product_type = input(
    'Enter the product type (Laptop/Mobile Phone/Tablet/Desktop Computer): ')
weight = float(input('Enter the weight of the device in grams: '))
battery = float(
    input('Enter the battery capacity in milliampere-hours (mAh): '))
screen_size = float(input('Enter the screen size in inches: '))
ram = float(input('Enter the RAM capacity in gigabytes (GB): '))
storage = float(input('Enter the storage capacity in gigabytes (GB): '))

# Create a DataFrame with the input values
data = pd.DataFrame({
    'product_type': [product_type],
    'weight': [weight],
    'battery': [battery],
    'screen_size': [screen_size],
    'ram': [ram],
    'storage': [storage]
})

# Preprocess the input data
data = ct.transform(data)
data = scaler.transform(data)

# Predict the composition of different elements
composition = model.predict(data)

# Print the results
print('The predicted composition of different elements is: ', composition[0])
