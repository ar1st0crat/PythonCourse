from app.models.topic import Topic
from app.exts import db


def query_topics(course_id):
    return Topic.query.filter_by(course_id=course_id).all()

def get_topic(topic_id):
    return Topic.query.filter_by(id=topic_id).first()

def add_topic(course_id, topic_dto):
    topic = Topic()
    topic.no = topic_dto.no
    topic.name = topic_dto.name
    topic.description = topic_dto.description
    topic.course_id = course_id

    db.session.add(topic)
    db.session.flush()
    db.session.commit()
    #db.session.refresh(topic)

    return topic

def update_topic(topic_id, topic_dto):
    Topic.query.filter_by(id=topic_id).update(topic_dto)
    db.session.commit()

def delete_topic(topic_id):
    Topic.query.filter_by(id=topic_id).delete()
    db.session.commit()
