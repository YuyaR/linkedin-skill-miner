import pandas as pd
from link_scraper import LinkScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import fnmatch
import matplotlib.pyplot as plt

# from bs4 import BeautifulSoup
# from bs4 import SoupStrainer
# import requests
# from requests_html import HTMLSession


class TextMiner:
    '''
    This class inherits the following attributes from LinkScraper:

    Attributes:
        chrome_path: the path to Chrome Driver on your device

    It contains methods that scrape the bulletpoints from each job listing 
    collected from Linkedin, then count the number of occurrence for ten
    most common transferable skills. 
    The result is displayed by a barplot.
    '''

    def __init__(self, job, loc, chrome_path):
        self.job = job
        self.loc = loc
        self.chrome_path = chrome_path
        self.DF = pd.read_csv('./job_data.csv')

    def getText(self):
        '''
        This function uses selenium to scrape all bullet points from each job listing (from links)

        Arguments:
            n: the number of links/jobs to get information from (if list too long, 
                user may consider selecting only first n jobs). Default is whole list.
        Returns:
            a barplot displaying the resulting count for each skill
        '''

        n = len(self.DF)
        if n > 100:
            n = 100  # too many job listings can take too long to mine

        links = list(self.DF['Link'][:n])
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(
            options=options, executable_path=self.chrome_path)

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
            # text = texts.get_attribute('innerHTML')
            # bunch_texts.append(text)

            driver.get(url)
            try:
                main = driver.find_element_by_xpath(
                    "//*[@class = 'show-more-less-html__markup show-more-less-html__markup--clamp-after-5']")
                bp = main.find_elements_by_xpath('.//ul')
                for n in bp:
                    tx = n.get_attribute('innerText')
                    txt = tx.split('\n')
                bullets.extend(txt)
            except:
                pass

        final_list = [i for i in bullets if i]  # removing empty strings

        print(final_list)

        self._mineText(final_list)

        self._plot(keywords)

    def _mineText(self, final_list):
        '''
        This method counts how many times each of the skill keyword in the keywords dictionary
        is found in the scraped bullet points

        Returns: 
            a dictionary with the skill and its number of occurrence
        '''
        words = []
        for s in final_list:
            sentence = s.split(' ')
            sentence = [i.lower() for i in sentence]
            # collects individual lowercased words from scraped bulletpoint texts
            words.extend(sentence)

        global keywords

        keywords = {'plan': None, 'communicat': None, 'analy': None, 'organi': None,
                    'independen': None, 'creativ': None, 'collabor': None, 'manage': None,
                    'initiat': None, 'lead': None}

        for kw in keywords.keys():
            # allow wildcard matching of words with specified beginning
            word_count = len(fnmatch.filter(words, f'{kw}*'))
            keywords[kw] = word_count

    @staticmethod
    def _plot(dic):
        '''
        a static method visualising the frequency of occurrence of each skill in a barplot.
        '''
        skills = ['planning', 'communication', 'analysis', 'organisation', 'independence',
                  'creativity', 'collaboration', 'management', 'initiative', 'leadership']
        plt.barh(skills, dic.values())
        plt.title('How Top Transferable Skills are Desired in Your Dream Job')
        plt.show()


if __name__ == '__main__':
    m = TextMiner('/Users/yuyara/Downloads/chromedriver 2')
    m.getText()
    print(keywords)
