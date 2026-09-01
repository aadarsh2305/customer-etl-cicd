def extract():
    """Return a list of raw customer records."""
    return [
        {"id": 1, "name": "Rahul", "country": "India"},
        {"id": 2, "name": "John", "country": "USA"},
        {"id": 3, "name": "Amit", "country": "India"},
    ]


def transform(customers):
    """Transform customer records into ETL-ready output format."""
    return [
        {
            "customer_id": customer["id"],
            "customer_name": customer["name"].upper(),
            "country": customer["country"],
        }
        for customer in customers
    ]


def load(customers):
    """Load transformed customers to the target sink."""
    print("Loading customers:")
    for customer in customers:
        print(customer)


def run_etl():
    """Execute the extract-transform-load pipeline end-to-end."""
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)


if __name__ == "__main__":
    run_etl()

