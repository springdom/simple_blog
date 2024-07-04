import os
import sys
import pytest

# Add the project directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app  # Assuming your Flask app factory is in app.py

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Simple Blog" in response.data

def test_404(client):
    """Test a 404 error."""
    response = client.get('/non_existent_page')
    assert response.status_code == 404

