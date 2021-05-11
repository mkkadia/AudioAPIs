from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify

from JSONValidator import payload_validation
from Models import Song, Podcast, Audiobook


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mrugeshroot@localhost/getybo"
db = SQLAlchemy(app)
logger = app.logger


@app.route("/api/<string:audio_file_type>", methods=["POST"])
@payload_validation
def upload_audio(audio_file_type):
    try:
        json_data = request.json

        if audio_file_type == "Song":
            obj = Song(title=json_data["title"], duration=json_data["duration"])
        elif audio_file_type == "Podcast":
            obj = Podcast(title=json_data["title"], duration=json_data["duration"], host=json_data["host"], participants=json_data["participants"])
        elif audio_file_type == "Audiobook":
            obj = Audiobook(title=json_data["title"], duration=json_data["duration"], author=json_data["author"], narrator=json_data["narrator"])
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        db.session.add(obj)
        db.session.commit()

        return jsonify({"message": "Success"}), 200
    except Exception as e:
        logger.exception(e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/<string:audio_file_type>/<int:audio_file_id>", methods=["PUT"])
@payload_validation
def update_audio(audio_file_type, audio_file_id):
    try:
        json_data = request.json

        if audio_file_type == "Song":
            data = db.session.query(Song).filter(Song.id == audio_file_id).update(json_data)
            db.session.commit()
        elif audio_file_type == "Podcast":
            data = db.session.query(Podcast).filter(Podcast.id == audio_file_id).update(json_data)
            db.session.commit()
        elif audio_file_type == "Audiobook":
            data = db.session.query(Audiobook).filter(Audiobook.id == audio_file_id).update(json_data)
            db.session.commit()
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        return jsonify({"message": "Success"}), 200
    except Exception as e:
        logger.exception(e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/<string:audio_file_type>/<int:audio_file_id>", methods=["DELETE"])
def delete_audio(audio_file_type, audio_file_id):
    try:
        if audio_file_type == "Song":
            model = Song
        elif audio_file_type == "Podcast":
            model = Podcast
        elif audio_file_type == "Audiobook":
            model = Audiobook
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        data = db.session.query(model).filter(model.id == audio_file_id).delete()
        db.session.commit()

        return jsonify({"message": "Success"}), 200
    except Exception as e:
        logger.exception(e)
        return jsonify({"message": "Internal Server Error"}), 500


@app.route("/api/<string:audio_file_type>/<int:audio_file_id>", methods=["GET"])
def get_audio(audio_file_type, audio_file_id):
    try:
        logger.debug("ok")
        if audio_file_type == "Song":
            model = Song
        elif audio_file_type == "Podcast":
            model = Podcast
        elif audio_file_type == "Audiobook":
            model = Audiobook
        else:
            return jsonify({"message": "Invalid Audio File Type"}), 400

        data = db.session.query(model).filter(model.id == audio_file_id).one_or_none()

        return jsonify(data), 200
    except Exception as e:
        logger.exception(e)
        return jsonify({"message": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
