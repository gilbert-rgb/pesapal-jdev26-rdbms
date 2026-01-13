from flask import Flask, request, jsonify
from rdbms.engine import Database

app = Flask(__name__)
db = Database()

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(db.select_all("users"))

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    message = db.insert("users", data)
    return jsonify({"message": message})

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    column = list(data.keys())[0]
    value = data[column]
    message = db.update("users", column, value, "id", user_id)
    return jsonify({"message": message})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    message = db.delete("users", "id", user_id)
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
