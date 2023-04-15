# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import joblib

# Load the dataset
data = pd.read_csv('e-waste-data.csv')

# Select relevant features for the model
features = ['Latitude', 'Longitude', 'Population',
            'GDP', 'Distance to Nearest City']

# Separate input features and target variable
X = data[features]
y = data['Capacity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scale the data to normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the Support Vector Regression (SVR) model
model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
model.fit(X_train, y_train)

# Evaluate the model on the test set
score = model.score(X_test, y_test)
print(f'Model accuracy on test set: {score}')

# Save the model to a file
joblib.dump(model, 'e-waste-model.pkl')
