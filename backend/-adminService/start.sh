#!/bin/bash

cd "$(dirname "$0")"

create_venv() {
    echo "Creating virtual environment..."
    rm -rf venv
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing requirements..."
    pip install --upgrade pip
    pip install -r requirements.txt
}

echo "Starting Admin Service..."

# Check if virtual environment exists and is working
if [ ! -d "venv" ]; then
    create_venv
else
    source venv/bin/activate
    # Test if required packages are available in the venv
    if ! python -c "import fastapi, uvicorn, httpx, pydantic" 2>/dev/null; then
        echo "Virtual environment appears broken, recreating..."
        create_venv
    fi
fi

echo "Admin Service starting on port 8005..."
echo "Dashboard URL: http://localhost:5173"
echo "API URL: http://localhost:8005"

# Start the service using venv python
python -m uvicorn main:app --host 0.0.0.0 --port 8005 --reload 