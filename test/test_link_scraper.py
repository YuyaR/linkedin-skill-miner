import unittest
from project import link_scraper


class LinkScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.input = link_scraper.LinkScraper(
            'camera man', 'United Kingdom', '/Users/yuyara/Downloads/chromedriver 2')

    def test_process(self):
        expected_value = 'camera%20man'
        actual_value = self.input.job  # the job/location should be processed already
        self.assertEqual(expected_value, actual_value)

        with self.assertRaises(ValueError) as err:
            link_scraper.LinkScraper(
                'conservation', 'United.States', '/Users/yuyara/Downloads/chromedriver 2')
            # special character '.' not accepted
    
    def test_scraper(self):
        with self.assertRaises(ValueError) as err:
            example = link_scraper.LinkScraper(
                'ffwenie', 'vnoegniw', '/Users/yuyara/Downloads/chromedriver 2')
            example.scrape()
            #most coherent words would still return results. But in case of absolute nonsense or simply
            #extremely esoteric/unpopular jobs should it not find any jobs on Linkedin it would return 
            #this error
        
    def test_driver(self):
        with self.assertRaises(ValueError) as err:
            example = link_scraper.LinkScraper(
                'conservation', 'Japan', '/wrong/path/to/chromedriver')



unittest.main(argv=[''], verbosity=2, exit=False)
