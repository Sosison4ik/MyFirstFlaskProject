from flask import render_template, flash, redirect, url_for
from app import app 
from flask_login import current_user, login_user
from flask_login import logout_user
import sqlalchemy as sa
from app import db
from app.models import User
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(user.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remeber=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

