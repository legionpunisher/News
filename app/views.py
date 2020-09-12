from flask import render_template
from app import app

#Views
@app.route ('/')
def index():
    
    title = 'Homep welcome to the best news website online'
    return render_template('index.html',title = title)

@app.route ('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id = news_id)
