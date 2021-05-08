from flask import request
from flask_restx import Resource, reqparse, fields, marshal_with
from ..services.teacher_service import *


teacher_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'degree_id': fields.Integer
}

class TeacherResource(Resource):
    @marshal_with(teacher_fields)
    def get(self, teacher_id):
        return get_teacher(teacher_id)

    def put(self, teacher_id):
        pass

    def delete(self, teacher_id):
        pass


class TeacherListResource(Resource):
    @marshal_with(teacher_fields)
    def get(self):
        return query_teachers()

    def post(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('email')
        self.parser.add_argument('position_id', type=int)
        self.parser.add_argument('degree_id', type=int)
        args = self.parser.parse_args()
        add_teacher(args)
