import joblib
import pandas as pd

MODEL_PATH = "../training/salary_model.pkl"

model = joblib.load(MODEL_PATH)

sample_data = pd.DataFrame({
    "YearsExperience": [5.0],
    "Age": [28]
})

prediction = model.predict(sample_data)

print("Predicted Salary:", prediction[0])
