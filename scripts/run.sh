#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Set environment variables
export FLASK_APP=src/run.py
export FLASK_ENV=development  # Change to 'production' for production environment

# Run the Flask application
flask run