import pandas as pd
import joblib

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

model = joblib.load("salary_model.pkl")

test_df = pd.read_csv(
    "s3://salary-mlops-processed-data-445411728398/test/test.csv"
)

X_test = test_df[["YearsExperience", "Age"]]
y_test = test_df["Salary"]

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("MAE:", mae)
print("R2 Score:", r2)
