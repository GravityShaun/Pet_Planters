from fastapi import APIRouter
from datetime import datetime
from pathlib import Path

router = APIRouter()

@router.get("")
async def health_check():
    """
    Health check endpoint for the image upload service
    
    Returns:
        Service health status
    """
    try:
        # Check if upload directory exists and is writable
        upload_dir = Path("uploads/pet_images")
        upload_dir.mkdir(parents=True, exist_ok=True)
        
        # Test write permissions
        test_file = upload_dir / ".health_check"
        test_file.touch()
        test_file.unlink()
        
        return {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'Pet Planter Image Upload Service',
            'upload_directory': 'writable'
        }
    except Exception as e:
        return {
            'status': 'unhealthy',
            'timestamp': datetime.now().isoformat(),
            'error': str(e),
            'upload_directory': 'not writable'
        }
