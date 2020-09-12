from flask import render_template
from app import app
from .request import get_news

#Views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news category
    news_category = get_news('category')
    print(news_category)
    title = 'THE BEST NEWS SITE IN THE WORLD'
    return render_template('index.html', title = title,category = news_category)
