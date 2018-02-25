from bs4 import BeautifulSoup
from requests.sessions import Session, HTTPAdapter
from requests import get
import pandas as pd
from time import sleep
from random import randrange

#
# url = 'http://www.monash.edu/students/scholarships/current/merit-academic-achievement'
# response = get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# n = soup.find('div', id="content_container_667807")
#
# # start
#
# faculty = []
# scholarship = []
# link = []
#
# t = n.find_all('li')
# for item in t:
#     faculty.append(item.find_parent().find_previous().text)
#     scholarship.append(item.a.text)
#     link.append(item.a.get('href'))
#
# table = pd.DataFrame({'scholarships': scholarship, 'faculty': faculty, 'link': link})
# print(table['link'][0])

s = Session()
s.mount('http://www.monash.edu/students/scholarships/current/merit-academic-achievement',
        HTTPAdapter(max_retries=100))
response = get('http://www.monash.edu/students/scholarships/current/merit-academic-achievement')
print(response.text)
