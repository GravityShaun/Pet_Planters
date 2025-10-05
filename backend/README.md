# CTRL_CHAT_2 Backend Services

A comprehensive backend ecosystem consisting of three main services: Authentication, Chat, and WebRTC, designed for real-time communication with video calling capabilities.

## 🚀 **PORT MAPPING & SERVICE OVERVIEW**

### **Core Service Port Allocation**

| Service | Primary Port | Secondary Port | Protocol | Purpose | Health Check |
|---------|-------------|----------------|----------|---------|-------------|
| **🔐 Auth Service** | `8000` | - | HTTP | User authentication, JWT tokens, user management | `GET /health` |
| **💬 Chat Service** | `8007` | - | HTTP + WebSocket | Real-time messaging, channel management, offline sync (zero-copy) | `GET /health` |
| **📹 WebRTC Service** | `8002` (Socket.IO) | `8005` (FastAPI) | WebSocket + HTTP | Video calls, WebRTC signaling, call management | `GET /health` |

### **Infrastructure Ports**

| Service | Port | Protocol | Purpose | Health Check |
|---------|------|----------|---------|-------------|
| **Redis Cache** | `6380` | TCP | Distributed state, session management | `redis-cli ping` |
| **TURN Server** | `3478` (TCP/UDP) | TCP/UDP | WebRTC media relay | `GET /health` on 8080 |
| **TURN Server (TLS)** | `5349` | TCP/TLS | Secure WebRTC relay | `GET /health` on 8080 |
| **TURN API** | `8080` | HTTP | TURN credentials, management | `GET /health` |
| **HAProxy** | `8404` (Stats) | HTTP | Load balancer monitoring | `GET /` |
| **Prometheus** | `9090` | HTTP | Metrics collection | `GET /-/healthy` |
| **Grafana** | `3000` | HTTP | Metrics visualization | `GET /api/health` |

---

## 📊 **SERVICE ARCHITECTURE OVERVIEW**

### 🔐 **Authentication Service (Port 8000)**

**Purpose**: Centralized user authentication and management using JWT tokens

**Technology Stack**:
- **Framework**: FastAPI
- **Database**: SQLite (auth.db)
- **Security**: JWT tokens, bcrypt password hashing
- **File Storage**: Local file system for avatars

**Core Features**:
- User registration and login
- JWT access/refresh token management
- Password reset and change
- User profile management with avatar uploads
- Role-based access control

**Key Endpoints**:
```
POST /api/auth/signup          # User registration
POST /api/auth/login           # User authentication  
POST /api/auth/refresh         # Token refresh
POST /api/auth/logout          # User logout
GET  /api/auth/me              # Get current user info
PUT  /api/auth/profile         # Update user profile
GET  /api/auth/users           # Get all users (for contacts)
GET  /health                   # Service health check
```

**Database Schema**:
- `users` - User accounts, profiles, authentication data
- `refresh_tokens` - JWT refresh token storage and management

---

### 💬 **Chat Service (Port 8007)**

**Purpose**: Real-time messaging system with offline message delivery

**Technology Stack**:
- **Framework**: FastAPI + Socket.IO
- **Database**: SQLite (chat.db) 
- **Real-time**: Socket.IO for WebSocket communication
- **Cache**: Redis for session management

**Core Features**:
- Private channel creation between users
- Real-time message delivery via Socket.IO
- Offline message queuing and delivery
- Message synchronization for multi-device support
- Typing indicators and message reactions
- File attachment support

**Key HTTP Endpoints**:
```
POST /api/chat/channel         # Create/get private channel
GET  /api/chat/channels        # Get user's channels
GET  /api/chat/sync/{id}       # Sync messages since timestamp
POST /api/chat/sync/{id}       # Upload messages for sync
GET  /api/chat/undelivered     # Get offline messages
POST /api/chat/delivered       # Mark messages as delivered
GET  /health                   # Service health check
```

**Socket.IO Events**:
```
connect                        # User authentication and offline message delivery
join_channel                   # Join channel for real-time updates
leave_channel                  # Leave channel
message                        # Send/receive real-time messages
typing                         # Typing indicator events
notify_channel_created         # Notify users of new channels
```

