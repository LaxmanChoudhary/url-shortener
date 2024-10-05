#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set up the database
export FLASK_APP=src/run.py
#export FLASK_ENV=development

# Initialize the database
#flask init-db

# Populate the database with sample data
#flask populate-db

# db migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

echo "Setup complete. You can now run the application with './scripts/run.sh'"