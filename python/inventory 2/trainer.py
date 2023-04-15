import random
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from joblib import dump


states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 
          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 
          'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 
          'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 
          'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

populations = [random.randint(1000000, 200000000) for i in range(len(states))]
gdps = [random.randint(100000, 10000000) for i in range(len(states))]
urbanizations = [random.uniform(10, 100) for i in range(len(states))]
high_ewaste_generators = [random.randint(0, 1) for i in range(len(states))]


df = pd.DataFrame({'State': states,
                   'Population': populations,
                   'GDP': gdps,
                   'Urbanization': urbanizations,
                   'High_EWaste_Generator': high_ewaste_generators})

# Save to CSV
df.to_csv('e-waste_data.csv', index=False)

# Load data
data = pd.read_csv('e-waste_data.csv')

# Prepare data
X = data[['Population', 'GDP', 'Urbanization']]
y = data['High_EWaste_Generator']

# Preprocess data
X = (X - X.mean()) / X.std() # Normalize data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)


filename = 'logistic_regression_model.joblib'
dump(model, filename)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print('Accuracy: {:.2f}'.format(accuracy))
print('Precision: {:.2f}'.format(precision))
print('Recall: {:.2f}'.format(recall))
print('F1 Score: {:.2f}'.format(f1))
