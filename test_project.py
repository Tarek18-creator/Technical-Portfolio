import pytest
import requests_mock
from project import fetch_houses, filter_houses, generate_recommendations

# Sample data for testing
sample_houses = [
    {"id": 1, "price": 350000, "capacity": 2500, "location": "Miami - Downtown", "bedrooms": 3},
    {"id": 2, "price": 400000, "capacity": 3000, "location": "Miami - South Beach", "bedrooms": 3},
    {"id": 3, "price": 320000, "capacity": 2300, "location": "Miami - Little Havana", "bedrooms": 3},
    {"id": 4, "price": 450000, "capacity": 2700, "location": "Miami - Coconut Grove", "bedrooms": 4},
]

def test_fetch_houses():
    with requests_mock.Mocker() as m:
        m.get("http://localhost:5000/houses", json=sample_houses)
        result = fetch_houses()
        assert result == sample_houses

def test_filter_houses_price_capacity():
    preferences = {"type": "price_capacity", "price": 400000, "capacity": 2600}
    filtered = filter_houses(sample_houses, preferences)
    print("Filtered houses:", filtered)  # Add this line to see the actual output
    assert len(filtered) == 1
    assert filtered[0]["id"] == 2

def test_filter_houses_price_size():
    preferences = {"type": "price_size", "price": 350000, "size": 2400}
    filtered = filter_houses(sample_houses, preferences)
    assert len(filtered) == 1
    assert filtered[0]["id"] == 1

def test_filter_houses_price_location():
    preferences = {"type": "price_location", "price": 400000, "location": "Miami - South"}
    filtered = filter_houses(sample_houses, preferences)
    assert len(filtered) == 1
    assert filtered[0]["id"] == 2

def test_filter_houses_price_bedrooms():
    preferences = {"type": "price_bedrooms", "price": 500000, "bedrooms": 4}
    filtered = filter_houses(sample_houses, preferences)
    assert len(filtered) == 1
    assert filtered[0]["id"] == 4

def test_generate_recommendations():
    filtered_houses = [
        {"id": 3, "price": 320000, "capacity": 2300},
        {"id": 1, "price": 350000, "capacity": 2500},
        {"id": 2, "price": 400000, "capacity": 3000},
    ]
    recommendations = generate_recommendations(filtered_houses)
    assert len(recommendations) == 3
    assert recommendations.iloc[0]["id"] == 3
    assert recommendations.iloc[1]["id"] == 1
    assert recommendations.iloc[2]["id"] == 2

if __name__ == "__main__":
    pytest.main()
