from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return render_template('blog.html', posts=posts)