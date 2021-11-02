import unittest
from app.models import Headlines, Sources

class HeadlinesTest(unittest.TestCase):
    '''
    Test the Headlines class
    ''' 
    def setUp(self):
        '''
        Set up method Test
        '''
        self.new_headline = Headline('Jodie Comer','Amazing character in killing Eve','Known as the famous Villanelle','www.news.com','www.fandom.com', '2021-11-1-14T00:30:03Z', 'Her role as Molotov Girl was epic...' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,Headline))


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Sources class
    '''
    def setUp(self):
        '''
        Set up method Test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news','www.abcnews.com','general', 'en', 'us' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

