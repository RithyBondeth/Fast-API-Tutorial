#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the FastAPI project using uvicorn
# --reload: Automatically restart the server when files change
# --host 0.0.0.0: Make the server accessible from outside the container (if applicable)
# --port 8000: Run on port 8000
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
