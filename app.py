from flask import Flask, request, jsonify
from data import users_list

app = Flask(__name__)

# Routes
@app.route("/", methods=["GET"])
def index():
    return "ARHEX API (Flask)"

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return jsonify(users_list), 200
    elif request.method == "POST":
        try:
            users_list.append(request.json)
            response = {
                "code": 201,
                "message": "Data Added"
            }
        except:
            response = {
                "code": 400,
                "message": "Error"
            }
        return jsonify(response), response["code"]

@app.route("/users/<name>", methods=["GET", "PUT", "DELETE"])
def single_users(name):
    if request.method == "GET":
        data = []
        for i in users_list:
            if i["name"] == name:
                data.append(i)
        if data != []:
            return jsonify(data), 200
        else:
            return jsonify(data), 404
    elif request.method == "PUT":
        try:
            for i in range(len(users_list)):
                if users_list[i]["name"] == name:
                    users_list[i] = request.json
            response = {
                "code": 201,
                "message": "Data Updated"
            }
        except:
            response = {
                "code": 404,
                "message": "Error"
            }
        return jsonify(response), response["code"]
    elif request.method == "DELETE":
        try:
            for i in range(len(users_list)):
                if users_list[i]["name"] == name:
                    del users_list[i]
            response = {
                "code": 204,
                "message": "Data Deleted"
            }
        except:
            response = {
                "code": 404,
                "message": "Error"
            }
        return jsonify(response), response["code"]

if __name__ == "__main__":
    app.run(debug=True)