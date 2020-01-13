# SQL Server plugin for MLflow

This repository provides a MLflow plugin that allows users to use SQL Server as the artifact store for MLflow.

## Installation and use
To install this plugin package:

1. Initialize the custom `mlflow` submodule by running the following command from the repository root:
```
$ git submodule update --init
```

2. Invoke the `install.sh` script from the repository's root directory. This script uses `pip` to install the `sqlplugin` library (which provides a custom artifact repository implementation) as well as a custom version of the MLflow library that defines a `[sqlserver]` extras tag to automatically install the `sqlplugin` dependency when MLflow is installed (this is not strictly required for the plugin to work).

Once the plugin has been installed along with the custom version of MLflow, run the artifact logging test Python script located at `tests/log_artifacts.py`. If this Python script creates an `mlruns` directory and a SQLite database called `testartifactdb` without emitting errors, the plugin is working as expected.

## Implementation overview
This repository contains two main Python packages:

1. `sqlplugin`: This package includes the `DBArtifactRepository` class that is used to read and write artifacts from SQL databases. This class sets the attribute `is_plugin = True` in order to indicate that the class is an MLflow artifact repository plugin. This package also includes the SQLAlchemy database models referenced by `DBArtifactRepository`. The package's `setup.py` file defines entrypoints that tell MLflow to automatically associate the `mssql` URIs with the `DBArtifactRepository` implementation when the `sqlplugin` library is installed. The entrypoints are configured as follows:

```
entry_points={
    "mlflow.artifact_repository": [
      "mssql=sqlplugin.store:DBArtifactRepository",
    ]
},
```

2. `mlflow`: This package refers to a branch of the MLflow repository based on the MLflow version 1.3.0 release. This custom branch applies the changes in this PR: https://github.com/dbczumar/mlflow/pull/4. This PR simply defines a custom installation parameter called `[sqlserver]`, which enables the user to install MLflow and `sqlplugin` together by running: `pip install mlflow[sqlserver]`. This is a nice-to-have feature that makes the `sqlplugin` library easier to install along with MLflow, but it is not strictly required for the plugin to work


## User experience

The proposed plugin structure and development workflow provide the following experience to the end user:

Users can simply install MLflow with the SQL Server plugin via `pip install mlflow[sqlserver]` and then use MLflow as normal. The SQLServer artifact support will be provided automatically using the previously-described setup entrypoints mechanism.
