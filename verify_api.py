"""
Script to verify that the FastAPI application works correctly.
"""

import os
import sys
import importlib.util
import http.client
import json
import threading
import time
import uvicorn

# Get the absolute path to the app.py file
app_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src", "userhive", "app.py")
)

# Load the module dynamically
spec = importlib.util.spec_from_file_location("app_module", app_path)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)

# Get the app from the loaded module
app = app_module.app


def run_server():
    """Run the FastAPI server."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


# Start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

# Wait for the server to start
time.sleep(2)

# Make a request to the server
try:
    conn = http.client.HTTPConnection("127.0.0.1", 8000)
    conn.request("GET", "/")
    response = conn.getresponse()
    status_code = response.status
    response_data = json.loads(response.read().decode())

    print(f"Status code: {status_code}")
    print(f"Response: {response_data}")

    # Verify the response
    assert status_code == 200, f"Expected status code 200, got {status_code}"
    assert response_data == {
        "message": "helloworld"
    }, f"Expected response {{'message': 'helloworld'}}, got {response_data}"

    print("Verification successful! The API is working correctly.")
except Exception as e:
    print(f"Error: {e}")
