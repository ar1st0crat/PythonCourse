from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def seed_db():
    
    from .models.teacher import Position, Degree, Teacher

    pos1 = Position()
    pos1.name = 'Профессор'
    pos2 = Position()
    pos2.name = 'Доцент'
    pos3 = Position()
    pos3.name = 'Старший преподаватель'
    db.session.add(pos1)
    db.session.add(pos2)
    db.session.add(pos3)

    deg1 = Degree()
    deg1.name = 'Доктор технических наук, д.т.н.'
    deg2 = Degree()
    deg2.name = 'Кандидат технических наук, к.т.н.'
    db.session.add(deg1)
    db.session.add(deg2)

    t = Teacher()
    t.name = 'Шарий Тимофей Вячеславович'
    t.email = 'art1st.prog@gmail.com'
    t.degree_id = 2
    t.position_id = 2
    db.session.add(t)

    db.session.commit()
