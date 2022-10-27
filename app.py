import logging
import os
from dataclasses import dataclass

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# LOGGING CONFIG


@app.before_first_request
def before_first_request():
    app.logger.setLevel(logging.DEBUG)


@app.before_request
def log_request_info():
    app.logger.debug("Headers: %s", request.headers)
    app.logger.debug("Body: %s", request.get_data())


# DB CONFIG

db = SQLAlchemy()

host = os.getenv("POSTGRES_HOST")
user = os.getenv("POSTGRES_USER")
pswd = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql+psycopg2://{user}:{pswd}@{host}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# DATA MODEL


@dataclass
class Person(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String)


db.init_app(app)

# SEEDING THE DB


def seed():
    db.session.add_all(
        [
            Person(name="Alice"),
            Person(name="Bob"),
            Person(name="Charlie"),
            Person(name="Dave"),
            Person(name="Eve"),
            Person(name="Frank"),
            Person(name="Grace"),
        ]
    )
    db.session.commit()


with app.app_context():
    db.drop_all()
    db.create_all()
    seed()


# PERSON CRUD


@app.route("/person", methods=["GET", "POST"])
@app.route("/person/<person_id>", methods=["GET", "PUT", "DELETE"])
def person_endpoint(person_id=None):
    if person_id is not None:
        person = Person.query.get(person_id)

    if request.method == "GET":
        if person_id is not None:
            return jsonify(person)
        else:
            return jsonify(Person.query.all())
    elif request.method == "POST":
        person = Person(name=request.get_json()["name"])
        db.session.add_all([person])
        db.session.commit()
        return jsonify(person), 201
    elif request.method == "PUT":
        person.name = request.get_json()["name"]
        db.session.add_all([person])
        db.session.commit()
        return jsonify(person)
    else:
        db.session.delete(person)
        db.session.commit()
        return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
