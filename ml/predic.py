import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri(
    "sqlite:////Users/moon/Downloads/Python/Day13/ml-expense-platform/mlflow.db"
)

run_id = "ff31407dec1d40b58972f27df2b73df4"

model = mlflow.sklearn.load_model(
    f"runs:/{run_id}/model"
)

prediction = model.predict(["Starbucks latte"])

print(prediction)