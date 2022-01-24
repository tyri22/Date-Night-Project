""" CRUD functions """

from model import db, User, Like, connect_to_db

def create_user(email, password, name1, name2):

    user = User(email=email, password=password, name1=name1, name2=name2)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


def add_like(user_id, yelp_id):

    like = Like(user_id=user_id, yelp_id=yelp_id)
    
    db.session.add(like)
    db.session.commit()

    return like

def get_like_by_yelp_id(yelp_id):

    return Like.query.filter(Like.yelp_id == yelp_id).all()


if __name__ == "__main__":
    from server import app

    connect_to_db(app)