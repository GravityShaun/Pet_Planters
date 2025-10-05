#!/bin/bash

# Kill existing processes on ports
kill_ports() {
    ports=(8000 8001 8002 8003 8004 8005 8006 8007 8080)
    for port in "${ports[@]}"; do
        pid=$(lsof -t -i:$port)
        if [ ! -z "$pid" ]; then
            kill -9 $pid 2>/dev/null
        fi
    done
}

# Kill existing processes first
kill_ports

# Start all services in background with zero copy where available
echo "Starting Auth Service (regular)..."
(cd "./-authService" && bash start.sh) > auth.log 2>&1 &
sleep 1

echo "Starting Chat Service (zero copy)..."
(cd "./-chatService" && ZCASGI_PORT=8007 bash build_and_run_zero_copy.sh) > chat_zero_copy.log 2>&1 &
sleep 2

echo "Starting WebRTC Chat Service (zero copy)..."
(cd "./-WebRtcFramework/-webrtcSocketService" && bash build_and_run_zero_copy.sh) > webrtc_zero_copy.log 2>&1 &
sleep 2

echo "Starting Admin Service (regular)..."
(cd "./-adminService" && bash start.sh) > admin.log 2>&1 &
sleep 1

echo "Starting TURN Cluster Service (regular)..."
(cd "./-WebRtcFramework/turnCluster" && bash start.sh) > turn_cluster.log 2>&1 &

# Give services time to start
sleep 3

# Print status
echo "Services started on ports:"
echo "Auth Service:          http://localhost:8000 (regular)"
echo "Chat Service:          http://localhost:8007 (zero copy)"
echo "WebRTC Service:        http://localhost:8006 (zero copy enhanced)"
echo "Admin Service:         http://localhost:8005 (Admin Dashboard Backend)"
echo "TURN Cluster Service:  http://localhost:8080 (regular)"
echo ""
echo "Zero Copy Features:"
echo "• Chat Service: Full zero-copy ASGI with Rust backend"
echo "• WebRTC Service: Enhanced with zero-copy optimizations"
echo "• Performance monitoring available via /metrics endpoints"
echo ""
echo "Frontend Applications:"
echo "Admin Dashboard:       http://localhost:5173 (Start with: cd Admin_Dashboard && npm run dev)"

# Keep script running and capture all logs
tail -f *.log
