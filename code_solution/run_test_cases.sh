#!/bin/bash

# Enable strict mode
set -euo pipefail

# Determine the script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Add the `code_solution` directory to PYTHONPATH
export PYTHONPATH="$SCRIPT_DIR"

# Navigate to the test_cases directory
cd "$SCRIPT_DIR/test_cases"

# Run the test script
python3 -m unittest test_max_clique.py

# Check the exit status
if [ $? -eq 0 ]; then
    echo "All test cases passed successfully!"
else
    echo "Some test cases failed. Check the output for details."
fi
