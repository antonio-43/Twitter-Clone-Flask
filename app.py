from flask import Flask, render_template, url_for, redirect, request
from models import create_post, get_post

app = Flask(__name__)
"""
@app.route('/')
def index():
    return render_template('index.html')
"""

@app.route('/', methods=['GET', ])
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        global posts
        username = request.form.get('username')
        post_content = request.form.get('post_content')
        create_post(username, post_content)

    posts = get_post()

    return render_template('home.html', post=posts)

if __name__ == '__main__':
    app.run()
