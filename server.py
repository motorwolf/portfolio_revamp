import os
from flask import Flask
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def render_homepage():
    return "Hello, world!"

@app.route("/projects")
def render_projects():
    return "Projects!"

@app.route("/art")
def render_art():
    return "Art!"

@app.route("/me")
def render_about_me():
    return "Me!"

if __name__ == '__main__':
    app.debug=True
    app.run(port=5000, host='0.0.0.0')