**Database Schema**:
- `users` - Chat user profiles and display information
- `channels` - Private channels between users
- `messages` - All chat messages with attachments and reactions
- `channel_members` - User membership in channels
- `undelivered_messages` - Offline message queue

---

### 📹 **WebRTC Service (Ports 8002 + 8005)**

**Purpose**: Video/audio calling with WebRTC signaling and TURN server infrastructure

**Technology Stack**:
- **Framework**: FastAPI (8005) + Socket.IO (8002)
- **Database**: Redis for distributed state management
- **WebRTC**: TURN/STUN servers for media relay
- **Monitoring**: Prometheus + Grafana
- **Load Balancing**: HAProxy for high availability

**Core Features**:
- Video and audio call initiation/management
- WebRTC signaling (offer/answer/ICE candidate exchange)
- TURN/STUN server infrastructure for NAT traversal
- Distributed session management across multiple instances
- Call quality monitoring and metrics
- Automatic failover and load balancing

**FastAPI Endpoints (Port 8005)**:
```
GET  /api/webrtc/ice-config          # Get STUN/TURN servers
POST /api/webrtc/call/initiate       # Start video/audio call
POST /api/webrtc/call/respond        # Accept/reject call
POST /api/webrtc/call/end/{id}       # End active call
GET  /api/webrtc/call/{id}           # Get call status
GET  /metrics                        # Prometheus metrics
GET  /health                         # Service health check
```

**Socket.IO Events (Port 8002)**:
```
webrtc_call_initiate           # Start call signaling
webrtc_call_response           # Accept/reject call
webrtc_signaling_message       # WebRTC offer/answer/ICE exchange
webrtc_incoming_call           # Incoming call notification
join_webrtc_call_room          # Join call room
leave_webrtc_call_room         # Leave call room
```

**Infrastructure Components**:
- **TURN Server (3478/5349)**: Media relay for WebRTC
- **HAProxy (8404)**: Load balancing and failover
- **Redis (6380)**: Distributed session state
- **Prometheus (9090)**: Metrics collection
- **Grafana (3000)**: Performance monitoring

---

## 🚀 **QUICK START**

### **Development Mode (All Services)**
```bash
cd backend
./all.sh
```

This starts all services with the following URLs:
- **Auth Service**: `http://localhost:8000`
- **Chat Service**: `http://localhost:8007` (FastAPI + Socket.IO combined with zero-copy)
- **WebRTC Service**: `http://localhost:8002` (Socket.IO) + `http://localhost:8005` (FastAPI)
- **TURN Server**: `turn://localhost:3478`, `turns://localhost:5349`

### **Individual Service Startup**
```bash
# Auth Service
cd authService && ./start.sh

# Chat Service  
cd -chatService && ./start.sh

# WebRTC Framework
cd -WebRtcFramework && ./all.sh
```

### **Production Deployment**
```bash
cd -WebRtcFramework
docker-compose up -d
```

---

## 🔗 **SERVICE INTEGRATION**

### **Authentication Flow**
1. User registers/logs in via **Auth Service (8000)**
2. JWT tokens returned for API access
3. **Chat Service (8007)** validates JWT for messaging access
4. **WebRTC Service (8002/8005)** validates JWT for call access

### **Messaging Flow**
1. User requests channel via **Chat Service HTTP API (8007)**
2. Real-time messaging via **Chat Service Socket.IO (8007)**
3. Offline messages queued and delivered on reconnection

### **Video Call Flow**
1. Call initiated via **WebRTC FastAPI (8005)**
2. WebRTC signaling via **WebRTC Socket.IO (8002)**
3. Media flows through **TURN Server (3478/5349)**
4. Call state managed in **Redis (6380)**

---

## 🔧 **FRONTEND INTEGRATION**

### **Service URLs Configuration**
```typescript
const config = {
  authApi: 'http://localhost:8000/api/auth',
  chatApi: 'http://localhost:8007/api/chat', 
  chatSocket: 'http://localhost:8007',  // Socket.IO on same port as HTTP (zero-copy)
  webrtcApi: 'http://localhost:8005/api/webrtc',
  webrtcSocket: 'http://localhost:8002',
  turnApi: 'http://localhost:8080'
};
```

