from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("../training/salary_model.pkl")


class SalaryRequest(BaseModel):
    YearsExperience: float
    Age: int


@app.get("/")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: SalaryRequest):

    input_df = pd.DataFrame({
        "YearsExperience": [data.YearsExperience],
        "Age": [data.Age]
    })

    prediction = model.predict(input_df)

    return {
        "predicted_salary": float(prediction[0])
    }
