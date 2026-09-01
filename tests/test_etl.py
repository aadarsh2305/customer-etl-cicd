from src.etl import extract, transform


def test_extract():
    data = extract()

    assert len(data) == 3
    assert data[0]["name"] == "Rahul"


def test_transform():
    data = extract()
    transformed = transform(data)

    assert transformed[0]["customer_id"] == 1
    assert transformed[0]["customer_name"] == "WRONG_NAME"