### **Authentication Headers**
```javascript
const headers = {
  'Authorization': `Bearer ${jwtToken}`,
  'Content-Type': 'application/json'
};
```

---

## 🏗️ **DATABASE SCHEMAS**

### **Auth Service Database (auth.db)**
```sql
-- User accounts and authentication
users (user_id, email, password_hash, first_name, last_name, avatar_url, is_verified, created_at)

-- JWT refresh token management  
refresh_tokens (token_id, user_id, token_hash, expires_at, created_at)
```

### **Chat Service Database (chat.db)**
```sql
-- Chat user profiles
users (user_id, profile_id, name, avatar_url, email, is_active, created_at)

-- Private channels between users
channels (channel_id, name, description, channel_type, created_by, created_at)

-- All chat messages
messages (message_id, channel_id, sender_profile_id, text, attachments, reactions, created_at)

-- Channel membership
channel_members (channel_id, profile_id, joined_at)

-- Offline message delivery queue
undelivered_messages (id, message_id, recipient_profile_id, channel_id, delivered_at)
```

### **WebRTC Service (Redis)**
```
-- Active call sessions
call:{call_id} -> {caller_id, receiver_id, status, created_at}

-- User socket sessions  
user_session:{user_id} -> {socket_id, instance_id, last_activity}

-- Call signaling data
signaling:{call_id} -> {offers, answers, ice_candidates}
```

---

# WebRTC Socket Service Framework

A production-ready WebRTC signaling service built with FastAPI and Socket.IO, designed for scalability and enterprise deployment. Features distributed processing, memory management, throttling, and comprehensive monitoring.

## 🚀 Service Port Mapping

## Key Ports

- Auth - 8000
- WebRTC - 8005
- WebRTC Socket - 8002

### Core Services
| Service | Port(s) | Protocol | Purpose | Health Check |
|---------|---------|----------|---------|-------------|
| **WebRTC Socket Service (FastAPI)** | `8005` | HTTP | REST API endpoints, WebRTC signaling | `GET /health` |
| **WebRTC Socket Service (Socket.IO)** | `8002` | WebSocket | Real-time communication, Socket.IO | TCP socket check |
| **Redis** | `6380` | TCP | Distributed state management, caching | `redis-cli ping` |
| **Backend Service** | `8000` | HTTP | Django backend API | `GET /api/health/` |

### TURN/STUN Services
| Service | Port(s) | Protocol | Purpose | Health Check |
|---------|---------|----------|---------|-------------|
| **TURN Server (TCP)** | `3478` | TCP | WebRTC TURN relay | `GET /health` on 8080 |
| **TURN Server (UDP)** | `3478` | UDP | WebRTC TURN relay | `GET /health` on 8080 |
| **TURN Server (TLS)** | `5349` | TCP/TLS | Secure WebRTC TURN relay | `GET /health` on 8080 |
| **TURN Server (API)** | `8080` | HTTP | TURN credentials API | `GET /health` |
| **TURN Media Range** | `49160-49200` | UDP | Media streaming ports | N/A |

### Load Balancing & Proxy
| Service | Port(s) | Protocol | Purpose | Health Check |
|---------|---------|----------|---------|-------------|
| **HAProxy (Stats)** | `8404` | HTTP | Load balancer statistics | `GET /` |
| **HAProxy (TCP)** | `3479` | TCP | Load balanced TURN TCP | `GET /` on 8404 |
| **HAProxy (TLS)** | `5350` | TCP/TLS | Load balanced TURN TLS | `GET /` on 8404 |
| **HAProxy (Alternative)** | `3480` | TCP/UDP | Alternative TURN routing | `GET /` on 8404 |

### Monitoring & Observability
| Service | Port(s) | Protocol | Purpose | Health Check |
|---------|---------|----------|---------|-------------|
| **Prometheus** | `9090` | HTTP | Metrics collection | `GET /-/healthy` |
| **Grafana** | `3000` | HTTP | Metrics visualization | `GET /api/health` |
| **Coturn Metrics** | `9641` | HTTP | TURN server metrics | N/A |

