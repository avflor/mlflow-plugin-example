import mlflow
from mlflow.store.artifact_repository_registry import _artifact_repository_registry

from sqlplugin.store.db_artifact_repo import DBArtifactRepository

_artifact_repository_registry.register('sqlite', DBArtifactRepository)
_artifact_repository_registry.register('mssql', DBArtifactRepository)

