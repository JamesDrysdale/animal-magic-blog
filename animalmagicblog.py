from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1a394f30fa58662edd8941ed9f8c21e2'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password': #dummy data for testing
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)