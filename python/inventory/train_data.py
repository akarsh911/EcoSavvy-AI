import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import joblib
data = pd.read_csv('e-waste-data.csv')
features = ['Latitude', 'Longitude', 'Population',
            'GDP', 'Distance to Nearest City']
X = data[features]
y = data['Capacity']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f'Model accuracy on test set: {score}')
joblib.dump(model, 'e-waste-model.pkl')
