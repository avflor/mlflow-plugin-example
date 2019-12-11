from distutils.core import setup

setup(
  name='sqlplugin',
  version='1.0',
  description='Plugin that provides DB Artifact Store functionality for MLflow',
  author='Avrilia Floratou',
  author_email='avrilia.floratou@@microsoft.com',
  packages=['sqlplugin'],
  install_requires=[
      'mlflow',
  ],
  entry_points={
      "mlflow.artifact_repository": [
        "mssql=sqlplugin.store.artifact:DBArtifactRepository",
        "sqlite=sqlplugin.store.artifact:DBArtifactRepository",
      ]
  },
)
