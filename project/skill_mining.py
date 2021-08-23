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

#TODO: make import-all file
#TODO: see if can skip creating the data frame

class TextMiner(LinkScraper):
    '''
    This class inherits the following attributes from LinkScraper:

    Attributes:
        job: type of job for search (case-insensitive)
        location: the location where the jobs are posted (case-insensitive)
        chrome_path: the path to Chrome Driver on your device

    It contains methods that scrape the bulletpoints from each job listing 
    collected from Linkedin, then count the number of occurrence for ten
    most common transferable skills. 
    The result is displayed by a barplot.
    '''
    DF = pd.read_csv('./job_data.csv')

    def getText(self, n=len(DF)):
        '''
        This function uses selenium to scrape all bullet points from each job listing (from links)

        Arguments:
            n: the number of links/jobs to get information from (if list too long, 
                user may consider selecting only first n jobs). Default is whole list.
        Returns:
            a barplot displaying the resulting count for each skill
        '''

        links = list(DF['Link'][:n])
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=self.chrome_path) 

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
        
        self.mineText(final_list)

        self.plot(keywords)

    def mineText(self, final_list):
        '''
        This method counts how many times each of the skill keyword in the keywords dictionary
        is found in the scraped bullet points

        Returns: 
            a dictionary with the skill and its number of occurrence
        '''
        words = []
        for s in all_text:
            sentence = s.split(' ')
            sentence = [i.lower() for i in sentence]
            words.extend(sentence) #collects individual lowercased words from scraped bulletpoint texts

        global keywords

        keywords = {'plan': None, 'communicat': None, 'analy': None, 'organi': None,
                    'independen': None, 'creativ': None, 'collabor': None, 'manage': None, 
                    'initiat': None, 'lead': None}

        for kw in keywords.keys():
            word_count = len(fnmatch.filter(words, f'{kw}*')) #allow wildcard matching of words with specified beginning
            keywords[kw] = word_count

    #TODO: make graph horizontal (if not wordcloud)

    @staticmethod
    def plot(dic):
        '''
        a static method visualising the frequency of occurrence of each skill in a barplot.
        '''
        skills = ['planning', 'communication', 'analysis', 'organisation', 'independence', 'creativity', 'collaboration', 'management', 'initiative', 'leadership']
        plt.bar(x=skills, height=dic.values())
        plt.title('How the Top Transferable Skills are Desired in Your Dream Job')
        plt.show()

    # if __name__ == '__main__':
    #     mine()
    #     print(keywords)
        