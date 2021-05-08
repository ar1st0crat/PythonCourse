import werkzeug
from flask import request
from flask_restx import Resource, reqparse, fields, marshal_with
from ..services.synopsis_service import *


class SynopsisPdfResource(Resource):

    def post(self, topic_id: int):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        pdf_file = args['file']

        full_text = extract_pdf(pdf_file, topic_id)

        return { 'message': full_text }


class SynopsisPptxResource(Resource):

    def post(self, topic_id: int):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        pptx_file = args['file']

        full_text = extract_pptx(pptx_file, topic_id)

        return { 'message': full_text }
