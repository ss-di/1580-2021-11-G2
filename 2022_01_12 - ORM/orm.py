from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db' # привязываем базу данных
db = SQLAlchemy(app) # создаем объект SQLAlchemy

from datetime import datetime

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    lesson_amount = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'{self.id} {self.name}'

class Streams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'),
        nullable=False)
    course = db.relationship('Courses',
        backref=db.backref('streams', lazy=False))
    
    def __repr__(self):
        return f'course number {self.number}'
        
#db.create_all()

'''course = Courses(name="SQLAlchemy basics2", lesson_amount=4)
st = Streams(number=45, start_date=datetime.now(), course=course)
db.session.add(course)
db.session.add(st)
db.session.commit()
'''

print(Courses.query.all()[0].streams[0].start_date)


