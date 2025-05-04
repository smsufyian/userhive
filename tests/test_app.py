"""
Tests for the FastAPI application.
"""

import os
import sys
import importlib.util
from fastapi.testclient import TestClient

# Get the absolute path to the app.py file
app_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src", "userhive", "app.py")
)

# Load the module dynamically
spec = importlib.util.spec_from_file_location("app_module", app_path)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)

# Get the app from the loaded module
app = app_module.app
client = TestClient(app)


def test_hello_world():
    """
    Test that the root endpoint returns the expected hello world message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "helloworld"}

def test_function():
    assert True
