import unittest
from models import source
Source = source.Source


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
        
if __name__ == '__main__':
    unittest.main()
