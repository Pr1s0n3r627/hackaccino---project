import requests
import numpy as np
import torch
from transformers import BertModel, BertTokenizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
bert_model = BertModel.from_pretrained(model_name)

# Weatherstack API parameters
api_key = "6f9c6496403400f57c4fded4f46cad0c"  # Replace with your Weatherstack API key
location = "Delhi"  # Replace with the location for which you want to fetch weather data
area = 1
# Fetch weather data from Weatherstack API
weather_api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}&forecast_days=180"
response = requests.get(weather_api_url)
weather_data = response.json()

# Dummy dataset (replace with your own dataset)
# Each sample consists of a textual description and corresponding yield per acre
dataset = [
    {"text": "Good weather conditions, well-drained soil.", "yield": 50},
    {"text": "Heavy rainfall last month, clay soil.", "yield": 30},
    # Add more samples as needed
]

# Process textual descriptions using BERT and collect embeddings
embeddings = []
for sample in dataset:
    text = sample["text"]
    encoded_input = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        output = bert_model(**encoded_input)
    # Assuming you want to use the embeddings of the [CLS] token
    cls_embedding = output.last_hidden_state.mean(dim=1).squeeze().numpy()
    embeddings.append(cls_embedding)

# Extract yield in pounds per acre from the dataset
y = np.array([sample["yield"] for sample in dataset])

# Extract weather features from Weatherstack API response
weather_features = [
    weather_data["current"]["temperature"],
    weather_data["current"]["precip"],
    weather_data["current"]["humidity"],
    weather_data["current"]["cloudcover"],
    weather_data["current"]["wind_speed"],  # Corrected to "wind_speed"
    # Add more weather features as needed
]

# Convert weather features to numpy array
weather_features_array = np.array(weather_features).reshape(1, -1)

# Duplicate weather features to match the number of samples
weather_features_array = np.tile(weather_features_array, (len(dataset), 1))

# Combine BERT embeddings and weather features
X = np.concatenate([np.array(embeddings), weather_features_array], axis=1)

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = regression_model.predict(X_val)

# Calculate evaluation metrics
mae = mean_absolute_error(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)
rmse = np.sqrt(mse)
'''
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
'''
# Predict yields per acre for the validation set
predicted_yield = regression_model.predict(X_val)
print("Predicted yields:", predicted_yield)
