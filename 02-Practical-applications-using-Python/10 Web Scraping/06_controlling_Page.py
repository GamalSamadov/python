"""
Selenium special keys:
https://selenium-python.readthedocs.io/api.html?highlight=keys#module-selenium.webdriver.common.keys

The click() function is used to click on the element.
The send_keys() function sends alert keys.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

try:
    # Click Operator
    # elem = browser.find_element(By.CSS_SELECTOR, '#ca-viewsource > a')
    # elem.click()
    # time.sleep(5)

    # search operator
    # elem = browser.find_element(By.CSS_SELECTOR, '#searchInput')
    # elem.send_keys('Python')
    # time.sleep(3)
    # button = browser.find_element(By.CSS_SELECTOR, '#searchButton')
    # button.click()
    # time.sleep(5)

    # scroll operator
    time.sleep(3)
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    htmlElem.send_keys(Keys.END)
    time.sleep(3)
    htmlElem.send_keys(Keys.HOME)
    time.sleep(3)


except:
    print('Was not able to find as element with that name.')