### Additional Services
| Service | Port(s) | Protocol | Purpose | Health Check |
|---------|---------|----------|---------|-------------|
| **Nginx** | `80`, `443` | HTTP/HTTPS | Web server, reverse proxy | N/A |
| **PostgreSQL** | `5432` | TCP | Production database | N/A |

## 🏗️ Architecture Overview

### Core Components
- **WebRTC Socket Service**: FastAPI (8005) + Socket.IO (8002) for real-time WebRTC signaling
- **Distributed State Management**: Redis (6380) for multi-node scaling and session management
- **Database Layer**: SQLite for development, PostgreSQL for production
- **Load Balancing**: HAProxy (8404) for high availability and traffic distribution
- **Monitoring**: Prometheus (9090) + Grafana (3000) for comprehensive observability

### Production Features
- **Distributed Processing Framework**: Multi-node orchestration with automatic failover
- **Memory Management System**: L1/L2 caching with predictive algorithms
- **Execution Engine**: Rate limiting and throttling to prevent resource contention
- **Scaling Infrastructure**: Auto-scaling triggers and horizontal scaling support
- **Security Layer**: Authentication, CORS, and encrypted execution environment

## 🚀 Quick Start

### Development Mode
```bash
cd backend/-WebRtcFramework
./all.sh
```

### Production Deployment
```bash
cd backend/-WebRtcFramework
docker-compose up -d
```

This starts all services with the following URLs:
- **FastAPI WebRTC Service**: `http://localhost:8005`
- **Socket.IO WebRTC Service**: `http://localhost:8002`
- **Redis**: `redis://localhost:6380`
- **Backend API**: `http://localhost:8000`
- **TURN Server**: `turn://localhost:3478` (TCP/UDP), `turns://localhost:5349` (TLS)
- **HAProxy Stats**: `http://localhost:8404`
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000`

### TURN Cluster Only
```bash
cd backend/-WebRtcFramework/turnCluster
docker-compose up -d
```

This starts only the TURN infrastructure:
- **TURN Server**: `turn://localhost:3478`, `turns://localhost:5349`
- **TURN API**: `http://localhost:8080`
- **HAProxy**: `http://localhost:8404` (stats)
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000`

## 📡 API Endpoints

### Core WebRTC APIs (Port 8005)
- `GET /health` - Service health check
- `GET /api/webrtc/ice-config` - ICE servers (STUN/TURN) configuration
- `POST /api/webrtc/call/initiate` - Initiate video/audio call
- `POST /api/webrtc/call/respond` - Accept/reject incoming call
- `POST /api/webrtc/call/end/{call_id}` - End active call
- `GET /api/webrtc/call/{call_id}` - Get call status
- `GET /metrics` - Prometheus metrics

### TURN Server APIs (Port 8080)
- `GET /health` - TURN server health check
- `POST /credentials` - Generate TURN credentials
- `GET /metrics` - TURN server metrics

### Backend APIs (Port 8000)
- `GET /api/health/` - Backend health check
- `GET /api/users/` - User management
- `GET /api/calls/` - Call history

### Monitoring & Metrics (Port 8005)
- `GET /metrics` - Prometheus metrics
- `GET /api/socket/status/{channel_id}` - Socket connection status

### Socket.IO Events (Port 8002)
- `webrtc_call_initiate` - Start call
- `webrtc_call_response` - Accept/reject call
- `webrtc_signaling_message` - WebRTC offer/answer/ICE exchange
- `webrtc_incoming_call` - Incoming call notification
- `join_webrtc_call_room` / `leave_webrtc_call_room` - Room management

## 🔧 Frontend Integration

### Configuration
```typescript
// frontend/src/lib/constants.ts
const config = {
  // Socket.IO for real-time communication
  webrtcSocketUrl: 'http://localhost:8002',
  
  // FastAPI for REST endpoints
  webrtcApiUrl: 'http://localhost:8005/api/webrtc',
  
  // Backend API
  backendApiUrl: 'http://localhost:8000/api',
  
  // TURN server API
  turnApiUrl: 'http://localhost:8080',
};
```

### Socket Connection (Port 8002)
```javascript
import { io } from 'socket.io-client';

