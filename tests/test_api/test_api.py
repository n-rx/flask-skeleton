created_id = 0


def test_create_data(client):
	body = {"data": "Test_example"}
	response = client.post("/api/data", json=body)
	assert response.status_code == 200
	response_json = response.json
	global created_id
	created_id = response_json["data"]["id"]

	assert response_json["success"] is True
	assert response_json["data"]["data"] == body.get("data")


# You can add here another tests
def test_get_data(client):
	response = client.get("/api/data")
	assert response.status_code == 200

	response_json = response.json
	assert response_json["success"] is True
	assert response_json["Data"][-1]["id"] == created_id
