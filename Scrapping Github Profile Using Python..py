# Scrapping Github Profile Using Python.

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.comkalyan4636"
req = requests.get(github_profile)
profile_picture = scraper.find("img", {"alt": "Avtar"})["src"]
print(profile_picture)
