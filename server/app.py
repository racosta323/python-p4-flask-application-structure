#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# app.route is an instance method that modifies app; allows us to define a route
# registers index() to the applicationo instance
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

#anything in between <> will be passed to the app.route decorator as a parameter
#add validity by using "string"
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)