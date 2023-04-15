# Step 1: Collecting the data
import pandas as pd
data = pd.read_csv('e-waste_data.csv')

# Step 2: Preprocessing the data

# drop irrelevant columns
data = data.drop(['S.No.', 'State/UT'], axis=1)
# remove missing values
data = data.dropna()
# normalize the data
data = (data - data.mean()) / data.std()

# Step 3: Building the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Step 4: Training the model
X = data.drop(['E-waste generated (Tonnes)'], axis=1)
y = data['E-waste generated (Tonnes)']
model.fit(X, y)

# Step 5: Testing the model
# split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# evaluate the model
from sklearn.metrics import r2_score
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
print(f"Model accuracy: {score}")

# Step 6: Making predictions
# predict e-waste generation for a new state
new_state = pd.DataFrame({'Population': [50000000], 'GDP (in Crore)': [10000]})
predicted_e_waste = model.predict(new_state)
print(f"Predicted e-waste generation: {predicted_e_waste}")