const socket = io('http://localhost:8002', {
  auth: { user_id: 'user_id', token: 'jwt_token' },
  transports: ['websocket', 'polling']
});

// Listen for incoming calls
socket.on('webrtc_incoming_call', (data) => {
  console.log('Incoming call:', data);
  // Handle call with call_id, caller_id, call_type
});

// Join call room
socket.emit('join_webrtc_call_room', { call_id: 'call_123' });
```

### ICE Servers Configuration (Port 8005)
```javascript
// Get ICE servers from WebRTC service
const response = await fetch('http://localhost:8005/api/webrtc/ice-config');
const { ice_servers } = await response.json();

// Configure WebRTC peer connection
const peerConnection = new RTCPeerConnection({ 
  iceServers: ice_servers 
});
```

### TURN Credentials (Port 8080)
```javascript
// Get TURN credentials directly from TURN server
const response = await fetch('http://localhost:8080/credentials', {
  method: 'POST',
  headers: { 'Authorization': `Bearer ${token}` }
});
const credentials = await response.json();
```

## 🏭 Production Architecture

### Distributed Processing Framework
- **Load Distribution**: Dynamic resource allocation based on real-time demand
- **Multi-Node Orchestration**: Automatic failover and state synchronization via Redis
- **Data Partitioning**: Optimized schema for WebRTC workloads
- **Session Stickiness**: Socket.IO rooms maintained across instances

### Memory Management System
- **L1 Cache**: In-memory TTL cache for active call data (10s TTL)
- **L2 Cache**: Redis distributed cache for cross-node state synchronization
- **Predictive Caching**: Reduces unnecessary data transfer between nodes
- **Auto-scaling Memory**: Dynamic memory allocation based on usage patterns

### Execution Engine & Throttling
- **Rate Limiting**: Per-user, per-endpoint throttling (configurable)
- **Event Rate Limiting**: Socket.IO event throttling (5 events/second/user)
- **Resource Contention Prevention**: Queue management for high-load scenarios
- **API Abuse Protection**: Automatic blocking of excessive requests

### Scaling Infrastructure
- **Horizontal Scaling**: Redis-based session sharing across instances
- **Auto-scaling Triggers**: Custom metrics for Kubernetes HPA
- **State Migration**: Seamless capacity expansion without service interruption
- **Load Balancing**: HAProxy for WebRTC-optimized routing

## 🔐 Security Features

### Authentication & Authorization
- **JWT Token Validation**: All endpoints require valid tokens
- **User Session Management**: Redis-based session tracking
- **Role-Based Access Control**: Configurable user permissions
- **API Rate Limiting**: Prevents abuse and DDoS attacks

### Network Security
- **CORS Protection**: Configurable allowed origins
- **TURN Authentication**: Time-based credentials with HMAC-SHA1
- **TLS Encryption**: Secure TURN connections on port 5349
- **Session Security**: Encrypted session data in Redis

### Monitoring & Alerting
- **Failed Authentication Tracking**: Prometheus metrics
- **Rate Limit Violations**: Automated alerting
- **Suspicious Activity Detection**: Pattern recognition

## 🌐 Environment Configuration

### Development (.env)
```bash
# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_PORT=6380

# TURN Server Configuration
EXTERNAL_IP=127.0.0.1
TURN_SECRET=development_secret
TURN_REALM=localhost
TURN_MIN_PORT=49160
TURN_MAX_PORT=49200

# HAProxy Configuration
HAPROXY_TCP_PORT=3479
HAPROXY_TLS_PORT=5350
HAPROXY_STATS_PORT=8404

# Monitoring
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000
```

### Production (.env)
```bash
# Redis Configuration
REDIS_URL=redis://redis-cluster:6379/0
REDIS_PORT=6380
REDIS_CPU_LIMIT=1.0
REDIS_MEMORY_LIMIT=1G

# TURN Server Configuration
EXTERNAL_IP=your.public.ip
TURN_SECRET=secure_production_secret
TURN_REALM=your-domain.com
TURN_MIN_PORT=49160
TURN_MAX_PORT=49200

# Database
DATABASE_URL=postgresql://user:pass@db:5432/webrtc

