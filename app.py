from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder="../templates")
app.secret_key = 'pyva-2026-secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/placements')
def placements():
    return render_template('placements.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you for contacting us!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

# IMPORTANT for Vercel
app.debug = False
