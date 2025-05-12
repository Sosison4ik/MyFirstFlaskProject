from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Vlad'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'Beautiful day in Portland'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Aengers movie is so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)
