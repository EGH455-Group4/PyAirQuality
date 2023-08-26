#!/bin/bash

# Assumes requirements are already installed.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Script directory: $SCRIPT_DIR"

cd $SCRIPT_DIR/

source paq/bin/activate

until python3 ip_set.py
do
    sleep 5
done

deactivate
