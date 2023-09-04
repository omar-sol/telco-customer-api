from fastapi import FastAPI, Request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the model and transformer
lr = joblib.load("logistic_regression_model.pkl")
transformer = joblib.load('column_transformer.pkl')

class InputData(BaseModel):
    gender: str
    SeniorCitizen: str
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
async def predict(data: list[InputData]):
    df = pd.DataFrame([item.dict() for item in data])

    # Apply Label Encoding for binary categorical variables
    binary_features = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "PaperlessBilling",
    ]
    le = LabelEncoder()
    for feature in binary_features:
        df[feature] = le.fit_transform(df[feature])

    df = transformer.transform(df)

    y_pred_lr = lr.predict(df)
    y_prob_lr = lr.predict_proba(df)[:, 1]

    return {"prediction": y_pred_lr.tolist(), "probability": y_prob_lr.tolist()}
