from datetime import datetime
from email.mime import application
from random import randint
from unittest import result
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://root:root@localhost:5432/store"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    age = db.Column(db.Integer)
    email = db.Column(db.String(200))
    job = db.Column(db.String(100))
    applications = db.relationship('Application') 
    
    def __init__(self, firstname, lastname, age, email, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.job = job
    
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    lastconnection = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, appname, username, lastconnection):
        self.appname = appname
        self.username = username
        self.lastconnection = lastconnection


from faker import Faker
fake = Faker()
def populate_tables():
    for i in range(0,100):
        #création des fausses
        new_user = users(fake.first_name(),fake.last_name(),randint(20,60), fake.email(), fake.job())
        apps = ["Facebook", "Twitter", "Intagram", "Linkedin"]
        nb_app = 2
        applications = []
        for app_n in range(0, nb_app):
            app = Application(apps[app_n], fake.user_name(), datetime.now())
            applications.append(app)
        new_user.applications = applications
        db.session.add(new_user)
    db.session.commit()



@app.route("/user", methods = ["POST", "GET"])
def user():
    if request.method == "GET":
        result = users.query.all()
        user_list = []
        for row in result:
            print(row)
            user = {
                "id": row.id,
                "firstname" : row.firstname,
                "lastname": row.lastname,
                "age": row.age,
                "email": row.email,
                "job": row.job
            }
            user_list.append(user)
        return jsonify(user_list)


if __name__=='__main__':
    db.drop_all()
    db.create_all()
    populate_tables()
    app.run(host="0.0.0.0", port=8080, debug=True)



