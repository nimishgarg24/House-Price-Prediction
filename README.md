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
3. Deployment Strategy
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
