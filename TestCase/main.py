import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import page


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.python.org')

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()
        
    def test_example(self):
        print('test_example')
        assert True

    def not_a_test(self):
        print("This doesn't work as it's not started with test")

    def test_example_2(self):
        print('Test failed...')
        assert False

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
