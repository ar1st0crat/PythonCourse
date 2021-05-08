from app.models.teacher import Teacher
from app.exts import db


def query_teachers():
    return Teacher.query.all()

def get_teacher(teacher_id):
    return Teacher.query.filter_by(id=teacher_id).first()

def add_teacher(teacher_dto):
    teacher = Teacher()
    teacher.name = teacher_dto.name
    teacher.email = teacher_dto.email
    teacher.degree_id = teacher_dto.degree_id
    teacher.position_id = teacher_dto.position_id

    db.session.add(teacher)
    db.session.commit()

def update_teacher(teacher_id):
    pass
