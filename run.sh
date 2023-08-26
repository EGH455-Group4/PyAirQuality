#!/bin/bash

# Assumes requirements are already installed.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Script directory: $SCRIPT_DIR"

cd $SCRIPT_DIR/

source paq/bin/activate

python3 main.py

deactivate