# Security
CORS_ORIGINS=https://your-frontend.com,https://your-app.com
JWT_SECRET=your-jwt-secret

# Load Balancing
HAPROXY_TCP_PORT=3479
HAPROXY_TLS_PORT=5350
HAPROXY_STATS_PORT=8404

# Monitoring
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000
GRAFANA_ADMIN_PASSWORD=secure_password

# Resource Limits
TURN_CPU_LIMIT=2.0
TURN_MEMORY_LIMIT=4G
BACKEND_CPU_LIMIT=1.0
BACKEND_MEMORY_LIMIT=2G
```

## 📊 Monitoring & Observability

### Prometheus Metrics (Port 9090)
```bash
# WebRTC Service Metrics
webrtc_active_connections          # Current WebSocket connections
webrtc_active_calls               # Ongoing video/audio calls
webrtc_call_duration_seconds      # Call duration histogram
webrtc_cache_hit_rate             # L1/L2 cache performance
webrtc_rate_limit_violations      # Throttling events
webrtc_failed_calls               # Call failure rate
webrtc_signaling_messages         # WebRTC signaling message count

# TURN Server Metrics
turn_active_allocations           # Active TURN allocations
turn_bytes_sent                   # Total bytes relayed
turn_bytes_received              # Total bytes received
turn_failed_allocations          # Failed TURN requests

# System Metrics
redis_connected_clients          # Redis connection count
haproxy_current_sessions         # HAProxy active sessions
```

### Grafana Dashboards (Port 3000)
- **WebRTC Overview**: Real-time connection monitoring, call statistics
- **TURN Server Performance**: Allocation rates, bandwidth usage
- **System Health**: CPU, memory, Redis performance
- **Call Quality**: Success rates, duration, error tracking
- **Security**: Authentication failures, rate limiting events

### Health Checks
```bash
# Service Health Checks
curl http://localhost:8005/health     # WebRTC FastAPI
curl http://localhost:8002/health     # Socket.IO (via TCP)
curl http://localhost:8000/api/health/ # Backend Django
curl http://localhost:8080/health     # TURN server
curl http://localhost:8404/stats      # HAProxy stats
curl http://localhost:9090/-/healthy  # Prometheus
curl http://localhost:3000/api/health # Grafana

# Redis Health
redis-cli -h localhost -p 6380 ping

# Comprehensive Health Check
curl http://localhost:8005/api/webrtc/ice-config
```

## 🧪 Testing

### Automated Test Suite
```bash
# Core functionality tests
python test_all_sh.py

# Comprehensive production tests
python test_webrtc_framework.py

# Load testing
python test_load_webrtc.py --concurrent=100 --duration=300
```

### Manual Testing
```bash
# Test WebRTC signaling
curl -X POST http://localhost:8005/api/webrtc/call/initiate \
  -H "Content-Type: application/json" \
  -d '{"caller_id": "user1", "receiver_id": "user2", "call_type": "video"}'

# Test TURN credentials
curl -X POST http://localhost:8080/credentials \
  -H "Authorization: Bearer YOUR_TOKEN"

# Test Socket.IO connection
node -e "
const io = require('socket.io-client');
const socket = io('http://localhost:8002');
socket.on('connect', () => console.log('Connected'));
"
```

### WebRTC Test Client
```bash
cd WebRTC_Browser_APP
npm install
npm run dev
# Access: http://localhost:3000
```

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);
```

### Calls Table
```sql
CREATE TABLE calls (
    call_id TEXT PRIMARY KEY,
    caller_id TEXT NOT NULL,
    receiver_id TEXT NOT NULL,
    call_type TEXT DEFAULT 'video' CHECK (call_type IN ('video', 'audio')),
    status TEXT DEFAULT 'initiated' CHECK (status IN ('initiated', 'ringing', 'accepted', 'ended', 'failed')),
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    duration INTEGER DEFAULT 0,
    quality_score INTEGER,
    disconnect_reason TEXT,
    FOREIGN KEY (caller_id) REFERENCES users(user_id),
    FOREIGN KEY (receiver_id) REFERENCES users(user_id)
);
```

