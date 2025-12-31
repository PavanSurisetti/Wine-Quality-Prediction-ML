import pandas as p  # for importing and using of datasets
from sklearn.model_selection import train_test_split  # for splitting the data
from sklearn.linear_model import LinearRegression  # because continuous values
from sklearn.metrics import mean_absolute_error, r2_score  # for evaluation
from sklearn.preprocessing import StandardScaler  # for feature scaling
import joblib  # for saving and loading models

# Load the dataset
ds = p.read_csv('WineQT.csv')

# Splitting features and target
input = ds.iloc[:, :11]  # to extract all the columns except the quality and id [id is a unique tag for each wine]
output = ds['quality']  # target label

# Splitting the dataset into train and test sets
x_train, x_test, y_train, y_test = train_test_split(input, output, random_state=42, test_size=0.2)

# Feature scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Creating the Linear Regression model
model = LinearRegression()

# Training the model
model.fit(x_train_scaled, y_train)

# Making predictions
y_pred = model.predict(x_test_scaled)

# Evaluating the model
mae, r2 = mean_absolute_error(y_test, y_pred), r2_score(y_test, y_pred)

# Save the trained model and scaler using joblib
joblib.dump(model, 'wine_quality_model.pkl')  # saved model
joblib.dump(scaler, 'scaler.pkl')  # saved scaler

# Preparing to give your own input values for checking the wine quality
col_names = input.columns  # get column names to avoid warnings

# Sample wine 1
w1 = [[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]]
w1 = p.DataFrame(w1, columns=col_names)
w1_scaled = scaler.transform(w1)  # scale the input

# Sample wine 2
w2 = [[6.8, 0.28, 0.34, 2.4, 0.065, 25.0, 100.0, 0.9956, 3.20, 0.68, 10.5]]
w2 = p.DataFrame(w2, columns=col_names)
w2_scaled = scaler.transform(w2)  # scale the input

# Making predictions for your own samples
print(f'Wine Sample1: {model.predict(w1_scaled)[0]}')
print(f'Wine Sample2: {model.predict(w2_scaled)[0]}')

# Printing evaluation metrics
print(f'MAE: {mae}')
print(f'R2: {r2}')

# Example: Loading the saved model and scaler (optional demonstration)
# loaded_model = joblib.load('wine_quality_model.pkl')
# loaded_scaler = joblib.load('scaler.pkl')
# print(loaded_model.predict(loaded_scaler.transform(w1))[0])
