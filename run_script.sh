#!/bin/bash

# Set environment variables
export OPENAI_API_KEY=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
export GITHUB_API_KEY=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

# Debugging: Print environment variables
echo "OPENAI_API_KEY: $OPENAI_API_KEY"
echo "GITHUB_API_KEY: $GITHUB_API_KEY"

# Run your Python script
python3 github_openai.py