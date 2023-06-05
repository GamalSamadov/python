from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
driver.maximize_window()

languages = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[2]')
native_speekers = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[3]')
percentage_of_world_population = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[4]')
del languages[100]


resualt = []
for i in range(len(languages)):
    dict_data = {'languages' : languages[i].text,
                 'native_speekers' : native_speekers[i].text,
                 'percentage_of_world_population' : percentage_of_world_population[i].text}
    resualt.append(dict_data)

df_data = pd.DataFrame(resualt)

df_data.to_excel('wepScraping.xlsx', index_label=False)

