# House-Price-Prediction
<br>
<br>
It is a machine learning model which predicts the house prices in calfornia .The dataset used in this model is California housing dataset which is present in sklearn library.
<br>
<br>
PROJECT WORKFLOW:-
<br>
<br>
1. Data Preprocessing & Feature Engineering
Dataset: The California Housing dataset was used.
Steps Taken:
Loaded the dataset and converted it into a Pandas DataFrame.
Checked for missing values and handled them (dropped NaN values).
Split data into features (X) and target (y).
Performed train-test split (80-20%) to separate training and testing sets.
<br>
<br>
2. Model Selection & Optimization
Model Used: RandomForestRegressor
Hyperparameter Optimization: Used RandomizedSearchCV to find the best combination of:
n_estimators: Number of trees in the forest.
max_depth: Maximum depth of the tree.
min_samples_split: Minimum samples required to split a node.
min_samples_leaf: Minimum samples required at a leaf node.
Best Model: The best-performing model was selected and saved using joblib.
<br>
<br>
3. Deployment Strategy
Framework: FastAPI was used for deploying the model as a REST API.
Steps:
Created a FastAPI application (app.py).
Defined API endpoint (/predict) to receive house features as JSON input.
Loaded the trained model (house_price_model.pkl).
Used the model to make predictions and returned the predicted house price.

