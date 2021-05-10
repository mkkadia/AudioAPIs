from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class SongJSONValidator(Schema):
    title = fields.String(data_key="title", required=True, validate=Length(max=100))
    duration = fields.Integer(data_key="duration", required=True, validate=Range(min=1))


class PodcastJSONValidator(Schema):
    title = fields.String(data_key="title", required=True, validate=Length(max=100))
    host = fields.String(data_key="host", required=True, validate=Length(max=100))
    participants = fields.List(
        fields.String(validate=Length(max=100)),
        data_key="participants",
        required=False,
        validate=Length(max=10)
    )


class AudiobookJSONValidator(Schema):
    title = fields.String(data_key="title", required=True, validate=Length(max=100))
    narrator = fields.String(data_key="narrator", required=True)

