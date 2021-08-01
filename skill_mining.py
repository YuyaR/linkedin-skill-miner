import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from bs4 import SoupStrainer
# import requests
# from requests_html import HTMLSession
import fnmatch
import matplotlib.pyplot as plt

DF = pd.read_csv('./job_data.csv')
final_list = []

def getText(n=len(DF)):
    links = list(DF['Link'][:n])
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path="/Users/yuyara/Downloads/chromedriver 2") 

    bullets = []
    for url in links:
        # session = HTMLSession()
        # r = session.get(url)
        # soup = BeautifulSoup(r.content, 'html.parser')
        
        # main = soup.find_all(id="job-details")
        # main = soup.find('div', attrs = {"id":["careers"]})
        # main = soup.findAll('div', attrs={"class": ["jobs-box__html-content jobs-description-content__text t-14 t-normal"]})
        # texts = main.find('span')
        # print(texts.text)

        driver.get(url)
        try:
            main = driver.find_element_by_xpath("//*[@class = 'show-more-less-html__markup show-more-less-html__markup--clamp-after-5']")
            bp = main.find_elements_by_xpath('.//ul')
            for n in bp:
                tx = n.get_attribute('innerText')
                txt = tx.split('\n')
            bullets.extend(txt)
        except:
            bullets.append(None)

        # text = texts.get_attribute('innerHTML')
        # bunch_texts.append(text)

    final_list = [i for i in bullets if i] #removing empty strings
    return final_list

def mineText():
    words = []
    for s in final_list:
        sentence = s.split(' ')
        sentence = [i.lower() for i in sentence]
        words.extend(sentence)

    global keywords

    keywords = {'planning': None, 'communication': None, 'analy': None, 'organi': None,
     'independen': None, 'creativ': None, 'collabor': None, 'manage': None, 'initiat': None, 'lead': None}

    for kw in keywords.keys():
        word_count = len(fnmatch.filter(words, f'{kw}*'))
        keywords[kw] = word_count

def plot(dic):
    skills = ['planning', 'communication', 'analysis', 'organisation', 'independence', 'creativity', 'collaboration', 'management', 'initiative', 'leadership']
    plt.bar(x=skills, height=dic.values())
    plt.title('The top 10 Skills desired in your dream job!')
    plt.show()

# if __name__ == '__main__':
#     mine()
#     print(keywords)
    