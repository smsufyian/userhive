#!/bin/bash
# Script to set up pre-commit hooks for the userhive project

# Check if pre-commit is installed
if ! command -v pre-commit &> /dev/null; then
    echo "pre-commit is not installed. Installing..."
    pip install pre-commit
fi

# Install the pre-commit hooks
echo "Installing pre-commit hooks..."
pre-commit install

echo "Pre-commit hooks have been installed successfully!"
echo "Now your code will be automatically formatted, linted, and tested before each commit."