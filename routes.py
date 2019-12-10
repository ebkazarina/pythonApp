from flask import Blueprint, jsonify

from models import db, Class, School, Student, Teacher


index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
@index.route('/index')
def get_index():
    return '''
    <html>
    <title>
        best REST
    </title>
    <body>
        <h3>Api:</h3>
        <a href="./api/schools">Schools</a>
        <a href="./api/classes">Classes</a>
        <a href="./api/students">Students</a>
        <a href="./api/teachers">Teacher</a>        
    </body>
    </html>'''


schoolsApi = Blueprint('schoolsApi', __name__, url_prefix='/api/schools')


@schoolsApi.route('/')
def get_schools():
    return jsonify([(lambda school:school.json()) (school) for school in School.query.all()])


@schoolsApi.route('/id/<int:id>')
def get_school(id):
    school = School.query.get(id)
    return jsonify(school.json()) if school else ''


@schoolsApi.route('/name/<string:name>/address/<string:address>')
def put_school(name, address):
    school = School(name=name, address=address)
    db.session.add(school)
    db.session.commit()
    return jsonify(school.json()) if school else ''


classesApi = Blueprint('classesApi', __name__, url_prefix='/api/classes')


@classesApi.route('/')
def get_classes():
    return jsonify([(lambda group:group.json()) (group) for group in Class.query.all()])


@classesApi.route('/id/<int:id>')
def get_class(id):
    group = Class.query.get(id)
    return jsonify(group.json()) if group else ''


@classesApi.route('/name/<string:name>/school_id/<int:school_id>')
def put_class(name, school_id):
    group = Class(name=name, school_id=school_id)
    db.session.add(group)
    db.session.commit()
    return jsonify(group.json()) if group else ''


    return jsonify(school.json()) if school else ''


studentsApi = Blueprint('studentsApi', __name__, url_prefix='/api/students')


@studentsApi.route('/')
def get_classes():
    return jsonify([(lambda student:student.json()) (student) for student in Student.query.all()])


@studentsApi.route('/id/<int:id>')
def get_class(id):
    student = Student.query.get(id)
    return jsonify(student.json()) if student else ''


@studentsApi.route('/name/<string:name>/class_id/<int:class_id>')
def put_class(name, class_id):
    student = Student(name=name, class_id=class_id)
    db.session.add(student)
    db.session.commit()
    return jsonify(student.json()) if student else ''


teachersApi = Blueprint('teachersApi', __name__, url_prefix='/api/teachers')


@teachersApi.route('/')
def get_classes():
    return jsonify([(lambda teacher:teacher.json()) (teacher) for teacher in Teacher.query.all()])


@teachersApi.route('/id/<int:id>')
def get_class(id):
    teacher = Teacher.query.get(id)
    return jsonify(teacher.json()) if teacher else ''


@teachersApi.route('/name/<string:name>/class_id/<int:class_id>')
def put_class(name, class_id):
    teacher = Teacher(name=name, class_id=class_id)
    db.session.add(teacher)
    db.session.commit()
    return jsonify(teacher.json()) if teacher else ''