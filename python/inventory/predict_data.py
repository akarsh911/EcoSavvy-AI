import joblib
from sklearn.preprocessing import StandardScaler
model = joblib.load('e-waste-model.pkl')
new_location = [[28.7041, 77.1025, 21500000, 300000, 50]]
scaler = StandardScaler()
new_location_scaled = scaler.fit_transform(new_location)
predicted_capacity = model.predict(new_location_scaled)[0]
print(f'Predicted capacity for new location: {predicted_capacity}')
