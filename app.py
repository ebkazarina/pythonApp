from flask import Flask

app= Flask(__name__)

from models import db, School, Class, Student, Teacher

if __name__ == "__main__":
    app.run()