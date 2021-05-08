from .entity import Entity
from ..exts import db


class Course(Entity):
    __tablename__ = 'courses'

    name = db.Column(db.String)
    description = db.Column(db.String)
    ects = db.Column(db.Float)
    image_url = db.Column(db.String)
    
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship("Teacher", back_populates="courses")

    topics = db.relationship('Topic', backref='courses')
