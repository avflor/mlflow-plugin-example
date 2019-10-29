from distutils.core import setup

setup(
  name='sqlplugin',
  version='1.0',
  description='SQL plugin example for MLflow',
  author='Corey Zumar',
  author_email='corey.zumar@databricks.com',
  packages=['sqlplugin'],
  install_requires=[
      'mlflow',
  ],
  entry_points={
      "mlflow.artifact_repository": [
        "mssql=sqlplugin.store:DBArtifactRepository",
        "sqlite=sqlplugin.store:DBArtifactRepository",
      ]
  },
)
