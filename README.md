# Boston House Price Prediction Using Flask and Flutter

## Overview
This project is aimed at developing a machine learning model to predict house prices in the Boston area. The model utilizes a dataset containing various features such as crime rate, nitric oxides concentration, and average number of rooms per dwelling to make accurate predictions. Additionally, the model is hosted using Flask, and the predictions are displayed through a Flutter application.

## Features
- Utilizes the Boston Housing dataset for training and testing.
- Implements a machine learning model to predict house prices based on various input features.
- Hosts the model using Flask, allowing for easy access through API endpoints.
- Utilizes a Flutter application to display the predicted house prices to users.

## Requirements
- Python 3.x
- Flask
- scikit-learn
- Flutter SDK

**Dataset Download Links:**
- [boston_house_prices (1).csv](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/boston_house_prices%20(1).csv)

**Dataset Created By Me After Analysis Download Links:**
- [boston_house_prices (1).csv](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/Load_boston_dataset.csv)

## How to Use
- After completing the installation steps, you can use the project in the following way:
1. Train the machine learning model using the provided Jupyter notebook [House_price_prediction.ipynb](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/House_price_prediction.ipynb).
2. Serialize the trained model into a pickle file named [model.pkl](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/model.pkl).
3. Run the Flask application using the script [ml_and_flask_deploy.py](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/ml_and_flask_deploy.py) to host the model on localhost.
4. Finally, launch the Flutter application from the [Predict-price-app](https://github.com/Skull-7/Predict-price-app) repository to interact with the model and view predictions.

## Testing API Responses with Postman
- You can use Postman to test the API responses after hosting the Flask application.

## Note
- To check my model or python notebook file you can check [House_price_prediction.ipynb](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/House_price_prediction.ipynb)
- After creating my model i have stored it in pkl file using pickle module and the file name is [model.pkl](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/model.pkl)
- To check the flask code click on [ml_and_flask_deploy.py](https://github.com/Skull-7/Machine-Learning-and-Flutter/blob/main/ml_and_flask_deploy.py)
- To check my app code you can visit another repository [Predict-price-app](https://github.com/Skull-7/Predict-price-app) 
