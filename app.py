from flask import Flask
from models import db, School, Class, Student, Teacher
from routes import classesApi, schoolsApi, teachersApi, studentsApi, index

app = Flask(__name__)
app.register_blueprint(classesApi)
app.register_blueprint(schoolsApi)
app.register_blueprint(teachersApi)
app.register_blueprint(studentsApi)
app.register_blueprint(index)
db.init_app(app)

with app.app_context():
    db.create_all()
    school = School(name='middle50', address='address')
    db.session.add(school)
    db.session.commit()
    group = Class(name='1A', school_id=school.id)
    db.session.add(group)
    db.session.commit()
    db.session.add(Student(name='Vasya', class_id=group.id))
    db.session.add(Teacher(name='Irina', class_id=group.id, subject='Math'))
    db.session.commit()
if __name__ == "__main__":
    app.run()