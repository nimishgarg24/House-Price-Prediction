# House-Price-Prediction
<br>

It is a machine learning model which predicts the house prices in calfornia .The dataset used in this model is California housing dataset which is present in sklearn library.
<br>
<br>
<br>
<br>
PROJECT WORKFLOW:-
<br>
<br>
1. Data Preprocessing & Feature Engineering<br>
Dataset: The California Housing dataset was used.
Steps Taken:<br>
Loaded the dataset and converted it into a Pandas DataFrame.<br>
Checked for missing values and handled them (dropped NaN values).
Split data into features (X) and target (y).<br>
Performed train-test split (80-20%) to separate training and testing sets.
<br>
<br>
2. Model Selection & Optimization<br>
Model Used: RandomForestRegressor<br>
Hyperparameter Optimization: Used RandomizedSearchCV to find the best combination of:<br>
n_estimators: Number of trees in the forest.<br>
max_depth: Maximum depth of the tree.<br>
min_samples_split: Minimum samples required to split a node.<br>
min_samples_leaf: Minimum samples required at a leaf node.<br>
Best Model: The best-performing model was selected and saved using joblib.
<br>
<br>
3. Deployment Strategy<br>
Framework: FastAPI was used for deploying the model as a REST API.
Steps:<br>
Created a FastAPI application (app.py).<br>
Defined API endpoint (/predict) to receive house features as JSON input.<br>
Loaded the trained model (house_price_model.pkl).<br>
Used the model to make predictions and returned the predicted house price.
<br>
<br>
<br>
API USAGE GUIDE:-


<br>
<br>
To deploy and access the House Price Prediction API, follow these steps:

1. Start the API Server:-<br>
In the Jupyter Notebook cell where the model training and API code exist, execute the following command to run the FastAPI application:<br>
    uvicorn.run(app, host="0.0.0.0", port=8000)

<br>
<br>
2. Access the API Documentation<br>
Once the server is running, open your browser and navigate to:
http://127.0.0.1:8000/docs
This interactive Swagger UI allows you to test the API by providing input values and receiving predictions.

<br>
<br>
3. Making Predictions
<br>
Send a POST request to the /predict endpoint with the following JSON payload:<br><br>
{
  "MedInc": 3.5,
  "HouseAge": 25,
  "AveRooms": 5.2,
  "AveBedrms": 1.1,
  "Population": 1000,
  "AveOccup": 2.8,
  "Latitude": 37.77,
  "Longitude": -122.42
}
<br><br>
 4. Result:-<br>
A successful response will return the predicted house price:<br>{
  "Predicted Price": 2.35
}


<br>
<br>
5.Stopping the Server<br>
To stop the API server, press CTRL + C in the terminal or interrupt the Jupyter Notebook kernel.



<br>
<br>
![image](https://github.com/user-attachments/assets/dd3dff09-cd06-495b-8775-fce46cbfe98d)


<br><br>
![image](https://github.com/user-attachments/assets/411c3dad-0c97-4d2e-bfc3-cf3d41bc6996)



