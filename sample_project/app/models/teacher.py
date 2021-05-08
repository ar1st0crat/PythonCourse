from .entity import Entity
from ..exts import db


class Position(Entity):
    __tablename__ = 'positions'

    name = db.Column(db.String)


class Degree(Entity):
    __tablename__ = 'degrees'

    name = db.Column(db.String)


class Teacher(Entity):
    __tablename__ = 'teachers'

    name = db.Column(db.String)
    email = db.Column(db.String)
    degree_id = db.Column(db.Integer, db.ForeignKey('degrees.id'))
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'))

    courses = db.relationship('Course', backref='teachers')
