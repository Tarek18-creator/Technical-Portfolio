from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database of houses (10 houses)
houses = [
    {"id": 1, "price": 350000, "capacity": 2500, "location": "Miami - Downtown", "bedrooms": 3, "bathrooms": 2, "garage": True, "time_to_beach_minutes": 15},
    {"id": 2, "price": 400000, "capacity": 3000, "location": "Miami - South Beach", "bedrooms": 3, "bathrooms": 2, "garage": True, "time_to_beach_minutes": 5},
    {"id": 3, "price": 320000, "capacity": 2300, "location": "Miami - Little Havana", "bedrooms": 3, "bathrooms": 2, "garage": False, "time_to_beach_minutes": 20},
    {"id": 4, "price": 450000, "capacity": 2700, "location": "Miami - Coconut Grove", "bedrooms": 4, "bathrooms": 3, "garage": True, "time_to_beach_minutes": 10},
    {"id": 5, "price": 380000, "capacity": 2200, "location": "Miami - Coral Gables", "bedrooms": 3, "bathrooms": 2, "garage": True, "time_to_beach_minutes": 15},
    {"id": 6, "price": 500000, "capacity": 3200, "location": "Miami - Brickell", "bedrooms": 4, "bathrooms": 3, "garage": True, "time_to_beach_minutes": 8},
    {"id": 7, "price": 330000, "capacity": 2100, "location": "Miami - Wynwood", "bedrooms": 3, "bathrooms": 2, "garage": False, "time_to_beach_minutes": 25},
    {"id": 8, "price": 420000, "capacity": 2600, "location": "Miami - Mid Beach", "bedrooms": 3, "bathrooms": 2, "garage": True, "time_to_beach_minutes": 6},
    {"id": 9, "price": 340000, "capacity": 2400, "location": "Miami - North Beach", "bedrooms": 3, "bathrooms": 2, "garage": True, "time_to_beach_minutes": 12},
    {"id": 10, "price": 360000, "capacity": 2800, "location": "Miami - Key Biscayne", "bedrooms": 3, "bathrooms": 2, "garage": True, "time_to_beach_minutes": 3}
]

# Route to get all houses
@app.route('/houses', methods=['GET'])
def get_houses():
    return jsonify(houses)

# Route to get a specific house by ID
@app.route('/houses/<int:house_id>', methods=['GET'])
def get_house(house_id):
    house = next((h for h in houses if h["id"] == house_id), None)
    if house:
        return jsonify(house)
    return jsonify({"error": "House not found"}), 404

# Route to add a new house
@app.route('/houses', methods=['POST'])
def add_house():
    new_house = request.get_json(force=True)  # Ensure it treats input as JSON
    if not new_house:
        return jsonify({"error": "Invalid JSON data"}), 400
    new_house["id"] = max([h['id'] for h in houses], default=0) + 1  # Auto-generate unique ID
    houses.append(new_house)
    return jsonify(new_house), 201

# Route to update house information
@app.route('/houses/<int:house_id>', methods=['PUT'])
def update_house(house_id):
    house = next((h for h in houses if h["id"] == house_id), None)
    if house:
        house.update(request.get_json(force=True))  # Update with new data
        return jsonify(house)
    return jsonify({"error": "House not found"}), 404

# Route to delete a house
@app.route('/houses/<int:house_id>', methods=['DELETE'])
def delete_house(house_id):
    global houses
    houses = [h for h in houses if h["id"] != house_id]
    return jsonify({"message": "House deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
