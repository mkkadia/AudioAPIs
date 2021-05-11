from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from JSONValidatorModels import SongJSONValidator


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mrugeshroot@localhost/getybo"
db = SQLAlchemy(app)

from Models import Song, Podcast, Audiobook


@app.route("/api/<str:audioFileType>", methods=["POST"])
def upload_audio(file_type):
    json_data = request.json

    if json_data == "Song":
        json_validation = SongJSONValidator().validate(json_data)

    elif json_data == "Podcast":
        json_validation = SongJSONValidator().validate(json_data)

    elif json_data == "Audiobook":
        json_validation = SongJSONValidator().validate(json_data)

    else:
        return jsonify({"message": "Invalid Audio Type"}), 400

    if json_validation:
        return jsonify({"message": "Invalid Payload"}), 400

    return jsonify({"message": "Success"}), 200


@app.route("/api/<str:audioFileType>/<int:audioFileID>", methods=["PUT"])
def update_audio(file_type):
    json_data = request.json

    if json_data == "Song":
        json_validation = SongJSONValidator().validate(json_data)

    elif json_data == "Podcast":
        json_validation = SongJSONValidator().validate(json_data)

    elif json_data == "Audiobook":
        json_validation = SongJSONValidator().validate(json_data)

    else:
        return jsonify({"message": "Invalid Audio Type"}), 400

    if json_validation:
        return jsonify({"message": "Invalid Payload"}), 400

    return jsonify({"message": "Success"}), 200


@app.route("/api/<str:audioFileType>/<int:audioFileID>", methods=["DELETE"])
def delete_audio(file_type):

    id_ = request.args.get("id")

    return jsonify({"message": "Success"}), 200


@app.route("/api/<str:audioFileType>/<int:audioFileID>", methods=["GET"])
def get_audio(file_type):

    id_ = request.args.get("id")

    return jsonify({"message": "Success"}), 200


if __name__ == "__main__":
    app.run()
