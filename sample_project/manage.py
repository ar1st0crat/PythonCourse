import os
import unittest
from app.models.synopsis import Synopsis
from app.models.topic import Topic
from app.models.course import Course
from app.models.teacher import Position, Degree, Teacher
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.api import create_app
from app.exts import db, seed_db


app = create_app('dev') 
# app = create_app(os.getenv('AUTOSYNAPSES_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()

@manager.command
def seed():
    seed_db()

@manager.command
def test():
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
