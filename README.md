# Example SQL Server plugin for MLflow

This repository provides an example for converting the SQLServer integration PR submitted to the main MLflow repository by @avflor (https://github.com/mlflow/mlflow/pull/1734) into an MLflow plugin.

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

1. `sqlplugin`: This package includes the `DBArtifactRepository` class that is used to read and write artifacts from SQL databases. This class sets the attribute `is_plugin = True` in order to indicate that the class is an MLflow artifact repository plugin. This package also includes the SQLAlchemy database models referenced by `DBArtifactRepository`. The files associated with this implementation were taken from the MLflow GitHub PR by @avflor (https://github.com/mlflow/mlflow/pull/1734); a couple of small modifications were applied for correctness purposes that are not relevant to the plugin. Most critically, the package's `setup.py` file defines entrypoints that tell MLflow to automatically associate the `mssql` and `sqlite` URIs with the `DBArtifactRepository` implementation when the `sqlplugin` library is installed. The entrypoints are configured as follows:

```
entry_points={
    "mlflow.artifact_repository": [
      "mssql=sqlplugin.store:DBArtifactRepository",
      "sqlite=sqlplugin.store:DBArtifactRepository",
    ]
},
```


2. `mlflow`: This package refers to a branch of the MLflow repository based on the MLflow version 1.3.0 release. This custom branch applies the changes in this PR: https://github.com/dbczumar/mlflow/pull/4. This PR simply defines a custom installation parameter called `[sqlserver]`, which enables the user to install MLflow and `sqlplugin` together by running: `pip install mlflow[sqlserver]`. This is a nice-to-have feature that makes the `sqlplugin` library easier to install along with MLflow, but it is not strictly required for the plugin to work

**Note: sqlite is only included here for testing purposes. We  recommend that this plugin ultimately target mssql exclusively**

**Note 2: `sqlplugin` is used as an example plugin package name. Feel free to use another name of your choosing.**

### Development workflow

We propose that the CISL team will control the development and testing of the `sqlplugin` component in their own repository. The MLflow team will review and incorporate a PR similar to https://github.com/dbczumar/mlflow/pull/4 in order to provide users with the ability to install both MLflow and the SQL Server plugin library at the same time.

## User experience

The proposed plugin structure and development workflow provide the following experience to the end user:

Users can simply install MLflow with the SQL Server plugin via `pip install mlflow[sqlserver]` and then use MLflow as normal. The SQLServer artifact support will be provided automatically using the previously-described setup entrypoints mechanism.

## Additional considerations

The SQLServer integration PR submitted by @avflor (https://github.com/mlflow/mlflow/pull/1734) defines some additional logic for parsing artifact URIs of the type `ArtifactRepositoryType.DB` (https://github.com/mlflow/mlflow/blob/c0e1fa56587f858dddf15f26852b2fa8c51c6d51/mlflow/tracking/artifact_utils.py#L59-L76, https://github.com/mlflow/mlflow/blob/c0e1fa56587f858dddf15f26852b2fa8c51c6d51/mlflow/store/artifact_repository_registry.py#L97-L102). The MLflow team will need to determine whether or not this additiona logic is necessary and potentially merge artifact URI parsing changes into th main repository for plugin compatibility purposes.
