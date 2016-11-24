__author__ = 'Patrick'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

# capabilities = DesiredCapabilities.CHROME
# # This is a web driver capability that Firefox 48 and higher use by default. Since our container uses Firefox 47, let's disable it.
# # capabilities["marionette"] = False
#
# # Wire it all up. Be sure to use the port for _your_ container found earlier using docker ps
# # webdriver driver = new webdriver(new URL("http://localhost:4444/wd/hub"), DesiredCapabilities.firefox());
# browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
# url = 'http://192.168.99.100:8001/'
# browser.get(url)
# print("HELLO MADE IT HERE LUV")
# browser.quit()

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()