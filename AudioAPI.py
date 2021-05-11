from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify

from JSONValidator import payload_validation
from Models import Song, Podcast, Audiobook


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mrugeshroot@localhost/getybo"
db = SQLAlchemy(app)


@app.route("/api/<audioFileType>", methods=["POST"])
@payload_validation
def upload_audio(audioFileType):
    try:
        json_data = request.json

        if audioFileType == "Song":
            obj = Song(title=json_data["title"], duration=json_data["duration"])
        elif audioFileType == "Podcast":
            obj = Podcast(title=json_data["title"], duration=json_data["duration"], host=json_data["host"], participants=json_data["participants"])
        elif audioFileType == "Audiobook":
            obj = Audiobook(title=json_data["title"], duration=json_data["duration"], author=json_data["author"], narrator=json_data["narrator"])
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        db.session.add(obj)
        db.session.commit()

        return jsonify({"message": "Success"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/<audioFileType>/<audioFileID>", methods=["PUT"])
@payload_validation
def update_audio(audioFileType):
    json_data = request.json

    return jsonify({"message": "Success"}), 200


@app.route("/api/<audioFileType>/<audioFileID>", methods=["DELETE"])
def delete_audio(audioFileType, audioFileID):
    try:
        if audioFileType == "Song":
            model = Song
        elif audioFileType == "Podcast":
            model = Podcast
        elif audioFileType == "Audiobook":
            model = Audiobook
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        data = db.session.query(model).filter(model.id == audioFileID).delete()
        print(data)
        db.session.commit()

        return jsonify({"message": "Success"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/<audioFileType>/<audioFileID>", methods=["GET"])
def get_audio(audioFileType, audioFileID):
    try:
        print(audioFileID)

        if audioFileType == "Song":
            model = Song
        elif audioFileType == "Podcast":
            model = Podcast
        elif audioFileType == "Audiobook":
            model = Audiobook
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        data = db.session.query(model).filter(model.id == audioFileID).one_or_none()

        print(data)

        return jsonify({"data": data if data else {}}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run()
