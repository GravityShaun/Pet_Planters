# Pet Planter Image Upload Service

A FastAPI-based service for uploading and managing pet images for custom 3D planter generation. This service handles secure image uploads, storage, and order management for Pet Planters customers.

## 🚀 Service Information

| Service | Port | Protocol | Purpose | Health Check |
|---------|------|----------|---------|-------------|
| **Image Upload Service** | `8007` | HTTP | REST API for image uploads and order management | `GET /health` |
| **Metrics** | `8007` | HTTP | Prometheus metrics endpoint | `GET /metrics` |
| **Auth Service** | `8000` | HTTP | User authentication and JWT validation | `GET /health` |

---

## 📡 API Endpoints

### Health & Service Info

#### `GET /`
- **Description**: Service information and available endpoints
- **Response**:
  ```json
  {
    "service": "Pet Planter Image Upload Service",
    "version": "2.0.0",
    "description": "Upload pet images for custom planter generation",
    "endpoints": { ... }
  }
  ```

#### `GET /health`
- **Description**: Health check endpoint
- **Response**:
  ```json
  {
    "status": "healthy",
    "timestamp": "2025-10-05T12:00:00"
  }
  ```

### Image Upload & Order Management

#### `POST /api/images/upload`
- **Description**: Upload pet images for custom planter order
- **Authentication**: Required (JWT Bearer token)
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `files`: List of image files (required, max 4 files)
  - `pet_name`: Name of the pet (optional)
  - `pet_type`: Type of pet (dog, cat, etc.) (optional)
  - `notes`: Additional notes for the order (optional)
- **File Requirements**:
  - Maximum 4 images per upload
  - Supported formats: JPG, JPEG, PNG, WEBP
  - Maximum file size: 10MB per file
- **Response**:
  ```json
  {
    "success": true,
    "message": "Images uploaded successfully",
    "order_id": "abc123...",
    "files_uploaded": 3,
    "order_metadata": {
      "order_id": "abc123...",
      "user_id": "user-uuid",
      "pet_name": "Max",
      "pet_type": "dog",
      "notes": "Loves to play fetch",
      "files": [...],
      "upload_timestamp": "2025-10-05T12:00:00",
      "status": "pending"
    }
  }
  ```

#### `GET /api/images/orders`
- **Description**: Get all orders for the authenticated user
- **Authentication**: Required (JWT Bearer token)
- **Response**:
  ```json
  {
    "success": true,
    "orders": [...],
    "count": 5
  }
  ```

#### `GET /api/images/orders/{order_id}`
- **Description**: Get details for a specific order
- **Authentication**: Required (JWT Bearer token)
- **Response**:
  ```json
  {
    "success": true,
    "order": {
      "order_id": "abc123...",
      "user_id": "user-uuid",
      "pet_name": "Max",
      "files": [...],
      "upload_timestamp": "2025-10-05T12:00:00",
      "status": "pending"
    }
  }
  ```

#### `DELETE /api/images/orders/{order_id}`
- **Description**: Delete an order and its associated files
- **Authentication**: Required (JWT Bearer token)
- **Response**:
  ```json
  {
    "success": true,
    "message": "Order deleted successfully",
    "order_id": "abc123..."
  }
  ```

---

## 🗂️ File Storage Structure

Images are stored in the following directory structure:

```
uploads/
└── pet_images/
    └── {user_id}/
        └── {order_id}/
            ├── order_metadata.json
            ├── 20251005_120000_abc123.jpg
            ├── 20251005_120001_def456.jpg
            └── ...
```

Each order directory contains:
- **order_metadata.json**: Order information and file metadata
- **Image files**: Uploaded images with unique timestamped filenames

---

## 🔐 Authentication

All image upload and order management endpoints require authentication via JWT Bearer token. The token should be obtained from the Auth Service (port 8000) and passed in the `Authorization` header:

```
Authorization: Bearer <your-jwt-token>
```

---

## 🚀 Running the Service

### Development Mode

```bash
# Navigate to service directory
cd backend/-generateService

# Activate virtual environment (if using venv)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the service
python main.py
# OR
uvicorn main:app --reload --host 0.0.0.0 --port 8007
```

### Production Mode

```bash
# Using the start script
./start.sh
```

---

## 📊 Monitoring

### Prometheus Metrics

The service exposes Prometheus-compatible metrics at:

```
GET /metrics
```

Metrics include:
- Request counts
- Response times
- Error rates
- Upload statistics

---

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=api --cov-report=html
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the service directory:

```env
# Auth Service Configuration
AUTH_SERVICE_URL=http://localhost:8000

# JWT Configuration
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256

# Upload Configuration
MAX_UPLOAD_SIZE=10485760  # 10MB in bytes
MAX_FILES_PER_ORDER=4
```

---

## 📝 Future Enhancements

- [ ] Image preprocessing and optimization
- [ ] Automatic thumbnail generation
- [ ] Image quality validation
- [ ] Integration with 3D model generation service
- [ ] Order status tracking and notifications
- [ ] Admin dashboard for order management

---

## 🛠️ Tech Stack

- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **Python-Jose**: JWT token handling
- **Prometheus**: Metrics and monitoring
- **Pydantic**: Data validation

---

## 📞 Support

For issues or questions, please contact the development team or create an issue in the project repository.
