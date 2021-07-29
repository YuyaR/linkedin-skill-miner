from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

def scrape(job: str, location: str):
    options = Options()
    options.headless = False #change to True if you don't want the browser to actually open
    driver = webdriver.Chrome(options=options, executable_path="/Users/yuyara/Downloads/chromedriver 2") 
    action = ActionChains(driver)

    job = job.lower()
    location = location.lower()
    url = f'https://www.linkedin.com/jobs/search/?keywords={job}&location={location}'

    driver.get(url)

    time.sleep(2)

    while True:
        oldH = 0
        latestH = 1
        while oldH != latestH:
            oldH = driver.execute_script('return document.body.scrollHeight')
            driver.execute_script(f'window.scrollTo(50, {oldH})')
            time.sleep(1)
            latestH = driver.execute_script('return document.body.scrollHeight')
        
        try:
            button = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]/button')
            action.move_to_element(button).click().perform()
        except:
            break
        time.sleep(0.5)
        driver.execute_script(f'window.scrollTo(50, {latestH}+{500})')
        time.sleep(0.5)
        latestH = driver.execute_script('return document.body.scrollHeight')
        
        if oldH == latestH:
            break

    listings = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]/ul') #contains all posts
    posts = listings.find_elements_by_xpath('.//*[@class="base-card__full-link"]') #contains hyperlink
    len(posts)
    titles = listings.find_elements_by_xpath('.//*[@class="base-search-card__info"]/h3') #contains job titles
    company = listings.find_elements_by_xpath('.//*[@class="base-search-card__info"]/h4/a') #contains employee name

    link = []
    title = []
    employee = []
    for i in range(len(posts)):
        link.append(posts[i].get_attribute('href'))
        title.append(titles[i].text)
        employee.append(company[i].text)

    raw_data = pd.DataFrame(list(zip(title, employee, link)), columns=['Title', 'Employee', 'Link'])

    DF = raw_data.drop_duplicates(['Title','Employee'])

    DF.to_csv('~/job_data.csv', index=False, header=True)

    driver.close()