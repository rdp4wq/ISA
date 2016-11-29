__author__ = 'Patrick'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.test import TestCase
from selenium_tests.settings import WEB_URL, SELENIUM_URL
import re

class WebTestCase(TestCase):
    def setUp(self):
        pass

    def test_success_response(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor= SELENIUM_URL + 'wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get("http://www.python.org")
        title = str(browser.title)
        print(title)
        browser.quit()

        self.assertIn('Python', title)

    # Test correct website
    def test_sugar_url(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor= SELENIUM_URL + 'wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get(WEB_URL)
        title = str(browser.title)
        print(title)
        browser.quit()
        self.assertIn('SugarSugar', title)

    # Test login
    def test_login(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor=SELENIUM_URL + 'wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get(WEB_URL)

        # Login
        browser.find_element_by_xpath('//a[@class = "btn btn-info"]').click()
        username_entry = browser.find_element_by_id('id_username')
        password_entry= browser.find_element_by_id('id_password')
        username_entry.send_keys('Pat')
        password_entry.send_keys('password')
        browser.find_element_by_xpath('//input[@value = "Submit"]').click()

        logout = browser.find_element_by_xpath('//a[@href="/logout"]')
        browser.quit()


        self.assertNotEquals(logout, None)

    # Test register
    def test_register(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor=SELENIUM_URL + 'wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get(WEB_URL)

        # Register
        browser.find_element_by_xpath('//a[@href="/register"]').click()
        first_name = browser.find_element_by_id('id_first_name')
        last_name = browser.find_element_by_id('id_last_name')
        email= browser.find_element_by_id('id_email')
        username= browser.find_element_by_id('id_username')
        password_entry= browser.find_element_by_id('id_password')
        date_of_birth= browser.find_element_by_id('id_date_of_birth')
        city= browser.find_element_by_id('id_city')
        income= browser.find_element_by_id('id_income')

        first_name.send_keys('TestFirst')
        last_name.send_keys('TestLast')
        email.send_keys('selenium@selenium.com')
        username.send_keys('Selenia')
        password_entry.send_keys('password')
        date_of_birth.send_keys('1995-03-17')
        city.send_keys('Southside')
        income.send_keys('1234')

        browser.find_element_by_xpath('//input[@value = "Submit"]').click()

        # Test new login
        browser.find_element_by_xpath('//a[@class = "btn btn-info"]').click()
        username_entry = browser.find_element_by_id('id_username')
        password_entry= browser.find_element_by_id('id_password')
        username_entry.send_keys('Selenia')
        password_entry.send_keys('password')
        browser.find_element_by_xpath('//input[@value = "Submit"]').click()

        logout = browser.find_element_by_xpath('//a[@href="/logout"]')
        browser.quit()

        self.assertNotEquals(logout, None)

   # Test create date
    def test_create_date(self):
        capabilities = DesiredCapabilities.CHROME

        browser = webdriver.Remote(command_executor=SELENIUM_URL + 'wd/hub', desired_capabilities=capabilities)

        print("Made it to test")
        browser.get(WEB_URL)

        # Login
        browser.find_element_by_xpath('//a[@class = "btn btn-info"]').click()
        username_entry = browser.find_element_by_id('id_username')
        password_entry= browser.find_element_by_id('id_password')
        username_entry.send_keys('Pat')
        password_entry.send_keys('password')
        browser.find_element_by_xpath('//input[@value = "Submit"]').click()

        # Create date
        browser.find_element_by_xpath('//a[@href = "/dates"]').click()
        browser.find_element_by_xpath('//a[@href = "/create"]').click()
        price = browser.find_element_by_id('id_price')
        description= browser.find_element_by_id('id_description')
        price.send_keys('9876')
        description.send_keys('Selena is looking for some cool picnic outing!')
        browser.find_element_by_xpath('//input[@value = "Submit"]').click()

        # Check if date was created
        browser.find_element_by_xpath('//a[@href = "/dates"]').click()
        src = browser.page_source
        text_found = re.search(r'Selena is looking for some cool picnic outing!', src)
        browser.quit()
        self.assertNotEqual(text_found, None)


    def tearDown(self):
        pass
