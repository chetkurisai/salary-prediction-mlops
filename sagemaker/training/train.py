import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression

train_df = pd.read_csv(
    "s3://salary-mlops-processed-data-445411728398/train/train.csv"
)

X_train = train_df[["YearsExperience", "Age"]]
y_train = train_df["Salary"]

model = LinearRegression()

model.fit(X_train, y_train)

joblib.dump(model, "salary_model.pkl")

print("Model trained successfully")
print("Model saved as salary_model.pkl")
