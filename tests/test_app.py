import pytest # type: ignore
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome" in rv.data

def test_about_page(client):
    """Test that about page loads correctly"""
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b"About" in rv.data

def test_404_page(client):
    """Test that 404 error is handled"""
    rv = client.get('/nonexistent-page')
    assert rv.status_code == 404

def test_create_user(client):
    """Test user creation"""
    rv = client.post('/signup', data=dict(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b"Account created" in rv.data

def test_login_logout(client):
    """Test login and logout functionality"""
    # Login
    rv = client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b"Logged in successfully" in rv.data

    # Logout
    rv = client.get('/logout', follow_redirects=True)
    assert rv.status_code == 200
    assert b"Logged out successfully" in rv.data