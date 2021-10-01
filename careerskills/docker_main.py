from link_scraper import LinkScraper
from skill_mining import TextMiner

job = input("Title of job you want to search: ")
location = input('Location: ')
chrome_path = input('Absolute path to your Chrome driver: ')

scaper = LinkScraper(job, location, chrome_path)
scaper.scrape()

miner = TextMiner(job, location, chrome_path)
miner.getText()
