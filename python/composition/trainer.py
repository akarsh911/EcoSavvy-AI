import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the dataset
data = pd.read_csv('e-waste_data.csv')

# Separate the features and target variable
X = data.drop(['composition'], axis=1)
y = data['composition']

# One-hot encode the categorical variable 'product_type'
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [
                       'product_type'])], remainder='passthrough')
X = ct.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scale the numerical features to have a mean of zero and a standard deviation of one
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Save the trained model
joblib.dump(model, 'ewaste_model.pkl')

# Predict on the test dataset
y_pred = model.predict(X_test_scaled)

# Evaluate the performance of the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error: ', mse)
print('R-squared: ', r2)
