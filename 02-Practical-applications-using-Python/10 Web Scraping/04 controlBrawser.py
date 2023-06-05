"""
Download Selenium with Python library:
pip install selenium

Download chromedriver-binary library:
pip install chromedriver-binary-auto

Download geckodriver-autoinstaller library:
pip install chromedriver-binary-auto

link to download geckdriver from GitHub:
https://github.com/mozilla/geckodriver/releases

"""

from selenium import webdriver
import  chromedriver_binary

# Google Chrome
browser = webdriver.Chrome()
browser.get('https://www.google.com.ua/?hl=ru')
