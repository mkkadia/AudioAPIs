from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from JSONValidator import SongJSONValidator


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mrugeshroot@localhost/getybo"
db = SQLAlchemy(app)

from Models import Song, Podcast, Audiobook


@app.route("/api/create/<file_type>", methods=["POST"])
def upload_audio(file_type):

    json_validation = SongJSONValidator().validate(request.json)

    if json_validation:
        return jsonify({"message": "Invalid Payload"}), 400

    return jsonify({"message": "Success"}), 200


@app.route("/api/update/<file_type>", methods=["PUT"])
def update_audio(file_type):

    json_validation = SongJSONValidator().validate(request.json)

    if json_validation:
        return jsonify({"message": "Invalid Payload"}), 400

    return jsonify({"message": "Success"}), 200


@app.route("/api/delete/<file_type>", methods=["DELETE"])
def delete_audio(file_type):

    id_ = request.args.get("id")

    return jsonify({"message": "Success"}), 200


@app.route("/api/get/<file_type>", methods=["GET"])
def get_audio(file_type):

    id_ = request.args.get("id")

    return jsonify({"message": "Success"}), 200


if __name__ == "__main__":
    app.run()
