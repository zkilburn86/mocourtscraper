from mocourtscraper.utilities import chromedriver,case_search_spider_helper
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
import json

""" driver = chromedriver.driver()
driver.get('https://www.courts.mo.gov/casenet/cases/header.do?inputVO.caseNumber=200833276&inputVO.courtId=SMPDB0001_CT06')
content = driver.page_source
soup = BeautifulSoup(content, features='lxml')

detail_labels = soup.find_all('td', 'detailLabels')
detail_data = soup.find_all('td', 'detailData')
indexer = 0
header_result = {}
for label in detail_labels:
    if label.text.strip() != '':
        header_result[label.text.strip()] = detail_data[indexer].text.strip()
    indexer += 1

json_str = json.dumps(header_result)
print(json_str) """

