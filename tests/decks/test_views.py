
def test_view_loads(test_client):
    response = test_client.get("/decks/hello/")

    assert response.status_code == 200
