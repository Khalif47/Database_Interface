from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from time import sleep
import re
from random import randrange

url = 'https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/monash-scholarship-for-excellence-5764'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
if soup.find('p', text='Total scholarship value').find_next() is not None:
    t = soup.find('p', text='Total scholarship value').find_next().text
    print(t)
elif soup.find('strong', text='Benefits') is not None:
    t = soup.find('strong', text='Benefits').find_next().text
    print(t)

t = []

n =32
if n != []:
    print(1)

# value =[]

# else:
#     delete entry



