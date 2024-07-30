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
    assert response.status == '200 OK'
    assert 'endpoint' in data
    assert 'temphumid' in data

def test_receive_data_vibration(client):
    response = client.post("/sensors/vibration",
                           data=json.dumps({"uuid": "1234", "value_x": "123.4", "value_y": "567.8", "value_z": "134.5"}),
                           content_type='application/json')
    data = response.get_data(as_text=True)
    assert response.status == '200 OK'
    assert 'endpoint' in data
    assert 'vibration' in data

def test_receive_data_geolocation(client):
    response = client.post("/sensors/geolocation",
                           data=json.dumps({"uuid": "1234", "latitud": "123.45", "longitud": "234.45", "altitud": "678.90", "velociy": "23.45", "gps_time": "23:45", "gps_date": "01Jan2024"}),
                           content_type='application/json')

    assert response.status == '200 OK'
    data = response.get_data(as_text=True)
    assert 'endpoint' in data
    assert 'geolocation' in data

def test_receive_data_undefined(client):
    response = client.post("/sensors/unsoported",
                           data=json.dumps({"uuid": "1234", "data": "some data"}),
                           content_type='application/json')

    assert response.status == '400 BAD REQUEST'
