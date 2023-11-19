import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://nextspaceflight.com/launches/past/?search=")
data = response.text
soup = BeautifulSoup(data, 'html.parser')

organizations = soup.select('.mdl-card__title-text > span')
organizations = [organization.text.strip() for organization in organizations]

dates = soup.select('.mdl-card__supporting-text > span')
dates = [date.text.strip() for date in dates]

descriptions = soup.select('.mdl-card > h5')
descriptions = [description.text.strip() for description in descriptions]

print(descriptions)
