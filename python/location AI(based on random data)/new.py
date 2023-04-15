import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor


data = pd.read_csv('e-waste_data_kanishk.csv')


X = data.drop(['State', 'E-Waste (MT)'], axis=1)
y = data['E-Waste (MT)']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


model = RandomForestRegressor()
model.fit(X_train, y_train)


print("Training score:", model.score(X_train, y_train))
print("Testing score:", model.score(X_test, y_test))


states = data['State']
predictions = model.predict(X_scaled)
results = pd.DataFrame({'State': states, 'E-Waste (MT)': predictions})
top_10_states = results.nlargest(10, 'E-Waste (MT)')


print(top_10_states)
