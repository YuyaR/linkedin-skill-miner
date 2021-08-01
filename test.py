import skill_mining as sm
import link_scraper as ls
import pandas as pd

input = pd.read_csv('./input.csv')
input=pd.read_csv('/Users/yuyara/Documents/Coding/python/Data_pipeline/Career_skill/input.csv')

for i in range(len(input)):
    ls.scrape(input['Job'][i], input['Location'][i])
    assert 



