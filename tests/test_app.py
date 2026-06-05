def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Accueil" in response.get_data(as_text=True)
    assert "Bienvenue" in response.get_data(as_text=True)

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "À propos" in body

def test_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert "Page non trouvée" in response.get_data(as_text=True)