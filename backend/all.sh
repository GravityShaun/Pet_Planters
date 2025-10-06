#!/bin/bash

# Kill existing processes on ports
kill_ports() {
    ports=(8000 8005 8007)
    echo "Stopping existing services..."
    for port in "${ports[@]}"; do
        pid=$(lsof -t -i:$port)
        if [ ! -z "$pid" ]; then
            echo "  Killing process on port $port (PID: $pid)"
            kill -9 $pid 2>/dev/null
        fi
    done
}

# Kill existing processes first
kill_ports
echo ""

# Start all services in background
echo "Starting Auth Service..."
(cd "./-authService" && bash start.sh) > auth.log 2>&1 &
sleep 2

echo "Starting Admin Service..."
(cd "./-adminService" && bash start.sh) > admin.log 2>&1 &
sleep 2

echo "Starting Image Upload Service (Generate)..."
(cd "./-generateService" && bash start.sh) > generate.log 2>&1 &
sleep 2

# Give services time to start
echo "Waiting for services to initialize..."
sleep 3

# Print status
echo ""
echo "=================================="
echo "✅ Services Started Successfully"
echo "=================================="
echo ""
echo "Available Services:"
echo "  🔐 Auth Service:         http://localhost:8000"
echo "  👨‍💼 Admin Service:        http://localhost:8005"
echo "  📷 Image Upload Service: http://localhost:8007"
echo ""
echo "Health Checks:"
echo "  Auth:   curl http://localhost:8000/health"
echo "  Admin:  curl http://localhost:8005/health"
echo "  Images: curl http://localhost:8007/health"
echo ""
echo "Logs:"
echo "  Auth:     tail -f auth.log"
echo "  Admin:    tail -f admin.log"
echo "  Generate: tail -f generate.log"
echo ""
echo "To stop all services: pkill -f 'python.*main.py' or pkill -f uvicorn"
echo ""

# Keep script running and capture all logs
tail -f auth.log admin.log generate.log