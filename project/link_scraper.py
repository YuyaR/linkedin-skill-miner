from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

'''
This module contains a class which purpose is to scrapes all hrefs (links) to the returned hits
for a job search with a specified location on Linkedin.
'''


options = Options()
options.headless = True


class LinkScraper:
    '''
    class attributes:
        job: type of job for search (case-insensitive)
        location: the location where the jobs are posted (case-insensitive)
        chrome_path: the path to Chrome Driver on your device
        driver: a command used to perform most scraping tasks, containing the specified Chrome Driver path
    '''

    def __init__(self, job: str, location: str, chrome_path: str):
        self.job = job
        self.location = location
        self.chrome_path = chrome_path

        self.driver = webdriver.Chrome(
            options=options, executable_path=(chrome_path))

    @staticmethod
    def _process(x: str):
        '''
        This static method changes the entered string into correct format to be inserted in the url

        Returns:
            str: lower case string with space replaced with correct representation in url format
        '''
        x = x.lower()
        x = x.replace(' ', '%20')
        return x

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        self.__job = self._process(job)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = self._process(location)

    def _scroll(self):
        '''
        This static method scrolls to the bottom of the Linkedin page
        Used after the search
        '''

        while True:
            oldH = 0
            latestH = 1
            while oldH != latestH:
                oldH = self.driver.execute_script(
                    'return document.body.scrollHeight')
                self.driver.execute_script(f'window.scrollTo(50, {oldH})')
                time.sleep(1)
                latestH = self.driver.execute_script(
                    'return document.body.scrollHeight')

            try:
                button = self.driver.find_element_by_xpath(
                    '//*[@id="main-content"]/section[2]/button')
                # clicks button for more to scroll
                action.move_to_element(button).click().perform()
            except:
                break

            time.sleep(0.5)
            self.driver.execute_script(f'window.scrollTo(50, {latestH}+{500})')
            time.sleep(0.5)
            latestH = self.driver.execute_script(
                'return document.body.scrollHeight')

            if oldH == latestH:
                break

    @staticmethod
    def _remove_dup(df):
        '''
        This static method uses the job listing title and employer name to drop duplicated listings
        and stores the unique results in a dataframe
        Returns dataframe in local repository under name 'job_data.csv'
        '''
        DF = df.drop_duplicates(['Title', 'Employee'])

        DF.to_csv('./job_data.csv', index=False, header=True)

    def scrape(self):
        '''
        This function performs the webscrapping, also using the static methods in the same class.
        '''

        url = f'https://www.linkedin.com/jobs/search/?keywords={self.job}&location={self.location}'

        self.driver.get(url)

        time.sleep(2)

        self._scroll()

        listings = self.driver.find_element_by_xpath(
            '//*[@id="main-content"]/section[2]/ul')  # contains all posts
        posts = listings.find_elements_by_xpath(
            './/*[@class="base-card__full-link"]')  # contains hyperlink
        len(posts)
        titles = listings.find_elements_by_xpath(
            './/*[@class="base-search-card__info"]/h3')  # contains job titles
        company = listings.find_elements_by_xpath(
            './/*[@class="base-search-card__info"]/h4/a')  # contains employee name

        link = []
        title = []
        employee = []
        for i in range(len(posts)):
            link.append(posts[i].get_attribute('href'))
            title.append(titles[i].text)
            employee.append(company[i].text)

        self.driver.close()

        df = pd.DataFrame(list(zip(title, employee, link)),
                          columns=['Title', 'Employee', 'Link'])

        self._remove_dup(df)


if __name__ == '__main__':
    sc = LinkScraper('conservation', 'Japan',
                     '/Users/yuyara/Downloads/chromedriver 2')
    sc.scrape()
