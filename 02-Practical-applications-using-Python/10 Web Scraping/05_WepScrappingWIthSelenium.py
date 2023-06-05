"""
The find_element() function searches for a specific element depending on the strategy you specify.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

try:
    # elem = browser.find_element(By.CSS_SELECTOR, '#sdsmp-tfa > p')
    # print(elem.text)

    elem = browser.find_elements(By.TAG_NAME, 'p')
    print(len(elem))
    print(elem[0].text)
except:
    print('Was not able to find as element with that name.')