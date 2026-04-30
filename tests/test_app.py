import json


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'ACEest Fitness & Gym'
    assert 'version' in data


def test_get_members(client):
    response = client.get('/api/members')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(member['name'] == 'Samantha' for member in data)


def test_get_workouts(client):
    response = client.get('/api/workouts')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 3
    assert data[0]['title'] == 'Strength Training'


def test_create_booking(client):
    payload = {
        'member_id': 1,
        'workout_id': 1,
        'scheduled_for': '2026-05-01',
    }
    response = client.post('/api/bookings', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['member_id'] == 1
    assert data['workout_id'] == 1


def test_health(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
