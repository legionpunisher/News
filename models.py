class Source:
    """
    sources class to define Source Objects
    """
    
    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self. url = url
        self.category = category
        self.language = language
        self.country = country
        
class Headlines:
    '''
    Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
        
class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title

class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
