import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    with app.app_context():
        db.drop_all()

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome" in rv.data

def test_about_page(client):
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b"About our application" in rv.data

def test_create_user(client):
    with app.app_context():
        rv = client.post('/signup', data=dict(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            confirm_password='testpassword',
            first_name='Test',
            last_name='User',
            age='30',
            phone_number='1234567890'
        ), follow_redirects=True)
        print("Create User Response:", rv.data.decode('utf-8'))
        assert rv.status_code == 200
        assert b"Account created successfully" in rv.data or b"Email or Username already exists" in rv.data

def test_login_logout(client):
    with app.app_context():
        # Create a user
        client.post('/signup', data=dict(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            confirm_password='testpassword',
            first_name='Test',
            last_name='User',
            age='30',
            phone_number='1234567890'
        ))

        # Login
        rv = client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        print("Login Response:", rv.data.decode('utf-8'))
        assert rv.status_code == 200
        assert b"Logged in successfully" in rv.data or b"Welcome home !!!" in rv.data

        # Logout
        rv = client.get('/logout', follow_redirects=True)
        print("Logout Response:", rv.data.decode('utf-8'))
        assert rv.status_code == 200
        assert b"Logged out successfully" in rv.data