from flask import render_template, url_for, flash, redirect, request
from animalmagicblog import app, db, bcrypt
from animalmagicblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from animalmagicblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Dummy Data for testing
posts = [
    {
        'author': 'James Drysdale', 
        'title': 'Feeding birds',
        'content': 'Why you are probably feeding birds to death and how to feed them the right way.',
        'date_posted': 'September 1st 2020'
    },
    {
        'author': 'James Drysdale', 
        'title': 'Dog Training 101: Recall',
        'content': 'How to get your dog to return to you on your command.',
        'date_posted': 'September 11th 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts, title='Blog')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # Hashes the password to secure it
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has now been created, and you are now able to sign in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home')) #ternary
        else: 
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    form = UpdateAccountForm()
    image_file = (url_for('static', filename='profile_pics/' + current_user.image_file))
    return render_template('account.html', title='Account', 
                            image_file=image_file, form=form)