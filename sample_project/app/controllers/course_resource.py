from flask import request
from flask_restx import Resource, reqparse, fields, marshal_with
from ..services.course_service import *
from .teacher_resource import teacher_fields


course_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'ects': fields.Float,
    'image_url': fields.String,
    'teacher': fields.Nested(teacher_fields)
}

class CourseResource(Resource):

    @marshal_with(course_fields)
    def get(self, course_id):
        return get_course(course_id)

    def put(self, course_id):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('description')
        self.parser.add_argument('ects', type=float)
        self.parser.add_argument('image_url')
        self.parser.add_argument('teacher_id', type=int)
        args = self.parser.parse_args()
        update_course(course_id, args)

    def delete(self, course_id):
        delete_course(course_id)


class CourseListResource(Resource):
    @marshal_with(course_fields)
    def get(self):
        return query_courses()

    def post(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('name')
        self.parser.add_argument('description')
        self.parser.add_argument('ects', type=float)
        self.parser.add_argument('image_url')
        self.parser.add_argument('teacher_id', type=int)
        args = self.parser.parse_args()
        add_course(args)
