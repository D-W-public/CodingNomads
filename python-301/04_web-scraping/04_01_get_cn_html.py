# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

import requests
from bs4 import BeautifulSoup

page = requests.get("https://codingnomads.co/",headers={"User-agent": "Mozilla/5.0"})
soup = BeautifulSoup(page.text, "lxml")
print(soup.body.get_text(" ", strip=True))