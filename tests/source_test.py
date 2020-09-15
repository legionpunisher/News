import unittest
from app.models import Source



class SourceTest(unittest.TestCase):
    """
    test class to test the behaviour of the Source class
    """
    def setUp (self):
        """
        set up method that will run before every test
        """
        self.new_source=Source('aljazeera','aljazeeraEnglish','News analysis','http://www.aljazeera.com','general','en','us')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Naila-Jean Meyers and Scott Cacciola','In the 30th professional match between the sisters, Serena defeated Venus in the third round. Rafael Nadal, Juan Martin del Potro and Sloane Stephens also won Friday.','2018-09-01T05:22:26Z','https://www.nytimes.com/2018/08/31/sports/tennis/us-open-results.html','https://static01.nyt.com/images/2018/09/01/sports/01openlive7/01openlive7-facebookJumbo.jpg','US Open 2018 Results')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))
     
if __name__ == '__main__':
    unittest.main()
