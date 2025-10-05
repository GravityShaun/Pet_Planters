#!/usr/bin/env python3
"""
Simple test script to verify the image upload API is working.
This requires the service to be running on port 8007.
"""

import requests
import sys

def test_health_check():
    """Test the health check endpoint"""
    try:
        response = requests.get('http://localhost:8007/health')
        print(f"✓ Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    try:
        response = requests.get('http://localhost:8007/')
        print(f"✓ Root endpoint: {response.status_code}")
        print(f"  Service: {response.json()['service']}")
        return response.status_code == 200
    except Exception as e:
        print(f"✗ Root endpoint failed: {e}")
        return False

def test_upload_without_auth():
    """Test upload endpoint without authentication (should work now)"""
    try:
        files = {'files': ('test.jpg', b'fake image data', 'image/jpeg')}
        data = {
            'pet_name': 'Test Pet',
            'pet_type': 'dog',
            'notes': 'Test upload'
        }
        response = requests.post(
            'http://localhost:8007/api/images/upload', 
            files=files,
            data=data
        )
        
        if response.status_code == 200:
            print(f"✓ Upload without auth successful: {response.status_code}")
            result = response.json()
            if result.get('success'):
                print(f"  Order ID: {result.get('order_id')}")
                return True
        else:
            print(f"✗ Upload failed with status: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
    except Exception as e:
        print(f"✗ Upload test failed: {e}")
        return False

def main():
    print("Testing Pet Planter Image Upload Service")
    print("=" * 50)
    print()
    
    tests = [
        ("Health Check", test_health_check),
        ("Root Endpoint", test_root_endpoint),
        ("Image Upload (No Auth)", test_upload_without_auth),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"Running: {name}")
        results.append(test_func())
        print()
    
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        sys.exit(1)

if __name__ == "__main__":
    main()

