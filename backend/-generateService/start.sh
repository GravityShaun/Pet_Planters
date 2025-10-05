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

# Check if virtual environment exists and is working
if [ ! -d "venv" ]; then
    create_venv
else
    source venv/bin/activate
    # Test if uvicorn is available in the venv
    if ! python -c "import uvicorn" 2>/dev/null; then
        echo "Virtual environment appears broken, recreating..."
        create_venv
    fi
fi

# Start the Uvicorn server for Image Upload Service on port 8007 using venv python
python -m uvicorn main:app --host 0.0.0.0 --port 8007
