""" Models for the app """

## imports
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
## classes

class User(db.Model):
    """ A user """
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name1 = db.Column(db.String, nullable=True)
    name2 = db.Column(db.String, nullable=True)
    # bio = db.Column(db.Text, nullable=True)
    # interests = db.Column(db.Text,nullable=True)
    # dislikes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Like(db.Model):

    __tablename__ = "likes"

    like_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    yelp_id = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Like user={self.user_id} venue={self.yelp_id}>"

def connect_to_db(flask_app, db_uri="postgresql:///daters", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    db.create_all()
    print("Connected to the db!")



if __name__ == "__main__":
    from server import app

    connect_to_db(app)