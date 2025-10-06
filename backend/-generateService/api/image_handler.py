from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import datetime
import logging
import os
import uuid
import shutil
from pathlib import Path
from .auth import auth_dependency, User

router = APIRouter()
logger = logging.getLogger(__name__)

# Configure upload directory
UPLOAD_DIR = Path("uploads/pet_images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Allowed file extensions and max file size
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def is_allowed_file(filename: str) -> bool:
    """Check if the file extension is allowed"""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

def generate_unique_filename(original_filename: str) -> str:
    """Generate a unique filename while preserving the extension"""
    ext = Path(original_filename).suffix.lower()
    unique_id = uuid.uuid4().hex
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{timestamp}_{unique_id}{ext}"

@router.post("/upload")
async def upload_pet_images(
    files: List[UploadFile] = File(...),
    pet_name: Optional[str] = Form(None),
    pet_type: Optional[str] = Form(None),
    notes: Optional[str] = Form(None)
):
    """
    Upload pet images for custom planter generation
    
    Args:
        files: List of image files (max 4, each max 10MB)
        pet_name: Optional name of the pet
        pet_type: Optional type of pet (dog, cat, etc.)
        notes: Optional additional notes for the order
    
    Returns:
        JSON response with upload status and file information
    """
    logger.info("=" * 80)
    logger.info("🆕 NEW IMAGE UPLOAD REQUEST RECEIVED")
    logger.info("=" * 80)
    
    try:
        # Validate number of files
        logger.info(f"📊 Number of files received: {len(files)}")
        if not files or len(files) == 0:
            logger.warning("❌ No files provided in upload request")
            raise HTTPException(status_code=400, detail="No files provided")
        
        if len(files) > 4:
            logger.warning(f"❌ Too many files: {len(files)} (max 4 allowed)")
            raise HTTPException(status_code=400, detail="Maximum 4 images allowed")
        
        # Use anonymous user for now (no auth required)
        user_id = "anonymous"
        user_email = "anonymous@petplanters.com"
        
        logger.info(f"👤 User: {user_id}")
        logger.info(f"📧 Email: {user_email}")
        logger.info(f"🐾 Pet Name: {pet_name or 'Not provided'}")
        logger.info(f"🐕 Pet Type: {pet_type or 'Not provided'}")
        logger.info(f"📝 Notes: {notes or 'None'}")
        
        # Create user-specific directory
        user_upload_dir = UPLOAD_DIR / user_id
        user_upload_dir.mkdir(parents=True, exist_ok=True)
        
        # Create order directory
        order_id = uuid.uuid4().hex
        order_dir = user_upload_dir / order_id
        order_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"📁 Created order directory: {order_dir}")
        logger.info(f"🆔 Order ID: {order_id}")
        logger.info("-" * 80)
        
        uploaded_files = []
        
        # Process each file
        for idx, file in enumerate(files):
            logger.info(f"📄 Processing file {idx + 1}/{len(files)}: {file.filename}")
            
            # Validate file extension
            if not is_allowed_file(file.filename):
                logger.error(f"❌ Invalid file extension: {file.filename}")
                raise HTTPException(
                    status_code=400, 
                    detail=f"File {file.filename} has an invalid extension. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
                )
            logger.info(f"   ✅ File extension valid: {Path(file.filename).suffix}")
            
            # Read file content
            contents = await file.read()
            file_size = len(contents)
            file_size_mb = file_size / (1024 * 1024)
            
            logger.info(f"   📦 File size: {file_size:,} bytes ({file_size_mb:.2f} MB)")
            
            # Validate file size
            if file_size > MAX_FILE_SIZE:
                logger.error(f"❌ File too large: {file_size_mb:.2f} MB (max 10 MB)")
                raise HTTPException(
                    status_code=400, 
                    detail=f"File {file.filename} exceeds maximum size of 10MB"
                )
            logger.info(f"   ✅ File size within limits")
            
            # Generate unique filename
            unique_filename = generate_unique_filename(file.filename)
            file_path = order_dir / unique_filename
            
            logger.info(f"   💾 Saving as: {unique_filename}")
            
            # Save file
            with open(file_path, 'wb') as f:
                f.write(contents)
            
            logger.info(f"   ✅ File saved successfully to: {file_path}")
            
            uploaded_files.append({
                'original_filename': file.filename,
                'saved_filename': unique_filename,
                'file_path': str(file_path.relative_to(UPLOAD_DIR)),
                'size_bytes': file_size,
                'index': idx
            })
            
            logger.info(f"   ✨ File {idx + 1} processed successfully")
            logger.info("")
        
        # Create order metadata
        logger.info("-" * 80)
        logger.info("📋 Creating order metadata...")
        
        order_metadata = {
            'order_id': order_id,
            'user_id': user_id,
            'user_email': user_email,
            'pet_name': pet_name,
            'pet_type': pet_type,
            'notes': notes,
            'files': uploaded_files,
            'upload_timestamp': datetime.now().isoformat(),
            'status': 'pending'
        }
        
        # Save metadata to JSON file
        import json
        metadata_path = order_dir / 'order_metadata.json'
        with open(metadata_path, 'w') as f:
            json.dump(order_metadata, f, indent=2)
        
        logger.info(f"💾 Metadata saved to: {metadata_path}")
        logger.info("-" * 80)
        logger.info("🎉 ORDER CREATED SUCCESSFULLY!")
        logger.info(f"🆔 Order ID: {order_id}")
        logger.info(f"📁 Total files: {len(uploaded_files)}")
        logger.info(f"💾 Total size: {sum(f['size_bytes'] for f in uploaded_files):,} bytes")
        logger.info(f"📍 Location: {order_dir}")
        logger.info("=" * 80)
        
        return JSONResponse(
            status_code=200,
            content={
                'success': True,
                'message': 'Images uploaded successfully',
                'order_id': order_id,
                'files_uploaded': len(uploaded_files),
                'order_metadata': order_metadata
            }
        )
        
    except HTTPException as e:
        logger.error(f"❌ HTTP Exception: {e.detail}")
        logger.error("=" * 80)
        raise e
    except Exception as e:
        logger.error(f"❌ Unexpected error during upload: {str(e)}", exc_info=True)
        logger.error("=" * 80)
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@router.get("/orders")
async def get_user_orders():
    """
    Get all orders for the current user (anonymous for now)
    
    Returns:
        List of orders with their metadata
    """
    logger.info("📋 GET /orders - Fetching all orders")
    try:
        user_id = "anonymous"
        user_upload_dir = UPLOAD_DIR / user_id
        
        if not user_upload_dir.exists():
            logger.info(f"📁 No orders found for user {user_id}")
            return {
                'success': True,
                'orders': [],
                'count': 0
            }
        
        orders = []
        
        # Iterate through order directories
        for order_dir in user_upload_dir.iterdir():
            if order_dir.is_dir():
                metadata_path = order_dir / 'order_metadata.json'
                if metadata_path.exists():
                    import json
                    with open(metadata_path, 'r') as f:
                        order_data = json.load(f)
                        orders.append(order_data)
        
        # Sort by upload timestamp (newest first)
        orders.sort(key=lambda x: x.get('upload_timestamp', ''), reverse=True)
        
        logger.info(f"✅ Found {len(orders)} orders for user {user_id}")
        
        return {
            'success': True,
            'orders': orders,
            'count': len(orders)
        }
        
    except Exception as e:
        logger.error(f"❌ Get orders error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to retrieve orders: {str(e)}")