### User Sessions Table
```sql
CREATE TABLE user_sessions (
    session_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    instance_id TEXT NOT NULL,
    socket_id TEXT,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'idle', 'disconnected')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address TEXT,
    user_agent TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

### Call Events Table
```sql
CREATE TABLE call_events (
    event_id TEXT PRIMARY KEY,
    call_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_data JSON,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (call_id) REFERENCES calls(call_id)
);
```

## 🚀 Deployment

### Docker Compose (Recommended)
```bash
# Full stack deployment
docker-compose up -d

# Scale specific services
docker-compose up -d --scale webrtc-socket-service=3
docker-compose up -d --scale turn=2
```

### Kubernetes
```bash
# Deploy to Kubernetes
cd k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml  # Auto-scaling

# Monitor deployment
kubectl get pods -l app=webrtc-socket-service
kubectl logs -f deployment/webrtc-socket-service
```

### Manual Setup
```bash
# Start individual services
cd -webrtcSocketService
./start.sh

cd -turnCluster
./start.sh

cd -backendCluster
./start.sh
```

## 📈 Performance Benchmarks

### Single Instance Performance
| Metric | Value | Port |
|--------|-------|------|
| **WebSocket Connections** | ~1,000 concurrent | 8002 |
| **Simultaneous Calls** | ~100 video calls | 8005 |
| **Signaling Latency** | <50ms | 8002 |
| **API Response Time** | <100ms | 8005 |
| **Memory Usage** | ~512MB base | N/A |
| **CPU Usage** | ~30% under load | N/A |

### Multi-Instance (with Redis)
| Metric | Value | Notes |
|--------|-------|-------|
| **Connections** | Unlimited | Horizontal scaling via Redis |
| **Calls** | Unlimited | Distributed across nodes |
| **Latency** | <100ms | Including Redis overhead |
| **Memory** | Auto-scaling | Dynamic allocation |
| **Throughput** | 10,000+ req/sec | With proper load balancing |

## 🔧 Troubleshooting

### Common Production Issues

#### High Memory Usage
```bash
# Check L1 cache size
curl http://localhost:8005/metrics | grep cache_size

# Adjust cache settings
export LOCAL_CACHE_MAX_SIZE=1000
```

#### Redis Connection Failures
```bash
# Check Redis connectivity
redis-cli -h localhost -p 6380 ping

# Monitor Redis connections
redis-cli -h localhost -p 6380 info clients
```

#### Rate Limiting Issues
```bash
# Check rate limiting metrics
curl http://localhost:8005/metrics | grep rate_limit

# View HAProxy stats
curl http://localhost:8404/stats
```

#### TURN Server Issues
```bash
# Check TURN server health
curl http://localhost:8080/health

# Verify external IP configuration
curl http://localhost:8080/credentials

# Test TURN connectivity
turnutils_uclient -T -u test -w test your.external.ip
```

### Debug Commands
```bash
# Service-specific debugging
docker-compose logs webrtc-socket-service
docker-compose logs turn
docker-compose logs redis
docker-compose logs haproxy

# Port connectivity testing
nc -zv localhost 8002  # Socket.IO
nc -zv localhost 8005  # FastAPI
nc -zv localhost 6380  # Redis
nc -zv localhost 3478  # TURN
nc -zv localhost 8404  # HAProxy

# Performance monitoring
curl -s http://localhost:8005/metrics | grep webrtc_
curl -s http://localhost:9090/api/v1/query?query=webrtc_active_connections
```

### Log Analysis
```bash
# WebRTC service logs
docker logs webrtc-socket-service 2>&1 | grep ERROR

# TURN server logs
docker logs turn 2>&1 | grep -i "allocation\|error"

# HAProxy access logs
docker logs haproxy 2>&1 | grep -E "(5xx|4xx)"
```

## 📚 API Documentation

### WebRTC Service API (Port 8005)
Full API documentation available at: `http://localhost:8005/docs`

### TURN Server API (Port 8080)
Full API documentation available at: `http://localhost:8080/docs`

### Socket.IO Events (Port 8002)
Event documentation available in the `/docs` directory

---

**Production-ready WebRTC signaling with enterprise scalability and comprehensive monitoring! 🚀**

For support, please check the troubleshooting section or submit an issue on the repository.

---

