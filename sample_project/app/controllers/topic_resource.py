from flask import request
from flask_restx import Resource, reqparse, fields, marshal_with
from ..services.topic_service import *


synopsis_fields = {
    'id': fields.Integer,
    'url': fields.String(attribute='file_url'),
    'text': fields.String,
    'createdAt': fields.DateTime(attribute='created_at')
}

topic_fields = {
    'id': fields.Integer,
    'no': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'course_id': fields.Integer,
    'synopses': fields.List(fields.Nested(synopsis_fields), attribute="synopses")
}


class TopicResource(Resource):
    @marshal_with(topic_fields)
    def get(self, topic_id):
        return get_topic(topic_id)

    def put(self, topic_id):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('description')
        self.parser.add_argument('no', type=int)
        self.parser.add_argument('course_id', type=int)
        args = self.parser.parse_args()
        update_topic(topic_id, args)

    def delete(self, topic_id):
        delete_topic(topic_id)


class TopicListResource(Resource):
    @marshal_with(topic_fields)
    def get(self, course_id):
        return query_topics(course_id)

    @marshal_with(topic_fields)
    def post(self, course_id):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('description')
        self.parser.add_argument('no', type=int)
        self.parser.add_argument('course_id', type=int)
        args = self.parser.parse_args()
        return add_topic(course_id, args)