@router.get("/orders/{order_id}")
async def get_order_details(
    order_id: str
):
    """
    Get details for a specific order
    
    Args:
        order_id: The order ID to retrieve
    
    Returns:
        Order metadata
    """
    try:
        user_id = "anonymous"
        order_dir = UPLOAD_DIR / user_id / order_id
        
        if not order_dir.exists():
            raise HTTPException(status_code=404, detail="Order not found")
        
        metadata_path = order_dir / 'order_metadata.json'
        if not metadata_path.exists():
            raise HTTPException(status_code=404, detail="Order metadata not found")
        
        import json
        with open(metadata_path, 'r') as f:
            order_data = json.load(f)
        
        return {
            'success': True,
            'order': order_data
        }
        
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Get order details error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to retrieve order: {str(e)}")

@router.delete("/orders/{order_id}")
async def delete_order(
    order_id: str
):
    """
    Delete an order and its associated files
    
    Args:
        order_id: The order ID to delete
    
    Returns:
        Success message
    """
    logger.info(f"🗑️  DELETE /orders/{order_id} - Deleting order")
    try:
        user_id = "anonymous"
        order_dir = UPLOAD_DIR / user_id / order_id
        
        if not order_dir.exists():
            logger.warning(f"❌ Order not found: {order_id}")
            raise HTTPException(status_code=404, detail="Order not found")
        
        # Count files before deletion
        file_count = len([f for f in order_dir.iterdir() if f.is_file() and f.suffix in ALLOWED_EXTENSIONS])
        logger.info(f"📁 Order contains {file_count} files")
        
        # Delete the entire order directory
        shutil.rmtree(order_dir)
        
        logger.info(f"✅ Successfully deleted order {order_id} for user {user_id}")
        
        return {
            'success': True,
            'message': 'Order deleted successfully',
            'order_id': order_id
        }
        
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"❌ Delete order error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to delete order: {str(e)}")

