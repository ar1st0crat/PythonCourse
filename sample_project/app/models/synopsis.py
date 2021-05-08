from .entity import Entity
from ..exts import db


class Synopsis(Entity):
    __tablename__ = 'synopses'

    file_url = db.Column(db.String)
    text = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
