from mocourtscraper.utilities import chromedriver,case_spider_helper
from mocourtscraper.constants import search_options, navigation
from mocourtscraper.scripts import results_parse
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pprint
from urllib.parse import urlencode, quote
import pandas as pd

content = open('mocourtscraper/utilities/cases.html')
#content = open('/home/zkilburn/projects/consulting/mocourtscraper/cases-no-results.html')
soup = BeautifulSoup(content, features='lxml')

df = results_parse.get_results(soup)
print(df.head())