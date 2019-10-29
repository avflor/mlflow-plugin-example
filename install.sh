#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Install the 'sqplugin' library
cd $DIR
pip3 install -e .

# Install the 'mlflow[sqlserver]' library (MLflow + SQLserver support)
cd $DIR/mlflow
pip3 install -e .[sqlserver]

