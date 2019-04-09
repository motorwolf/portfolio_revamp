import os
from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def render_homepage():
    return render_template('index.html')

@app.route("/projects")
def render_projects():
    return render_template('projects.html')

@app.route("/art")
def render_art():
    return render_template('art.html')

@app.route("/me")
def render_about_me():
    return render_template('me.html')

@app.route("/resume")
def render_resume():
    return render_template('resume.html')

@app.route("/work")
def render_work_detail():
    return render_template('work.html')

@app.route("/writing")
def render_writing():
    return render_template('writing.html')

if __name__ == '__main__':
    app.debug=True
    app.run(port=5000, host='0.0.0.0')

