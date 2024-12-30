from flask import Flask, Blueprint, jsonify, request, abort

# Create a Flask application
app = Flask(__name__)

# Create a Blueprint object
employee_routes = Blueprint('employee_routes', __name__)

# In-Memory Data
employees = [
    {
        "id": 1,
        "name": "John Doe",
        "position": "Software Engineer"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "position": "Data Scientist"
    },
    {
        "id": 3,
        "name": "Mike Smith",
        "position": "Web Developer"
    }
]

# Home Route
@employee_routes.route("/", methods=["GET"])
def home():
    return "Welcome to the Employee API Project"

# Get all employees
@employee_routes.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# Get employee by ID
@employee_routes.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    employee = next((emp for emp in employees if emp["id"] == id), None)
    if employee:
        return jsonify(employee)
    else:
        abort(404, description="Employee not found")

# Add new employee
@employee_routes.route("/employees", methods=["POST"])
def add_employee():
    if not request.json:
        abort(400, description="Request body is missing")
    employee = {
        "id": employees[-1]["id"] + 1,  # Automatically assign a new ID
        "name": request.json.get("name"),
        "position": request.json.get("position")
    }
    employees.append(employee)
    return jsonify(employee), 201

# Update employee by ID
@employee_routes.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    employee = next((emp for emp in employees if emp["id"] == id), None)
    if not employee:
        abort(404, description="Employee not found")
    if not request.json:
        abort(400, description="Request body is missing")
    data = request.json
    employee.update(data)
    return jsonify(employee)

# Delete employee by ID
@employee_routes.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    employee = next((emp for emp in employees if emp["id"] == id), None)
    if not employee:
        abort(404, description="Employee not found")
    employees.remove(employee)
    return jsonify(employee)

# Register the Blueprint
app.register_blueprint(employee_routes)

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)
