#!/usr/bin/env bash

if [ -x "$(command -v pip3)" ];
then
    PIPCMD=pip3
else
    PIPCMD=pip
fi

echo Installing required packages using: `which $PIPCMD`.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Install the 'sqplugin' library
cd $DIR
$PIPCMD install -e .

# Install the 'mlflow[sqlserver]' library (MLflow + SQLserver support)
cd $DIR/mlflow
$PIPCMD install -e .[sqlserver]

