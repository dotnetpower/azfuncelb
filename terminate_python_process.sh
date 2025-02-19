#!/bin/bash

# Find the process ID of the running Python process
PYTHON_PID=$(pgrep -f "python .*azure.functions_worker")

if [ -z "$PYTHON_PID" ]; then
    echo "No Python process found"
    exit 1
fi

# Terminate the specific Python process
kill $PYTHON_PID