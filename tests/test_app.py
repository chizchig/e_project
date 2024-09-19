import pytest
from app import app, db, User
from flask import session

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()

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
    assert b"About Us" in rv.data

def test_create_user(client):
    with client.session_transaction() as sess:
        sess['_flashes'] = []
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
    assert rv.status_code == 200
    assert b"Account created successfully" in rv.data or b"Account created successfully" in session['_flashes'][0][1].encode()

def test_login_logout(client):
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

    # Clear flash messages
    with client.session_transaction() as sess:
        sess['_flashes'] = []

    # Login
    rv = client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b"Logged in successfully" in rv.data or any(b"Logged in successfully" in f[1].encode() for f in session['_flashes'])

    # Logout
    rv = client.get('/logout', follow_redirects=True)
    assert rv.status_code == 200
    assert b"Logged out successfully" in rv.data or any(b"Logged out successfully" in f[1].encode() for f in session['_flashes'])