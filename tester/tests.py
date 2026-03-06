from tester.client import get


def test_list_all_breeds():

    r = get("/breeds/list/all")

    assert r["status_code"] == 200
    assert r["json"]["status"] == "success"
    assert isinstance(r["json"]["message"], dict)


def test_random_image():

    r = get("/breeds/image/random")

    assert r["status_code"] == 200
    assert r["json"]["status"] == "success"
    assert isinstance(r["json"]["message"], str)


def test_hound_random():

    r = get("/breed/hound/images/random")

    assert r["status_code"] == 200
    assert r["json"]["status"] == "success"
    assert "hound" in r["json"]["message"]


def test_invalid_breed():

    r = get("/breed/notabreed/images/random")

    assert r["status_code"] == 404


def test_json_content():

    r = get("/breeds/image/random")

    assert "status" in r["json"]
    assert "message" in r["json"]


def test_latency():

    r = get("/breeds/image/random")

    assert r["latency_ms"] < 3000