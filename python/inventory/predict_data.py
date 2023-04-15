# Import necessary libraries
import joblib
from sklearn.preprocessing import StandardScaler
# Load the saved model
model = joblib.load('e-waste-model.pkl')

# Create a new input feature for a new location
new_location = [[28.7041, 77.1025, 21500000, 300000, 50]]

# Scale the input feature using the same StandardScaler object used during training
scaler = StandardScaler()
new_location_scaled = scaler.fit_transform(new_location)

# Use the model to make a prediction for the required capacity
predicted_capacity = model.predict(new_location_scaled)[0]

# Print the predicted capacity
print(f'Predicted capacity for new location: {predicted_capacity}')
