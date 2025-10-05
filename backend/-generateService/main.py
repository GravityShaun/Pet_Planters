from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from api import image_handler, health
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Pet Planter Image Upload Service",
    description="API service for uploading and managing pet images for custom planter generation",
    version="2.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(image_handler.router, prefix="/api/images", tags=["images"])
app.include_router(health.router, prefix="/health", tags=["health"])

@app.get("/")
async def root():
    """Root endpoint with service information"""
    return {
        "service": "Pet Planter Image Upload Service",
        "version": "2.0.0",
        "description": "Upload pet images for custom planter generation",
        "endpoints": {
            "health": "/health",
            "upload": "/api/images/upload",
            "orders": "/api/images/orders",
            "metrics": "/metrics"
        }
    }

@app.get("/metrics")
async def get_metrics():
    """Expose Prometheus metrics"""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)
