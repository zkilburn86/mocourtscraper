from mocourtscraper.utilities import chromedriver,case_spider_helper
from mocourtscraper.constants import search_options, navigation
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pprint
from urllib.parse import urlencode, quote

params = {
    'location_description': 'All',
    'case_status': 'All',
    'start_date': '01/21/2021',
    'case_type': 'Criminal',
    'county_description': 'All'
}
params['court_description'] = search_options.COURT_DESCRIPTIONS[5]

print(case_spider_helper.build_url(params))

params.pop('court_description')

print(case_spider_helper.build_url(params))