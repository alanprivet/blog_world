from flask import Flask, render_template, url_for

blog = Flask(__name__);

@blog.route('/')
def index():
	return render_template("index.html", style = url_for('static', filename='style.css'))







