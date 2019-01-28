from flask import Flask, request, jsonify, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.\\foo.db'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False,)

    def __repr__(self):
        return self.username


@app.route("/users", methods=["POST"])
def users_create():
    request_data = request.get_json()
    user = User(**request_data)
    db.session.add(user)
    db.session.commit()
    return Response(response="ok", status=201)


@app.route("/users", methods=["GET"])
def users_retrieve():
    if len(request.args) > 0:
        users = User.query.filter_by(**request.args)
    else:
        users = User.query.all()

    users_response = [dict(id=user.id, username=user.username,
                           email=user.email) for user in users]
    return jsonify(users_response), 200


@app.route("/users/<id>", methods=["GET"])
def user_get(id):
    user = User.query.get(id)
    if user is None:
        return Response("usuario no hallado", status=404)
    return jsonify(dict(id=user.id, username=user.username, email=user.email)), 200


@app.route("/users/<id>", methods=["PUT"])
def users_update(id):
    user = User.query.get(id)
    incoming_user = request.get_json()

    if user is None or incoming_user is None:
        return Response(response="No hallado", status=404)

    user.username = incoming_user.get("username")
    user.email = incoming_user.get("email")
    db.session.commit()

    return "ok", 200


@app.route("/users/<id>", methods=["DELETE"])
def users_delete(id):
    user = User.query.get(id)
    if user is None:
        return NotFound.description, 404

    db.session.delete(user)
    db.session.commit()
    return Response(status=204)


if __name__ == "__main__":
    # db.create_all()
    app.run(port=8085, debug=True)
