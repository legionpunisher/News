from flask import render_template
from app import app
from newsapi import NewsApiClient
from .request import get_sources,get_source

#Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular movie
    source = get_sources()       
    # print(source)
    title = 'THE BEST NEWS SITE IN THE WORLD'
    return render_template('index.html', title = title,sources=source)
@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )