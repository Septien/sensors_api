import json

def test_hello(client):
    response = client.get("/hello")
    print(response.data)
    assert b'Hello, World!' in response.data

def test_receive_data_temphumid(client):
    response = client.post("/sensors/temphumid",
                            data=json.dumps({"uuid":"1234", "temp":"23.5", "hum":"15", "local_time":"14:35"}),
                            content_type='application/json')
    data = response.get_data(as_text=True)
    assert 'endpoint' in data
    assert 'temphumid' in data