## �� **ENHANCED BACKEND FEATURES**

### **🔄 Global Load Balancer & Session Management**

**Redis-Backed Distributed Session Management**:
- Both Chat and WebRTC services now use `AsyncRedisManager` for Socket.IO
- Enables horizontal scaling across multiple service instances
- Shared session state allows seamless failover between replicas
- Configured with Redis URLs: `redis://redis:6379/0`

**Horizontal Scaling Configuration**:
```yaml
# Chat Service - 2 replicas by default
deploy:
  replicas: 2
  mode: replicated
  
# WebRTC Service - Auto-scaling via Kubernetes HPA
minReplicas: 2
maxReplicas: 20
```

### **⚡ Message Optimization**

**High-Performance JSON Processing**:
- `orjson` library integrated for 2-3x faster JSON serialization/deserialization
- Zero-copy parsing capabilities for improved memory efficiency
- Configured in both services: `json=orjson`

**Message Compression**:
- Gzip compression enabled for Socket.IO messages
- Compression threshold: 512 bytes (configurable)
- Reduces bandwidth usage by 60-80% for large messages

**Message Prioritization**:
- Priority field added to chat messages: `priority: 'normal' | 'high' | 'low'`
- Enables future implementation of priority-based message queuing
- Backward compatible with existing message structure

### **📈 Kubernetes Auto-Scaling**

**Custom Metrics-Based HPA**:
```yaml
# WebRTC Service Auto-scaling
metrics:
  - webrtc_active_connections (target: 500 per pod)
  - webrtc_active_calls (target: 100 per pod)
  - webrtc_cache_hit_rate (target: 50% minimum)
  - CPU utilization (target: 70%)
  - Memory utilization (target: 80%)
```

**Prometheus Metrics Integration**:
- Custom metrics exposed at `/metrics` endpoint
- ServiceMonitor configured for automatic scraping
- Grafana dashboards for real-time monitoring
- Metrics include connection counts, call statistics, and cache performance

**Scaling Behavior**:
- Scale up: 100% increase (double pods) within 60 seconds
- Scale down: 10% decrease with 5-minute stabilization
- Aggressive scaling up, conservative scaling down

### **🔒 Enhanced NGINX Security**

**Security Headers**:
```nginx
# HSTS with preload and subdomain inclusion
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

# Content Security Policy
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'..." always;

# Additional security headers
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "no-referrer" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
```

**Rate Limiting & DDoS Protection**:
```nginx
# Rate limiting configuration
limit_req_zone $binary_remote_addr zone=webrtc_ratelimit:10m rate=10r/s;
limit_req zone=webrtc_ratelimit burst=20 nodelay;

# Body size limits
client_max_body_size 10M;
```

**Protocol-Level Protection**:
- TLS 1.2/1.3 only with modern cipher suites
- Server version hiding: `server_tokens off`
- Enhanced SSL configuration with perfect forward secrecy

### **📊 Monitoring & Observability**

**Prometheus Metrics**:
```
# WebRTC Service Metrics
webrtc_active_connections          # Current WebSocket connections
webrtc_active_calls               # Active video/audio calls
webrtc_cache_hits_total           # Redis cache hit counter
webrtc_cache_misses_total         # Redis cache miss counter
```

**Health Checks**:
- Comprehensive health endpoints for all services
- Redis connectivity monitoring
- Database availability checks
- Service-specific health indicators

**Logging & Tracing**:
- Structured logging with correlation IDs
- Performance metrics collection
- Error tracking and alerting capabilities

---

## 🧪 **TESTING & VALIDATION**

### **Integration Testing**
```bash
# Run comprehensive integration tests
cd backend
python3 test_integration_simple.py
```

**Test Coverage**:
- ✅ Redis-backed session management validation
- ✅ orjson and compression configuration
- ✅ Prometheus metrics endpoint verification
- ✅ NGINX security headers validation
- ✅ Kubernetes HPA configuration
- ✅ Docker Compose scaling setup

### **Performance Testing**
```bash
# Load testing for WebRTC service
curl -s http://localhost:8005/metrics | grep webrtc_active_connections

# Chat service message throughput
# Socket.IO client connections with priority messages
```