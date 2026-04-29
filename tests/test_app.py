from copy import deepcopy

from fastapi.testclient import TestClient

import src.app as app_module

client = TestClient(app_module.app)
_original_activities = deepcopy(app_module.activities)


def setup_function() -> None:
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_original_activities))


def test_get_activities_returns_all_activities() -> None:
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert data["Chess Club"]["max_participants"] == 12
    assert isinstance(data["Chess Club"]["participants"], list)


def test_signup_for_activity_adds_participant() -> None:
    email = "test@mergington.edu"
    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"
    assert email in app_module.activities["Chess Club"]["participants"]


def test_signup_duplicate_participant_returns_400() -> None:
    email = "michael@mergington.edu"
    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_delete_participant_removes_participant() -> None:
    email = "michael@mergington.edu"
    response = client.delete(f"/activities/Chess%20Club/participants?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from Chess Club"
    assert email not in app_module.activities["Chess Club"]["participants"]


def test_delete_missing_participant_returns_404() -> None:
    email = "nobody@mergington.edu"
    response = client.delete(f"/activities/Chess%20Club/participants?email={email}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
