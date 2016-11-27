__author__ = 'Patrick'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from django.test import TestCase, Client
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# capabilities = DesiredCapabilities.CHROME
# browser = webdriver.Remote(command_executor='http://192.168.99.100:4444/wd/hub', desired_capabilities=capabilities)
# browser.get("http://www.python.org")
# if "Python" in browser.title:
#     print("Python is in the browser title!")
# else:
#     print("LOOOOOOOSER")
#
# elem = browser.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in browser.page_source
# browser.close()
# print("HELLO MADE IT HERE LUV")
# browser.quit()

class WebTestCase(TestCase):
    def setUp(self):
        pass
    def test_success_response(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor='http://192.168.99.100:4444/wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get("http://www.python.org")
        title = str(browser.title)
        print(title)
        self.assertIn('Python', title)

    # Test correct website
    def test_sugar_url(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor='http://192.168.99.100:4444/wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get("http://192.168.99.100:8001/")
        title = str(browser.title)
        print(title)
        self.assertIn('SugarSugar', title)

    # Test login
    def test_login(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor='http://192.168.99.100:4444/wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get("http://192.168.99.100:8001/")

        browser.find_element_by_xpath('//a[@class = "btn btn-info"]').click()
        username_entry = browser.find_element_by_id('id_username')
        password_entry= browser.find_element_by_id('id_password')
        username_entry.send_keys('Pat')
        password_entry.send_keys('password')
        browser.find_element_by_xpath('//input[@value = "Submit"]').click()

        logout = browser.find_element_by_xpath('//a[@href="/logout"]')
        self.assertNotEquals(logout, None)

    
    def tearDown(self):
        pass
