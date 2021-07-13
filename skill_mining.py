import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

DF = pd.read_csv('/Users/yuyara/Documents/Coding/python/Data_pipeline/Career_skill/Data/job_data.csv')
links = list(DF['Link'])
options = Options()
options.headless = False
driver = webdriver.Chrome(options=options, executable_path="/Users/yuyara/Downloads/chromedriver 2") 



bunch_texts = []
for url in links:
    driver.get(url)
    try:
        main = driver.find_element_by_id("main-content")
        texts = main.find_element_by_class_name('show-more-less-html__markup')
        text = texts.get_attribute('innerHTML')
        bunch_texts.append(text)
    except:
        bunch_texts.append('Null')


