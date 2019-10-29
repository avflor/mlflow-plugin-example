import mlflow
from mlflow.tracking.client import MlflowClient

client = MlflowClient()
exp_name = "artifact_test_experiment"
if client.get_experiment_by_name(exp_name) is None:
    client.create_experiment(exp_name, artifact_location="sqlite:///testartifactdb")
mlflow.set_experiment(exp_name)

fpath = "test.txt"
with open(fpath, "w") as f:
    f.write("TEST")

with mlflow.start_run():
    mlflow.log_artifact(fpath, "")
