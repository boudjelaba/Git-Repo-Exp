from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_about():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200

def test_home_contains_title():
    client = app.test_client()
    response = client.get("/")
    assert b"Accueil" in response.data

def test_home_content(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bienvenue" in response.data