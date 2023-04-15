import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('e-waste-data.csv')

# Preprocess the data
data.dropna(inplace=True)
data = pd.get_dummies(data, columns=['product_type'])

# Feature engineering
X = data.drop(['metal_composition'], axis=1)
y_metal = data['metal_composition'].str.split(',', expand=True).astype(float)
y_element = data['element_composition'].str.split(
    ',', expand=True).astype(float)

# Concatenate the metal and element compositions into a single target variable
y = pd.concat([y_metal, y_element], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
score = model.score(X_test, y_test)
print('Model Score:', score)

# Predict the metal and element composition of a new e-waste
product_type = 'laptop'
X_new = pd.DataFrame({'product_type_laptop': 1, 'product_type_mobile': 0,
                     'age': 2, 'element_1': 0.1, 'element_2': 0.2, 'element_3': 0.3}, index=[0])
y_new = model.predict(X_new)
print('Predicted metal and element composition:', y_new)
