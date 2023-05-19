from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    # retrieve blog content
    # blog_content = ...
    return render_template('blog.html', content=blog_content)
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
