from app.models.course import Course
from app.exts import db


def query_courses():
    return Course.query.all()

def get_course(course_id):
    return Course.query.filter_by(id=course_id).first()

def add_course(course_dto):
    course = Course()
    course.name = course_dto.name
    course.description = course_dto.description
    course.ects = course_dto.ects
    course.teacher_id = course_dto.teacher_id
    course.image_url = ''

    db.session.add(course)
    db.session.commit()

def update_course(course_id, course_dto):
    Course.query.filter_by(id=course_id).update(course_dto)
    db.session.commit()

def delete_course(course_id):
    Course.query.filter_by(id=course_id).delete()
    db.session.commit()
