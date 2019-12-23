import mlflow
from mlflow.tracking.client import MlflowClient

client = MlflowClient()
exp_name = "artifact_test_experiment_sql"
if client.get_experiment_by_name(exp_name) is None:
    client.create_experiment(exp_name, artifact_location="mssql+pyodbc://sqluser:Mlflow2019@microsoft@sqltestml.database.windows.net:1433/mlflow_test?driver=ODBC+Driver+17+for+SQL+Server")
mlflow.set_experiment(exp_name)

fpath = "test.txt"
with open(fpath, "w") as f:
    f.write("TEST")

with mlflow.start_run():
    mlflow.log_artifact(fpath, "")
