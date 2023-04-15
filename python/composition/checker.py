import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


data = pd.read_csv('e-Twaste_data.csv')


X = data.drop('composition', axis=1)
y = data['composition']


ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)

scaler = StandardScaler()
X = scaler.fit_transform(X)


model = LinearRegression()
model.fit(X, y)


product_type = input(
    'Enter the product type (Laptop/Mobile Phone/Tablet/Desktop Computer): ')
weight = float(input('Enter the weight of the device in grams: '))
battery = float(
    input('Enter the battery capacity in milliampere-hours (mAh): '))
screen_size = float(input('Enter the screen size in inches: '))
ram = float(input('Enter the RAM capacity in gigabytes (GB): '))
storage = float(input('Enter the storage capacity in gigabytes (GB): '))


data = pd.DataFrame({
    'product_type': [product_type],
    'weight': [weight],
    'battery': [battery],
    'screen_size': [screen_size],
    'ram': [ram],
    'storage': [storage]
})


data = ct.transform(data)
data = scaler.transform(data)


composition = model.predict(data)


print('The predicted composition of different elements is: ', composition[0])
