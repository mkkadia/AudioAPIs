from functools import wraps
from flask import request, jsonify

from JSONValidatorModels import SongJSONValidator, PodcastJSONValidator, AudiobookJSONValidator


def payload_validation(function):

    @wraps(function)
    def wrap_function(*args, **kwargs):
        try:
            audio_file_type = kwargs["audioFileType"]
            json_data = request.json

            if audio_file_type == "Song":
                json_validation = SongJSONValidator().validate(json_data)

            elif audio_file_type == "Podcast":
                json_validation = PodcastJSONValidator().validate(json_data)

            elif audio_file_type == "Audiobook":
                json_validation = AudiobookJSONValidator().validate(json_data)

            else:
                return jsonify({"message": "Invalid Audio File Type"}), 400

            if json_validation:
                return jsonify({"message": "Invalid Payload"}), 400

        except Exception:
            return jsonify({"message": "Internal Server Error"}), 500
        return function(*args, **kwargs)

    return wrap_function
