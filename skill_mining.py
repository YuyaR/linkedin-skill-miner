import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import fnmatch

DF = pd.read_csv('/Users/yuyara/Documents/Coding/python/Data_pipeline/Career_skill/Data/job_data.csv')
links = list(DF['Link'])
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path="/Users/yuyara/Downloads/chromedriver 2") 

bullets = []
for url in links:
    driver.get(url)
    try:
        # main = driver.find_element_by_id("main-content")
        main = driver.find_element_by_xpath("//*[@class = 'show-more-less-html__markup show-more-less-html__markup--clamp-after-5']")
        # text = texts.get_attribute('innerHTML')
        # bunch_texts.append(text)
        bp = main.find_elements_by_xpath('.//ul')
        for n in bp:
            tx = n.get_attribute('innerText')
            txt = tx.split('\n')
        bullets.extend(txt)
    except:
        bullets.append(None)

final_list = [i for i in bullets if i] #removing empty strings

#now text mining
words = []
for s in final_list:
    sentence = s.split(' ')
    sentence = [i.lower() for i in sentence]
    words.extend(sentence)

keywords = {'planning': None, 'communication': None, 'analy': None} #not sure how to do a wild card thing like analy*

for kw in keywords.keys():
    word_count = len(fnmatch.filter(words, f'{kw}*'))
    keywords[kw] = word_count

