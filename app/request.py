from app import app
import urllib.request,json
from newsapi import NewsApiClient
from .models import source

Source = source.Source
# Getting api key
api_key = app.config['SOURCE_API_KEY']

#Getting the news base url
base_url = app.config["SOURCE_API_BASE_URL"]

def get_sources():
    
    get_sources_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results
def process_results(source_list):
    '''
    Function  that processes the news source and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url_path')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

    if id:
        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)

    return source_results
