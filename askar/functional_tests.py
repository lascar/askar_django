from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
  
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)
    self.browser.maximize_window()

  def tearDown(self):
    self.browser.quit()

  # on the home page
  def testroot_page_prepare_client(self):
    self.browser.get('http://localhost:8000')

    # the title is set
    self.assertIn('Askar', self.browser.title)
    
    self.fail('Finish the test')

if __name__ == '__main__':
  unittest.main(warnings='ignore')
