""" Server for Double Dating App. """

## Imports - flask, requests, redirect, render_template, crud, flash, session
from flask import Flask, flash, request, redirect, render_template, session
import os
import requests
import crud
from model import connect_to_db, User

## App run things
app = Flask(__name__)
app.secret_key = "keyz"
API_KEY = os.environ['YELP_KEY']
## App routes


@app.route("/")
def homepage():
    """ View homepage """

    return render_template("homepage.html")

@app.route("/profile")
def show_profile():
    """ Show user's own profile """

    user = crud.get_user_by_email(session['email'])

    return render_template("profile.html", user=user)

@app.route("/profile/edit")
def edit_profile():
    """ Edit user's own profile """

    user = crud.get_user_by_email(session['email'])

    name1 = request.form.get("name1")
    name2 = request.form.get("name2")
    # bio = request.form.get("bio")
    # interests = request.form.get("interests")
    # dislikes = request.form.get("dislikes")
    
    return render_template("edit-profile.html", user=user)

@app.route("/venues")
def show_venue_form():
    """ Show venue search form """

    return render_template("search-form.html")

@app.route("/venues/search", methods=['POST'])
def find_venues():
    """ Search venues with Yelp """
    
    term = request.values.get('term')
    location = request.values.get('location')
    
    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {
               'term': term,
               'location': location}

    response = requests.get(url, params=payload, headers={'Authorization': 'Bearer '+API_KEY})
   
    data = response.json()
    
    venues = data['businesses']

    return render_template('search-results.html',
                           data=data,
                           results=venues)


@app.route("/businesses/<id>")
def get_venue_details(id):
    """ View details for particular search result """

    url = f'https://api.yelp.com/v3/businesses/{id}'
    

    response = requests.get(url, headers={'Authorization': 'Bearer '+API_KEY})
    
    venue = response.json()

    likes = len(crud.get_like_by_yelp_id(id))
    
    return render_template("venue-details.html", venue=venue, id=id, likes=likes)


@app.route("/register", methods=["POST"])
def register_user():
    """ Create a new user """
    
    email = request.form.get("new-email")
    password = request.form.get("new-password")
    name1 = request.form.get("name1")
    name2 = request.form.get("name2")
    user = crud.get_user_by_email(email)

    if user:
        flash("Email already exists in system, Please use another email and try again.")
    else:
        crud.create_user(email, password, name1, name2)
        flash("Congrats! You've created an account, now you can log in!")

    return redirect("/")

@app.route("/register-page")
def show_register():
    """"Show registration form"""

    return render_template("register.html")

@app.route("/login", methods=["POST"])
def process_login():
    """ Allow user to log in """

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Sorry, your email or password was incorrect.")
        return redirect("/")
    else:
        session["email"] = user.email
        flash("Yay, you're all logged in!")

    return redirect("/profile")


@app.route("/likes", methods=["POST"])
def create_like():
    """ Attach a like to a venue """
    
    yelp_id = request.json.get("venue")
    user = crud.get_user_by_email(session['email'])
    like = crud.add_like(user.user_id , yelp_id)
    like_count = len(crud.get_like_by_yelp_id(yelp_id))

    return str(like_count)
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0")