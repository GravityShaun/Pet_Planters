#!/bin/bash

# Kill existing processes on ports
kill_ports() {
    ports=(8000 8001 8002 8003 8004 8005 8006 8080)
    for port in "${ports[@]}"; do
        pid=$(lsof -t -i:$port)
        if [ ! -z "$pid" ]; then
            kill -9 $pid 2>/dev/null
        fi
    done
}

# Kill existing processes first
kill_ports

# Start all services in background
echo "Starting Auth Service..."
(cd "./-authService" && bash start.sh) > auth.log 2>&1 &
sleep 1

echo "Starting Chat Service..."
(cd "./-chatService" && bash start.sh) > chat.log 2>&1 &
sleep 1

echo "Starting WebRTC Chat Service..."
(cd "./-WebRtcFramework/-webrtcSocketService" && bash start.sh) > webrtc_chat.log 2>&1 &
sleep 1

echo "Starting Admin Service..."
(cd "./-adminService" && bash start.sh) > admin.log 2>&1 &
sleep 1

echo "Starting TURN Cluster Service..."
(cd "./-WebRtcFramework/turnCluster" && bash start.sh) > turn_cluster.log 2>&1 &

# Give services time to start
sleep 2

# Print status
echo "Services started on ports:"
echo "Auth Service:          http://localhost:8000"
echo "Chat Service:          http://localhost:8001 (FastAPI + Socket.IO)"
echo "WebRTC Service:        http://localhost:8002 (Socket.IO) & http://localhost:8005 (FastAPI)"
echo "Admin Service:         http://localhost:8005 (Admin Dashboard Backend)"
echo "TURN Cluster Service:  http://localhost:8080"
echo ""
echo "⚠️  NOTE: WebRTC and Admin services both use port 8005 but in different modes"
echo ""
echo "Frontend Applications:"
echo "Admin Dashboard:       http://localhost:5173 (Start with: cd Admin_Dashboard && npm run dev)"

# Keep script running and capture all logs
tail -f *.log