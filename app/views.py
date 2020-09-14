from flask import render_template
from app import app
from newsapi import NewsApiClient
from .request import get_sources

#Views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular movie
    source = get_sources()   
    # print(source)
    title = 'THE BEST NEWS SITE IN THE WORLD'
    return render_template('index.html', title = title,sources=source)
