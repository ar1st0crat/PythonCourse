from .entity import Entity
from ..exts import db


class Topic(Entity):
    __tablename__ = 'topics'

    no = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    synopses = db.relationship('Synopsis', backref='topics')
