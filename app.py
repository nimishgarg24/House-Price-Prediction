
import numpy as np
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define input data schema
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Define API endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = np.array([[features.MedInc, features.HouseAge, features.AveRooms, features.AveBedrms, 
                             features.Population, features.AveOccup, features.Latitude, features.Longitude]])
    prediction = model.predict(input_data)
    return {"Predicted Price": prediction[0]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
