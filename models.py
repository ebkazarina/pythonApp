from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    address = db.Column(db.String(120))
    def json(self):
        return {'id': self.id, 'name': self.name, 'address': self.address}

class Class(db.Model):
    __tablename__='classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    school_id = db.Column(db.Integer, ForeignKey('schools.id'))
    school = relationship('School')
    def json(self):
        return {'id': self.id, 'name': self.name, 'school': self.school.json()}

class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    class_id = db.Column(db.Integer, ForeignKey('classes.id'))
    group = relationship('Class')
    def json(self):
        return {'id': self.id, 'name': self.name, 'class': self.group.json()}

class Teacher(db.Model):
    __tablename__='teachers'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    subject = db.Column(db.String(120))
    class_id = db.Column(db.Integer, ForeignKey('classes.id'))
    group = relationship('Class')
    def json(self):
        return {'id': self.id, 'name': self.name, 'subject': self.subject, 'class': self.group.json()}